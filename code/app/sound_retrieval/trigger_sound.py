import pygame, os, time
import json

SOUND_DIR = '/Users/deirdre/git/Msc_Project/code/app/sound_retrieval/'

def play_sound_with_pygame(input_file):
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(os.path.join(SOUND_DIR, input_file))
	pygame.mixer.music.play()
	stopwatch(3)
	pygame.mixer.stop()

def retrieve_list_of_sounds(search_string_list):
	obj_list = []
	for x in search_string_list:
		return_string_id, sound_to_trigger = search_sounds(x)
		obj_list.append(sound_to_trigger)
	return obj_list

def search_sounds(search_string):
	return_string_id = ''
	sound_to_trigger = ''

	with open(os.path.join(SOUND_DIR,'sound_list.json')) as f:
	    data = json.loads(f.read())

	for i in data:
		if search_string in i['display_name']:
			print(i['display_name'],'found')
			return_string_id = i['id']
			sound_to_trigger = i['sound']
			print(i['sound'])
			break
		else:
			return_string_id = 'NO MATCH FOUND'

	return return_string_id, sound_to_trigger

def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start


# return_string_id, sound_to_trigger = search_sounds('kite')
# play_sound_with_pygame(sound_to_trigger)
