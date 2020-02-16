# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:12:54 2020

@author: pjoshi
"""


WELCOME_MESSAGE = (" {} "
                   " Welcome to the Committed Alarm ! "
                   " Your one stop solution to wake up efficiently in the morning. "
                   "You can ask me to set a committed alarm , or you can ask me to "
                   "start a demo.  What would you like to do? ")

START_DEMO_MESSAGE = (" OK. Get ready for demo. "
                      " {} "
                      " I will ask you some basic math questions . "
                      " You have to answer 5 of them correct . "
                      "For every incorrect answer, I will add one more question. "
                      " {} ")


ALARM_SET_MESSAGE = (" Committed alarm is set for {}. "
                     " You can ask me to set another committed alarm , or you can ask me to "
                     "start a demo, or just say stop to end.  What would you like to do? ")

EXIT_DEMO_MESSAGE = (" {} "
                      " I hope you enjoyed the demo!  "
                      " You can ask me to set a committed alarm , or you can ask me to "
                     "start another demo, or just say stop to end.  What would you like to do? "
                      )

EXIT_SKILL_MESSAGE = (" Sure. " )


EARLY_EXIT_SKILL_MESSAGE = (" {} "
                            " I am sorry! "
                            " but I can't allow you to go back to sleep. "
                            " whatever it takes! remember?  "
                            " Since, this is a demo, you can again ask me to set up your alarm "
                            " or take another demo. "
                            " What would you like to do ? ")


SET_MESSAGE = ("I can set a committed alarm for you which means I'll wake you up whatever it takes."
                "You can ask me to set up your alarm"
                "or if its your first time "
                "You can also test this service by asking me to start "
                "a demo.  What would you like to do? ")

CORRECT_SPEECHCONS = ['Booya', 'All righty', 'Bam', 'Bazinga', 'Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

WRONG_SPEECHCONS = ['Argh', 'Aw man', 'Blarg', 'Blast', 'Boo', 'Bummer',
                    'Darn', "D'oh", 'Dun dun dun', 'Eek', 'Honk', 'Le sigh',
                    'Mamma mia', 'Oh boy', 'Oh dear', 'Oof', 'Ouch', 'Ruh roh',
                    'Shucks', 'Uh oh', 'Wah wah', 'Whoops a daisy', 'Yikes']


sounds_squeaky = ["<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_01'/>","<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_02'/>",
"<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_03'/>","<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_04'/>","<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_05'/>",
"<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_06'/>","<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_07'/>","<audio src='soundbank://soundlibrary/doors/doors_squeaky/squeaky_08'/>"]

sounds_welcome = ["<audio src='soundbank://soundlibrary/alarms/air_horns/air_horn_01'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horn_02'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horn_03'/>",
"<audio src='soundbank://soundlibrary/alarms/air_horns/air_horn_04'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horns_05'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horns_06'/>",
"<audio src='soundbank://soundlibrary/alarms/air_horns/air_horns_07'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horns_08'/>","<audio src='soundbank://soundlibrary/alarms/air_horns/air_horns_09'/>"]

sounds_welcome_2 = ["<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_01'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_02'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_03'/>",
"<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_04'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_05'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_alarm_06'/>",
"<audio src='soundbank://soundlibrary/scifi/amzn_sfx_sirens_01'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_missile_02'/>","<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_missile_03'/>",
"<audio src='soundbank://soundlibrary/scifi/amzn_sfx_scifi_missile_04'/>"]

sounds_bloop = ["<audio src='soundbank://soundlibrary/alarms/beeps_and_bloops/boing_01'/>","<audio src='soundbank://soundlibrary/alarms/beeps_and_bloops/boing_02'/>","<audio src='soundbank://soundlibrary/alarms/beeps_and_bloops/boing_03'/>",
"<audio src='soundbank://soundlibrary/cartoon/amzn_sfx_boing_long_1x_01'/>","<audio src='soundbank://soundlibrary/cartoon/amzn_sfx_boing_med_1x_02'/>","<audio src='soundbank://soundlibrary/cartoon/amzn_sfx_boing_short_1x_01'/>"]

sounds_trumpet = ["<audio src='soundbank://soundlibrary/musical/amzn_sfx_trumpet_bugle_01'/>","<audio src='soundbank://soundlibrary/musical/amzn_sfx_trumpet_bugle_02'/>","<audio src='soundbank://soundlibrary/musical/amzn_sfx_trumpet_bugle_03'/>",
"<audio src='soundbank://soundlibrary/musical/amzn_sfx_trumpet_bugle_04'/>"]

sounds_buzzer = ["<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_01'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_02'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_03'/>",
"<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_04'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_05'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_06'/>",
"<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_07'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_08'/>","<audio src='soundbank://soundlibrary/alarms/buzzers/buzzers_09'/>"]

TARGET_CORRECT_ANSWERS = 5

FALLBACK_ANSWER = (
    "This is fallback answer. Sorry. I can't help you with that. {}".format(SET_MESSAGE))

SCORE = "Your {} score is {} out of {}. "

