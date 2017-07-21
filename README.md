# daily-wallpaper-ubuntu16.04
A script that changes your wallpaper to the bing image of the day. 

**To-Do:**
* Add a scheduler to make the script run automatically and not block the processor while its waiting (no sleep(time))
	**USE CRON INSTEAD**
* Make it run as a script on startup.
* Add a check for whether internet is connected or not.

**Usage:**
* One time use:

	Download the script ```onetimechange.py``` and execute it from the correct directory. Your wallpaper will be changed and the image downloaded as a jpg.

	```
	python3 onetimechange.py
	```

* To create a recurring job, can use crontab to schedule when you want the script to execute:
	
	* Open terminal -  ```crontab -e```

	* Choose your preferred editor (nano) move to the end and add the following line - ```10 9 * * * python3 /home/user/Desktop/onetimechange.py```  change the time based on your needs, this executes every day at 9:10 AM [*refer wiki article on cron*](https://en.wikipedia.org/wiki/Cron) 

	* To save press ```CTRL+X``` and then ```Y``` to save the crontab file.


* To change your region, edit the marked areas in the script ```onetimechange.py```.

	```python
	### CHANGE THESE IF NEEDED ###

	# Possible regions : en-US, zh-CN, ja-JP, en-AU, en-UK, de-DE, en-NZ, ru-RU
	resu = '1920x1080'
	region = 'en-US'

	##############################
	```

The images are downloaded and stored at ```~/Pictures/Daily Bing Wallpapers/``` .

The format of the image names is ```mm_dd__YYYY_region.jpg```

**Requirements:**

* Python 3
* Tested for Ubuntu 16.04 but should work with 14.04 as well.

**Errors/Troubleshooting:**

* The background doesn't change on my virtual machine running 16.04.2 the following is the error. Haven't been unable to solve the problem.

```Using the 'memory' GSettings backend.  Your settings will not be saved or shared with other applications.```

