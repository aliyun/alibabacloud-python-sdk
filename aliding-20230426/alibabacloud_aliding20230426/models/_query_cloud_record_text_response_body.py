# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryCloudRecordTextResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        paragraph_list: List[main_models.QueryCloudRecordTextResponseBodyParagraphList] = None,
        request_id: str = None,
    ):
        self.has_more = has_more
        self.paragraph_list = paragraph_list
        # requestId
        self.request_id = request_id

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
        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['paragraphList'] = []
        if self.paragraph_list is not None:
            for k1 in self.paragraph_list:
                result['paragraphList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.paragraph_list = []
        if m.get('paragraphList') is not None:
            for k1 in m.get('paragraphList'):
                temp_model = main_models.QueryCloudRecordTextResponseBodyParagraphList()
                self.paragraph_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryCloudRecordTextResponseBodyParagraphList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        next_ttoken: int = None,
        nick_name: str = None,
        paragraph: str = None,
        record_id: int = None,
        sentence_list: List[main_models.QueryCloudRecordTextResponseBodyParagraphListSentenceList] = None,
        start_time: int = None,
        status: int = None,
        user_id: str = None,
    ):
        self.end_time = end_time
        self.next_ttoken = next_ttoken
        self.nick_name = nick_name
        self.paragraph = paragraph
        self.record_id = record_id
        self.sentence_list = sentence_list
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        if self.sentence_list:
            for v1 in self.sentence_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_ttoken is not None:
            result['NextTtoken'] = self.next_ttoken

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.paragraph is not None:
            result['Paragraph'] = self.paragraph

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        result['SentenceList'] = []
        if self.sentence_list is not None:
            for k1 in self.sentence_list:
                result['SentenceList'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextTtoken') is not None:
            self.next_ttoken = m.get('NextTtoken')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Paragraph') is not None:
            self.paragraph = m.get('Paragraph')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        self.sentence_list = []
        if m.get('SentenceList') is not None:
            for k1 in m.get('SentenceList'):
                temp_model = main_models.QueryCloudRecordTextResponseBodyParagraphListSentenceList()
                self.sentence_list.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryCloudRecordTextResponseBodyParagraphListSentenceList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        sentence: str = None,
        start_time: int = None,
        user_id: str = None,
        word_list: List[main_models.QueryCloudRecordTextResponseBodyParagraphListSentenceListWordList] = None,
    ):
        self.end_time = end_time
        self.sentence = sentence
        self.start_time = start_time
        self.user_id = user_id
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
            result['EndTime'] = self.end_time

        if self.sentence is not None:
            result['Sentence'] = self.sentence

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        result['WordList'] = []
        if self.word_list is not None:
            for k1 in self.word_list:
                result['WordList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Sentence') is not None:
            self.sentence = m.get('Sentence')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        self.word_list = []
        if m.get('WordList') is not None:
            for k1 in m.get('WordList'):
                temp_model = main_models.QueryCloudRecordTextResponseBodyParagraphListSentenceListWordList()
                self.word_list.append(temp_model.from_map(k1))

        return self

class QueryCloudRecordTextResponseBodyParagraphListSentenceListWordList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        word: str = None,
        word_id: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.word = word
        self.word_id = word_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.word is not None:
            result['Word'] = self.word

        if self.word_id is not None:
            result['WordId'] = self.word_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        if m.get('WordId') is not None:
            self.word_id = m.get('WordId')

        return self

