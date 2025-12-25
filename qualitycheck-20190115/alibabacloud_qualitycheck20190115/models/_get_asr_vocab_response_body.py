# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetAsrVocabResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAsrVocabResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAsrVocabResponseBodyData(DaraModel):
    def __init__(
        self,
        asr_version: int = None,
        model_customization_id: str = None,
        name: str = None,
        words: main_models.GetAsrVocabResponseBodyDataWords = None,
    ):
        self.asr_version = asr_version
        self.model_customization_id = model_customization_id
        self.name = name
        self.words = words

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version

        if self.model_customization_id is not None:
            result['ModelCustomizationId'] = self.model_customization_id

        if self.name is not None:
            result['Name'] = self.name

        if self.words is not None:
            result['Words'] = self.words.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')

        if m.get('ModelCustomizationId') is not None:
            self.model_customization_id = m.get('ModelCustomizationId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Words') is not None:
            temp_model = main_models.GetAsrVocabResponseBodyDataWords()
            self.words = temp_model.from_map(m.get('Words'))

        return self

class GetAsrVocabResponseBodyDataWords(DaraModel):
    def __init__(
        self,
        word: List[main_models.GetAsrVocabResponseBodyDataWordsWord] = None,
    ):
        self.word = word

    def validate(self):
        if self.word:
            for v1 in self.word:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Word'] = []
        if self.word is not None:
            for k1 in self.word:
                result['Word'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.word = []
        if m.get('Word') is not None:
            for k1 in m.get('Word'):
                temp_model = main_models.GetAsrVocabResponseBodyDataWordsWord()
                self.word.append(temp_model.from_map(k1))

        return self

class GetAsrVocabResponseBodyDataWordsWord(DaraModel):
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

