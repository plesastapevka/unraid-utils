import csv
import os
import argparse
import PTN
import time
import shutil


def parse_args():
    parser = argparse.ArgumentParser(prog="Tdarr xref",
                                     description='Read transcoded media from Tdarr CSV export and remove the original files.')
    parser.add_argument('--file', '-f',
                        required=True,
                        help='Tdarr exported CSV file path')
    parser.add_argument('--dir', '-d',
                        required=True,
                        help='Original downloads folder path')
    parser.add_argument('--force',
                        help="If this flag is set, the script will delete all found original files, even those it may skip during the process",
                        action='store_true')
    return parser.parse_args()


def yes_or_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply == "":
        return True
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")


def get_size(start_path='.'):
    if start_path.endswith(".mkv") or start_path.endswith(".mp4"):
        return round(os.path.getsize(start_path) / (1024 * 1024 * 1024), 2)
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return round(total_size / (1024 * 1024 * 1024), 2)


def delete_file(file, interactive=False):
    if not interactive and os.path.isfile(file):
        os.remove(file)
        return True

    if not interactive:
        shutil.rmtree(file)
        return True

    if os.path.isfile(file) and yes_or_no(f"Delete {file}"):
        os.remove(file)
        return True

    if os.path.isdir(file) and yes_or_no(f"Delete folder {file}"):
        shutil.rmtree(file)
        return True

    return False


def find_show_to_delete(element_info, torrent_info, root, element, is_parent=False):
    to_delete = []
    saved_size = 0
    if torrent_info["title"] == "The Grand Tour":
        print(torrent_info)
        print(element_info)
    if not is_parent and torrent_info["title"].lower() != element_info["title"].lower():
        return 0, []
    if element_info["season"] and torrent_info["season"] and torrent_info["season"] != element_info["season"]:
        return 0, []
    print(
        f"Now searching for show {torrent_info['title']} S{torrent_info['season']}E{torrent_info['episode']} in {root}{element}")

    if not os.path.isdir(root + element) and not (element.endswith(".mkv") or element.endswith(".mp4")):
        return get_size(root + element), [root + element]
    if os.path.isdir(root + element):
        print(f"Now searching {root}{element}")
        elements = os.listdir(root + element)
        if len(elements) == 0:
            return 0, root + element
        for sub_element in elements:
            size, to_delete_list = find_show_to_delete(PTN.parse(sub_element), torrent_info, root + element + "/",
                                                       sub_element, True)
            to_delete += to_delete_list
            saved_size += size
    print(element)
    print(element_info)
    print(torrent_info)
    if element_info["episode"] and (element.endswith(".mkv") or element.endswith(".mp4")) and element_info[
        "title"].lower() == torrent_info[
        "title"].lower() and element_info["season"] == torrent_info["season"] and element_info["episode"] == \
            torrent_info["episode"]:
        to_delete += [root + element]
        saved_size += get_size(root + element)
        print(
            f"Added {root + element} of size {get_size(root + element)} GB to delete list. Total size: {saved_size} GB")

    return saved_size, to_delete


def main(csv_file, root, force=False):
    if not root.endswith("/"):
        root = root + "/"
    print(f"Cross referencing files from {csv_file} with files from {root}")
    print(f"Force set to {force}\n")
    # Open the CSV file
    with open(csv_file, "r") as csv_file_read:
        tdarr_export = csv.DictReader(csv_file_read)
        to_delete = []
        saved_size = 0
        for row in tdarr_export:
            if row["newSize"] == '0':
                continue
            torrent_path = row["_id"]
            # TODO: enhance type fetching, idea: from run parameter
            torrent_type = "movie" if torrent_path.split("/")[3] == "movies" else "show"
            torrent_name = os.path.basename(os.path.normpath(torrent_path))
            torrent_info = PTN.parse(torrent_name)
            try:
                for element in os.listdir(root):
                    element_info = PTN.parse(element)
                    if torrent_type == "show":
                        size, to_delete_list = find_show_to_delete(element_info, torrent_info, root, element)
                        to_delete += to_delete_list
                        saved_size += size
                        # print("\n\n")

                    if torrent_type == "movie" and element_info["title"].lower() == torrent_info["title"].lower() and \
                            (element_info["year"] and torrent_info["year"] and element_info["year"] == torrent_info[
                                "year"]):
                        print(
                            f"Staged for delete: {torrent_type} {root + element} of size {get_size(root + element)} GB")
                        to_delete.append(os.path.join(root, element))
                        saved_size += get_size(root + element)
            except KeyError:
                print(f"Error for torrent {torrent_info['title']}")

        if saved_size > 1000:
            saved_size = f"{round(saved_size / 1000, 2)} TB"
        else:
            saved_size = f"{round(saved_size, 2)} GB"
        skipped = []
        deleted = 0
        print(to_delete)
        if force or yes_or_no(f"Folders and files above will be deleted saving collectively {saved_size}. Continue?"):
            print("\nDeleting files...")
            for file in to_delete:
                try:
                    if os.path.getctime(file) > time.time() - 604800:
                        skipped.append(file)
                        continue
                    if delete_file(file):
                        print(f"Deleted {file}")
                        deleted += 1
                except OSError as e:
                    print("Error: %s : %s" % (file, e.strerror))
            print(f"{deleted} files deleted\n")

            if not skipped:
                exit(0)

            deleted = 0
            # Handle skipped files if forced
            if force:
                print("Force deleting skipped files...")
                for file in skipped:
                    try:
                        if delete_file(file):
                            print(f"Deleted {file}")
                            deleted += 1
                    except OSError as e:
                        print("Error: %s : %s" % (file, e.strerror))
                print(f"{deleted} skipped files deleted\n")
                exit(0)

            # Handle skipped files gracefully
            for file in skipped:
                print(
                    f"Skipped {file}, created/modified on {time.strftime('%d %B %Y %H:%M:%S', time.localtime(os.path.getctime(file)))}")
            deleted = 0
            if yes_or_no("Interactively delete skipped files?"):
                for file in skipped:
                    try:
                        if delete_file(file, True):
                            print(f"Deleted {file}")
                            deleted += 1
                    except OSError as e:
                        print("Error: %s : %s" % (file, e.strerror))
                print(f"{deleted} skipped files deleted\n")
                exit(0)

            if yes_or_no("Delete all skipped files?") and yes_or_no("Are you sure?"):
                for file in skipped:
                    try:
                        if delete_file(file, False):
                            print(f"Deleted {file}")
                            deleted += 1
                    except OSError as e:
                        print("Error: %s : %s" % (file, e.strerror))
                print(f"{deleted} skipped files deleted\n")
            exit(0)

        else:
            print("Nothing deleted")
            exit(0)


if __name__ == "__main__":
    args = parse_args()
    main(args.file, args.dir, args.force)
