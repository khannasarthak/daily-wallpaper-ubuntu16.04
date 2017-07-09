#!/usr/bin/python3
import requests
import json
from datetime import datetime
import os
import os.path, time
from os.path import expanduser
from urllib.request import urlopen
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
	direc = expanduser("~") +'/Pictures/PyBing Wallpapers/'
	ext = '.jpg'

	print ('----------------------------------------')
	print ('-------DAILY WALLPAPER SWITCHER---------')
	print ('----------------------------------------','\n')
	print ('You can change the resolution ( default : 1920x1080) and region ( default: ru-RU) by editing the dload.py file','\n')


	### CHANGE THESE IF NEEDED ###

	# Possible regions : en-US, zh-CN, ja-JP, en-AU, en-UK, de-DE, en-NZ, ru-RU
	resu = '1920x1080'
	region = 'en-US'

	##############################


	r = requests.get(url='http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=' + region)
	obj = r.json()
	url= ((obj['images'][0]['urlbase']))
	url = 'http://www.bing.com' + url + '_' + resu + '.jpg'

	if not os.path.exists(direc):
	    os.makedirs(direc)
	    print ('New folder created at ~/Pictures/PyBing Wallpapers/')

	todayDate = datetime.now().strftime("%m/%d/%Y")
	namek = (str(todayDate)+'_'+region+ext)
	name = namek.replace('/','_')
	path = direc+name
	if os.path.isfile(path):
		print ("Today's image has already been downloaded.")
	else:
		print ("Downloading image for date:",name)
		f = open(path, 'wb')
		newpic = urlopen(url)
		f.write(newpic.read())


	cmd = 'gsettings set org.gnome.desktop.background picture-uri '
	loc = 'file://'+path # exact location is needed.
	command = cmd+'"'+loc+'"'
	try : 
		os.system(command)
		print ('Wallpaper successfully changed')
	except Exception as e:
		print('Error while changing wallpaper', e)

main()
sched = BlockingScheduler()
@sched.scheduled_job( 'cron',hour = 6)
def scheduled_job():
	print ("FROM SCHEDULER")
	main()	
sched.start()

	