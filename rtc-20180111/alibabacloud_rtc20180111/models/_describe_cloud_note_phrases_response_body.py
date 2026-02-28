# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudNotePhrasesResponseBody(DaraModel):
    def __init__(
        self,
        phrases: List[main_models.DescribeCloudNotePhrasesResponseBodyPhrases] = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.phrases = phrases
        # Id of the request。
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.phrases:
            for v1 in self.phrases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Phrases'] = []
        if self.phrases is not None:
            for k1 in self.phrases:
                result['Phrases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.phrases = []
        if m.get('Phrases') is not None:
            for k1 in m.get('Phrases'):
                temp_model = main_models.DescribeCloudNotePhrasesResponseBodyPhrases()
                self.phrases.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeCloudNotePhrasesResponseBodyPhrases(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        word_weights: List[main_models.DescribeCloudNotePhrasesResponseBodyPhrasesWordWeights] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.id = id
        self.name = name
        # This parameter is required.
        self.word_weights = word_weights

    def validate(self):
        if self.word_weights:
            for v1 in self.word_weights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['WordWeights'] = []
        if self.word_weights is not None:
            for k1 in self.word_weights:
                result['WordWeights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.word_weights = []
        if m.get('WordWeights') is not None:
            for k1 in m.get('WordWeights'):
                temp_model = main_models.DescribeCloudNotePhrasesResponseBodyPhrasesWordWeights()
                self.word_weights.append(temp_model.from_map(k1))

        return self

class DescribeCloudNotePhrasesResponseBodyPhrasesWordWeights(DaraModel):
    def __init__(
        self,
        weight: int = None,
        word: str = None,
    ):
        self.weight = weight
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.weight is not None:
            result['Weight'] = self.weight

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

