# daily-wallpaper-ubuntu16.04
A script that changes your wallpaper to the bing image of the day. 

**To-Do:**
* Add a scheduler to make the script run automatically and not block the processor while its waiting (no sleep(time))
* Make it run as a script on startup.

**Usage:**
Download the script ```onetimechange.py``` and execute it from the correct directory. Your wallpaper will be changed and the image downloaded as a jpg.

```
python3 onetimechange.py
```

To change your region, edit the marked areas in the script.

```python
### CHANGE THESE IF NEEDED ###

# Possible regions : en-US, zh-CN, ja-JP, en-AU, en-UK, de-DE, en-NZ, ru-RU
resu = '1920x1080'
region = 'en-US'

##############################
```

The images are downloaded and stored at ```~/Pictures/Daily Bing Wallpapers/``` .

The format of the image names is ```mm_dd__YYYY_region.jpg```

** Requirements:**
* Python 3
* Tested for Ubuntu 16.04 but should work with 14.04 as well.



