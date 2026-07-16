# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class MeetingFlashMinutesTextResponseBody(DaraModel):
    def __init__(
        self,
        has_next: bool = None,
        next_token: str = None,
        paragraph_list: List[main_models.MeetingFlashMinutesTextResponseBodyParagraphList] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.has_next = has_next
        self.next_token = next_token
        self.paragraph_list = paragraph_list
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.paragraph_list:
            for v1 in self.paragraph_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_next is not None:
            result['hasNext'] = self.has_next

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['paragraphList'] = []
        if self.paragraph_list is not None:
            for k1 in self.paragraph_list:
                result['paragraphList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasNext') is not None:
            self.has_next = m.get('hasNext')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.paragraph_list = []
        if m.get('paragraphList') is not None:
            for k1 in m.get('paragraphList'):
                temp_model = main_models.MeetingFlashMinutesTextResponseBodyParagraphList()
                self.paragraph_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class MeetingFlashMinutesTextResponseBodyParagraphList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        nick_name: str = None,
        paragraph: str = None,
        sentence_list: List[main_models.MeetingFlashMinutesTextResponseBodyParagraphListSentenceList] = None,
        speaker_display: main_models.MeetingFlashMinutesTextResponseBodyParagraphListSpeakerDisplay = None,
        start_time: int = None,
        user_id: str = None,
    ):
        self.end_time = end_time
        self.nick_name = nick_name
        self.paragraph = paragraph
        self.sentence_list = sentence_list
        self.speaker_display = speaker_display
        self.start_time = start_time
        self.user_id = user_id

    def validate(self):
        if self.sentence_list:
            for v1 in self.sentence_list:
                 if v1:
                    v1.validate()
        if self.speaker_display:
            self.speaker_display.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.paragraph is not None:
            result['paragraph'] = self.paragraph

        result['sentenceList'] = []
        if self.sentence_list is not None:
            for k1 in self.sentence_list:
                result['sentenceList'].append(k1.to_map() if k1 else None)

        if self.speaker_display is not None:
            result['speakerDisplay'] = self.speaker_display.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('paragraph') is not None:
            self.paragraph = m.get('paragraph')

        self.sentence_list = []
        if m.get('sentenceList') is not None:
            for k1 in m.get('sentenceList'):
                temp_model = main_models.MeetingFlashMinutesTextResponseBodyParagraphListSentenceList()
                self.sentence_list.append(temp_model.from_map(k1))

        if m.get('speakerDisplay') is not None:
            temp_model = main_models.MeetingFlashMinutesTextResponseBodyParagraphListSpeakerDisplay()
            self.speaker_display = temp_model.from_map(m.get('speakerDisplay'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class MeetingFlashMinutesTextResponseBodyParagraphListSpeakerDisplay(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        nick_name: str = None,
    ):
        self.avatar_url = avatar_url
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url

        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')

        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        return self

class MeetingFlashMinutesTextResponseBodyParagraphListSentenceList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        sentence: str = None,
        start_time: int = None,
        word_list: List[main_models.MeetingFlashMinutesTextResponseBodyParagraphListSentenceListWordList] = None,
    ):
        self.end_time = end_time
        self.sentence = sentence
        self.start_time = start_time
        self.word_list = word_list

    def validate(self):
        if self.word_list:
            for v1 in self.word_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.sentence is not None:
            result['sentence'] = self.sentence

        if self.start_time is not None:
            result['startTime'] = self.start_time

        result['wordList'] = []
        if self.word_list is not None:
            for k1 in self.word_list:
                result['wordList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('sentence') is not None:
            self.sentence = m.get('sentence')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        self.word_list = []
        if m.get('wordList') is not None:
            for k1 in m.get('wordList'):
                temp_model = main_models.MeetingFlashMinutesTextResponseBodyParagraphListSentenceListWordList()
                self.word_list.append(temp_model.from_map(k1))

        return self

class MeetingFlashMinutesTextResponseBodyParagraphListSentenceListWordList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        word: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.word is not None:
            result['word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('word') is not None:
            self.word = m.get('word')

        return self

