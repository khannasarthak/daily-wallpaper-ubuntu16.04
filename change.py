import os
# gsettings = '/usr/bin/gsettings'
cmd = 'gsettings set org.gnome.desktop.background picture-uri '
loc = 'file:///home/excrutiator/Desktop/pic/1.jpg' # exact location is needed.
command = cmd+'"'+loc+'"'
print (command)
os.system(command)
print (os.system(command))

