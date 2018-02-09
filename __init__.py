# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
import time
url = "http://localhost:8080/"

__author__ = 'laurasomsen'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class HTTPSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(HTTPSkill, self).__init__(name="HTTPSkill")	


    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
	game_intent = IntentBuilder("GameIntent")\
           .require("GameKeyword").build()
        self.register_intent(game_intent,
                            self.handle_game_intent)

	self.load_data_files(dirname(__file__))
	skype_intent = IntentBuilder("SkypeIntent")\
           .require("SkypeKeyword").build()
        self.register_intent(skype_intent,
                            self.handle_skype_intent)

	self.load_data_files(dirname(__file__))
	guide_intent = IntentBuilder("GuideIntent")\
           .require("GuideKeyword").build()
        self.register_intent(guide_intent,
                            self.handle_guide_intent)

	self.load_data_files(dirname(__file__))
	nurse_intent = IntentBuilder("NurseIntent")\
           .require("NurseKeyword").build()
        self.register_intent(nurse_intent,
                            self.handle_nurse_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.

    def handle_game_intent(self):
        self.speak_dialog("game")
	r = requests.post(url, data = {'key':'game'})
	if(r.status_code==200):
		LOGGER.debug("Information was sent properly")
	else:
		LOGGER.debug("Information wasn't sent properly")

    def handle_skype_intent(self):
        self.speak_dialog("skype")
	r = requests.post(url, data = {'key':'skype'})
	if(r.status_code==200):
		LOGGER.debug("Information was sent properly")
	else:
		LOGGER.debug("Information wasn't sent properly")

    def handle_guide_intent(self):

	location = self.get_response("guide.question")
        self.speak_dialog("guide")
	r = requests.post(url, data = {'key': location})
	if(r.status_code==200):
		LOGGER.debug("Information was sent properly")
	else:
		LOGGER.debug("Information wasn't sent properly")

    def handle_nurse_intent(self):
        self.speak_dialog("nurse")
	r = requests.post(url, data = {'key':'nurse'})
	if(r.status_code==200):
		LOGGER.debug("Information was sent properly")
	else:
		LOGGER.debug("Information wasn't sent properly")
	

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return HTTPSkill()
