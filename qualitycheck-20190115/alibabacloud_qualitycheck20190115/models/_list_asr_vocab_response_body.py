# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListAsrVocabResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAsrVocabResponseBodyData = None,
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
            temp_model = main_models.ListAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAsrVocabResponseBodyData(DaraModel):
    def __init__(
        self,
        asr_vocab: List[main_models.ListAsrVocabResponseBodyDataAsrVocab] = None,
    ):
        self.asr_vocab = asr_vocab

    def validate(self):
        if self.asr_vocab:
            for v1 in self.asr_vocab:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsrVocab'] = []
        if self.asr_vocab is not None:
            for k1 in self.asr_vocab:
                result['AsrVocab'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_vocab = []
        if m.get('AsrVocab') is not None:
            for k1 in m.get('AsrVocab'):
                temp_model = main_models.ListAsrVocabResponseBodyDataAsrVocab()
                self.asr_vocab.append(temp_model.from_map(k1))

        return self

class ListAsrVocabResponseBodyDataAsrVocab(DaraModel):
    def __init__(
        self,
        asr_version: int = None,
        create_time: str = None,
        id: str = None,
        model_customization_id: str = None,
        name: str = None,
        update_time: str = None,
        vocabulary_id: str = None,
    ):
        self.asr_version = asr_version
        self.create_time = create_time
        self.id = id
        self.model_customization_id = model_customization_id
        self.name = name
        self.update_time = update_time
        self.vocabulary_id = vocabulary_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.model_customization_id is not None:
            result['ModelCustomizationId'] = self.model_customization_id

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModelCustomizationId') is not None:
            self.model_customization_id = m.get('ModelCustomizationId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        return self

