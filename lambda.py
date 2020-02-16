# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:34:03 2020

@author: pjoshi
"""

import json
import logging

from ask_sdk_core.api_client import DefaultApiClient
from ask_sdk_core.skill_builder import SkillBuilder, CustomSkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.serialize import DefaultSerializer
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response
from alexa import data, util
from random import choice

from datetime import datetime 
import pytz

from ask_sdk_model.services.reminder_management import Trigger, TriggerType, AlertInfo, SpokenInfo, SpokenText, \
    PushNotification, PushNotificationStatus, ReminderRequest



# Skill Builder object
#sb = SkillBuilder()

sb = CustomSkillBuilder(api_client=DefaultApiClient())


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Request Handler classes
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")
        handler_input.response_builder.speak(data.WELCOME_MESSAGE.format(choice(data.sounds_welcome))).ask(
            data.SET_MESSAGE.format(choice(data.sounds_welcome_2)))
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        print("Session ended with reason: {}".format(
            handler_input.request_envelope))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for help intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        handler_input.attributes_manager.session_attributes = {}
        # Resetting session

        handler_input.response_builder.speak(
            data.SET_MESSAGE).ask(data.SET_MESSAGE)
        return handler_input.response_builder.response




class AllInOneExitIntentHandler(AbstractRequestHandler):
    #Single Handler for Cancel, Stop and Pause intents.
    #Note that this skill can't be stopped once it enters TriggerAlarm Intent/State. 
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.PauseIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        response_builder = handler_input.response_builder
        
        if attr.get("state") == "AlarmTriggered":
            
            logger.info("In AllInOneExitIntentHandler Exit after Alarm triggered")
            handler_input.response_builder.speak(data.EARLY_EXIT_SKILL_MESSAGE.format(choice(data.sounds_buzzer)))
            return handler_input.response_builder.response
        
        elif attr.get("state") == "Demo":
            
            logger.info("In AllInOneExitIntentHandler Exit during Demo")
            attr["state"] = "DemoEnded"
            handler_input.response_builder.speak(data.EXIT_DEMO_MESSAGE.format(choice(data.sounds_trumpet)))
            return handler_input.response_builder.response
        
        else :
            logger.info("In AllInOneExitIntentHandler Normal Exit")
            handler_input.response_builder.speak(data.EXIT_SKILL_MESSAGE)
            response_builder.set_should_end_session(True)
            return handler_input.response_builder.response



class SetCommittedAlarmHandler(AbstractRequestHandler):
    """Handler for setting the committed alarm.
    The ``handle`` method will initiate a SetAlarm state and set the alarm for the requested time.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("SetCommittedAlarmIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SetCommittedAlarmHandler")
        #slot = handler_input.request_envelope.request.intent.slots
        
        """
        time_val = util.get_set_alarm_val(handler_input)
        
        print('pravesh output : type of time_val - {} ; value of time_val - {}'.format(type(time_val) , time_val))
        
                               
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "SetCommittedAlarm"
        attr["time"] = time_val
        
        """
        rb = handler_input.response_builder
        permissions = handler_input.request_envelope.context.system.user.permissions
        reminder_service = handler_input.service_client_factory.get_reminder_management_service()
        print( 'pravesh out - permissions : {} '.format(permissions))

        """
        if not (permissions and permissions.consent_token):
            logging.info("user hasn't granted reminder permissions")
            return rb.speak("Please give permissions to set reminders using the alexa app.").response
        """
        
        now = datetime.datetime.now()#(pytz.timezone(TIME_ZONE_ID))
        five_mins_from_now = now + datetime.timedelta(seconds=+20)
        notification_time = five_mins_from_now.strftime("%Y-%m-%dT%H:%M:%S")

        trigger = Trigger(TriggerType.SCHEDULED_ABSOLUTE, notification_time)#, time_zone_id=TIME_ZONE_ID)
        text = SpokenText(locale='en-IN', ssml='<speak>This is your reminder</speak>', text='This is your reminder')
        alert_info = AlertInfo(SpokenInfo([text]))
        #push_notification = PushNotification(PushNotificationStatus.ENABLED)
        reminder_request = ReminderRequest(notification_time, trigger, alert_info)

        try:
            reminder_responce = reminder_service.create_reminder(reminder_request)
        except ServiceException as e:
            # see: https://developer.amazon.com/docs/smapi/alexa-reminders-api-reference.html#error-messages
            logger.error(e)
            raise e

        return rb.speak("reminder created").set_should_end_session(True).response

"""
        response_builder = handler_input.response_builder
        response_builder.speak(data.ALARM_SET_MESSAGE.format(time_val))
        response_builder.ask(data.SET_MESSAGE)

        return response_builder.response
"""







class DemoHandler(AbstractRequestHandler):
    """Handler for starting a Demo.
    The ``handle`` method will initiate a demo state and build 
    questions randomly using the util methods.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("DemoIntent")(handler_input) or
                is_intent_name("AMAZON.StartOverIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In DemoHandler")
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "Demo"
        attr["counter"] = 0
        attr["score"] = 0

        question = util.demo_ask_question(handler_input)
        response_builder = handler_input.response_builder
        response_builder.speak(data.START_DEMO_MESSAGE.format(choice(data.sounds_welcome),choice(data.sounds_welcome_2)) + question)
        response_builder.ask(question)

        return response_builder.response



class DemoAnswerHandler(AbstractRequestHandler):
    """Handler for Demo.
    The ``handle`` method will check if the answer specified is correct,
    by checking if it matches with the corresponding session attribute
    value. According to the type of answer, alexa responds to the user
    with either the next question or the final score.
    
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        attr = handler_input.attributes_manager.session_attributes
        return (is_intent_name("AnswerIntent")(handler_input) and
                attr.get("state") == "Demo")

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In DemoAnswerHandler")
        attr = handler_input.attributes_manager.session_attributes
        response_builder = handler_input.response_builder
        print('Pravesh out Inside Demo Answer Handler ')

        #exp = attr["exp"]
        result = attr["result"]
        is_ans_correct = util.demo_compare_slots(
            handler_input=handler_input,
            value=result)

        if is_ans_correct:
            speech = util.demo_get_speechcon(correct_answer=True)
            speech += " Thats correct. "
            attr["score"] += 1
            handler_input.attributes_manager.session_attributes = attr
        else:
            speech = util.demo_get_speechcon(correct_answer=False)
            speech += util.demo_get_answer(str(result))

        if attr['score'] < data.TARGET_CORRECT_ANSWERS:
            # Ask another question
            speech += util.demo_get_current_score(
                attr["score"], attr["counter"])
            question = util.demo_ask_question(handler_input)
            speech += question
            reprompt = question

            return response_builder.speak(speech).ask(reprompt).response
        else:
            # Finished all questions.
            speech += util.demo_get_final_score(attr["score"], attr["counter"])
            speech += data.EXIT_DEMO_MESSAGE.format(choice(data.sounds_trumpet))

            #response_builder.set_should_end_session(True)
            return response_builder.speak(speech).response



class RepeatHandler(AbstractRequestHandler):
    """Handler for repeating the response to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatHandler")
        attr = handler_input.attributes_manager.session_attributes
        response_builder = handler_input.response_builder
        if "recent_response" in attr:
            cached_response_str = json.dumps(attr["recent_response"])
            cached_response = DefaultSerializer().deserialize(
                cached_response_str, Response)
            return cached_response
        else:
            response_builder.speak(data.FALLBACK_ANSWER).ask(data.SET_MESSAGE)
            return response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for handling fallback intent.
     2018-May-01: AMAZON.FallackIntent is only currently available in
     en-US locale. This handler will not be triggered except in that
     locale, so it can be safely deployed for any locale."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        handler_input.response_builder.speak(
            data.FALLBACK_ANSWER).ask(data.SET_MESSAGE)

        return handler_input.response_builder.response


# Interceptor classes
class CacheResponseForRepeatInterceptor(AbstractResponseInterceptor):
    """Cache the response sent to the user in session.
    The interceptor is used to cache the handler response that is
    being sent to the user. This can be used to repeat the response
    back to the user, in case a RepeatIntent is being used and the
    skill developer wants to repeat the same information back to
    the user.
    """
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["recent_response"] = response


# Exception Handler classes
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch All Exception handler.
    This handler catches all kinds of exceptions and prints
    the stack trace on AWS Cloudwatch with the request envelope."""
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Sorry, there was some problem. Please try again!!"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


# Request and Response Loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the request envelope."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.info("Request Envelope: {}".format(
            handler_input.request_envelope))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the response envelope."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.info("Response: {}".format(response))


# Add all request handlers to the skill.
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(DemoHandler())
sb.add_request_handler(AllInOneExitIntentHandler())

sb.add_request_handler(DemoAnswerHandler())
sb.add_request_handler(SetCommittedAlarmHandler())
sb.add_request_handler(RepeatHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(FallbackIntentHandler())

# Add exception handler to the skill.
sb.add_exception_handler(CatchAllExceptionHandler())

# Add response interceptor to the skill.
sb.add_global_response_interceptor(CacheResponseForRepeatInterceptor())
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Expose the lambda handler to register in AWS Lambda.
lambda_handler = sb.lambda_handler()
