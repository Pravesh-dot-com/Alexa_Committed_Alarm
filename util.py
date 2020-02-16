# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 00:03:44 2020

@author: Pravesh
"""
"""Utility module to generate text for commonly used responses."""

import random
from random import choice

from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data


def demo_get_current_score(score, counter):
    """Return the response text for current demo score of the user."""
    return data.SCORE.format("current", score, counter)


def demo_get_final_score(score, counter):
    """Return the response text for final demo score of the user."""
    return data.SCORE.format("final", score, counter)



def demo_get_ordinal_indicator(counter):
    """Return st, nd, rd, th ordinal indicators according to counter."""
    if counter == 1:
        return "1st"
    elif counter == 2:
        return "2nd"
    elif counter == 3:
        return "3rd"
    else:
        return "{}th".format(str(counter))



def demo_get_question(counter, item):
    """Return response text for nth question to the user."""
    return (
        " Here is your {} question. What is  {} . " 
        " {} ").format(
        demo_get_ordinal_indicator(counter), item, choice(data.sounds_buzzer))


def demo_get_answer(result):
    """Return response text for correct answer to the user."""
    return (" The correct answer is {} . ").format(result.replace('-','minus'))

def demo_ask_question(handler_input):
    # (HandlerInput) -> None
    """Get a random state and property, return question about it."""
    one_digit_f = 1
    one_digit_l = 10
    rand = random.sample(range(one_digit_f,one_digit_l),3)
    a, b, c = rand
    operator = [choice('+-'), choice('+-')]
    
    x = str(a)+operator[0]+str(b)+operator[1]+str(c)
    
    if x[1] == '+':
        result = a+b
        if x[3] == '+':
            result += c
        else:
            result -= c
    else:
        result = a-b
        if x[3] == '+':
            result += c
        else:
            result -= c
    
    x = x.replace('-','minus')
            
    #return x.replace('-','minus'), result

    attr = handler_input.attributes_manager.session_attributes

    attr["exp"] = x
    attr["result"] = result
    attr["counter"] += 1

    handler_input.attributes_manager.session_attributes = attr

    return demo_get_question(attr["counter"], x )


def demo_get_speechcon(correct_answer):
    """Return speechcon corresponding to the boolean answer correctness."""
    text = ("{} <say-as interpret-as='interjection'>{} !"
            "</say-as><break strength='strong'/>")
    if correct_answer:
        return text.format(random.choice(data.sounds_trumpet), random.choice(data.CORRECT_SPEECHCONS))
    else:
        return text.format(random.choice(data.sounds_bloop), random.choice(data.WRONG_SPEECHCONS))



    
def demo_compare_slots(handler_input, value):
    """Compare slot value to the value provided."""
    slot = handler_input.request_envelope.request.intent.slots
    
    val = int(slot["answer"].value)
    
    if val is not None:
        return val == value
    else:
        return False
    
def get_set_alarm_val(handler_input):
    """Compare slot value to the value provided."""
    slot = handler_input.request_envelope.request.intent.slots
    
    val = slot["time"].value
    
    if val is not None:
        return val
    else:
        return 'Nothing to show'      
