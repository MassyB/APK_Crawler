# APK_Crawler
A python 3 script for downloading APKs from the google Play Store
# Dependencies
- python 3.5+
- npm package [node-google-play](https://github.com/MassyB/node-google-play)
- npm pkcage [node-google-play-cli](https://github.com/dweinstein/node-google-play-cli)

# Input
Text files containing the package names to be downloaded :
- topselling_free_ART_AND_DESIGN.txt
- topselling_free_GAME.txt
- topselling_free_VIDEO_PLAYERS.txt
- ...etc.

# Output
Directories containing the APKs, each directory for each text file.

# Usage
In the `apkCrawler.py` you must provide correct values for : `GOOGLE_LOGIN`, `GOOGLE_PASSWORD` and `ANDROID_ID`. Refere to [node-google-play-cli](https://github.com/dweinstein/node-google-play-cli) for more details.

The script works on text files named according to the pattern `r'topselling_free_\w+\.txt'`. Each text file contains one package name per line. You can: 
- provide your own package names
- use [my apk Scrapper](https://github.com/MassyB/APK_scraping)
- use [42Matters API](https://42matters.com/launchpad) (you need to parse the result).

The script verifies if the APK is already downloaded, so you can launch it multiple times, it will continue the download not restart form zero.

