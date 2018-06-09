############################################
#Author:  Jill Irvin
#This python program plays or stops a playlist depending on the time of day
#The script is run from a cron task scheduler
#
#Revision 1.0
#6.9.18
############################################

#import the the sonos controller library and datetime library
from soco import SoCo
import datetime

#set player variable to a sonos speaker - speaker set with static IP
player = SoCo('192.168.1.15')

#set comparison variable
now = datetime.datetime.now()

#cron script will run this program at 10pm everynight and 830 am every morning
#for night time, play the sleep music playlist
if now.hour == 22 and now.minute == 0:     
	
	#clear the song queue    
	player.clear_queue()    

	#set playlist variable to sonos playlist    
	#night time music is the 5th one - want to update this to search for playlist by name   
	#playlist = player.get_sonos_playlists()[2]    
	playlist = player.get_sonos_playlists()[4]  
	
	#add playlist to sonos speaker queue    
	player.add_to_queue(playlist)    

	#play from queue method with index as arg    
	player.play()

#if it's morning, stop the sleep music
if now.hour == 8 and now.minute == 30:    
	player.stop()
    

    
