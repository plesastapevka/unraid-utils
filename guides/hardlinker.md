# Hardlinker

To run this script:

e.g. newly downloaded show called "Besa" is located in
```
/mnt/user/plex/downloads/Besa.S01-S02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX/
├── Besa.S01.SLOSubs.1080p.WEBRip.x264.AAC-GENOX
│   ├── Besa.S01E01.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E03.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E04.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E05.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E06.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E07.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E08.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E09.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E10.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E11.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   └── Besa.S01E12.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
└── Besa.S02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX
    ├── Besa.S02E01.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E03.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E04.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E05.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E06.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E07.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E08.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E09.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    └── Besa.S02E10.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
2 directories, 22 files
```
To create hardlinks in desired folder e.g. `/mnt/user/plex/shows/Besa/`, the folder should be empty. Corresponding directories such as `Season 1` etc. will be created automatically.

1. First of all install the required packages with `pip install -r requirements.txt`.
2. Run `python3 hardlinker.py /mnt/user/plex/downloads/Besa.S01-S02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX/ /mnt/user/plex/shows/Besa/`.
3. The script will indicate the link it will create. Type `y` and hit enter, or just hit enter to accept the link or type `n` and hit enter to reject the link. 
4. That's pretty much it. The file struture in the newly linked folder should look something like this:

```
/mnt/user/plex/shows/Besa/
├── Season 1
│   ├── Besa.S01E01.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E03.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E04.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E05.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E06.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E07.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E08.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E09.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E10.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   ├── Besa.S01E11.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
│   └── Besa.S01E12.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
└── Season 2
    ├── Besa.S02E01.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E02.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E03.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E04.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E05.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E06.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E07.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E08.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    ├── Besa.S02E09.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4
    └── Besa.S02E10.SLOSubs.1080p.WEBRip.x264.AAC-GENOX.mp4

2 directories, 22 files
```
