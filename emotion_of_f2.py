# -*- coding: utf-8 -*-
import random


def emotions(f):
    emotions_negative_speech = ['Неверно', 'Вы неправы!', 'Неполный ответ', 'Нет']
    emotions_positive_speech = ['Да', 'Всё верно', 'Вы правы', 'Хорошо']
    emotion = '<bml>\n'
    if f:
        emotion += '    <speech>'+ random.choice(emotions_positive_speech) +'</speech>\n'
    else:
        emotion += '    <speech>'+ random.choice(emotions_negative_speech) +'</speech>\n'

    emotion += '</bml>\n'
    return emotion

