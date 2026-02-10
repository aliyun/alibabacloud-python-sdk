# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class ListVocabResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVocabResponseBodyData] = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListVocabResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListVocabResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_model_code: str = None,
        description: str = None,
        name: str = None,
        vocabulary_id: str = None,
        word_weight_list: List[main_models.ListVocabResponseBodyDataWordWeightList] = None,
    ):
        self.audio_model_code = audio_model_code
        self.description = description
        self.name = name
        self.vocabulary_id = vocabulary_id
        self.word_weight_list = word_weight_list

    def validate(self):
        if self.word_weight_list:
            for v1 in self.word_weight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_model_code is not None:
            result['audioModelCode'] = self.audio_model_code

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.vocabulary_id is not None:
            result['vocabularyId'] = self.vocabulary_id

        result['wordWeightList'] = []
        if self.word_weight_list is not None:
            for k1 in self.word_weight_list:
                result['wordWeightList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioModelCode') is not None:
            self.audio_model_code = m.get('audioModelCode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('vocabularyId') is not None:
            self.vocabulary_id = m.get('vocabularyId')

        self.word_weight_list = []
        if m.get('wordWeightList') is not None:
            for k1 in m.get('wordWeightList'):
                temp_model = main_models.ListVocabResponseBodyDataWordWeightList()
                self.word_weight_list.append(temp_model.from_map(k1))

        return self

class ListVocabResponseBodyDataWordWeightList(DaraModel):
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
            result['weight'] = self.weight

        if self.word is not None:
            result['word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weight') is not None:
            self.weight = m.get('weight')

        if m.get('word') is not None:
            self.word = m.get('word')

        return self

