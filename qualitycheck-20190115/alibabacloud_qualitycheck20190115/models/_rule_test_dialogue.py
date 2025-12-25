# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class RuleTestDialogue(DaraModel):
    def __init__(
        self,
        content: List[main_models.RuleTestDialogueContent] = None,
        id: int = None,
        name: str = None,
        user_group: str = None,
    ):
        self.content = content
        self.id = id
        self.name = name
        self.user_group = user_group

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.RuleTestDialogueContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        return self

class RuleTestDialogueContent(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: int = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

