# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class CreateCloudNotePhrasesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        phrase: main_models.CreateCloudNotePhrasesRequestPhrase = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.phrase = phrase

    def validate(self):
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Phrase') is not None:
            temp_model = main_models.CreateCloudNotePhrasesRequestPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class CreateCloudNotePhrasesRequestPhrase(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        word_weights: List[main_models.CreateCloudNotePhrasesRequestPhraseWordWeights] = None,
    ):
        self.description = description
        # This parameter is required.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        result['WordWeights'] = []
        if self.word_weights is not None:
            for k1 in self.word_weights:
                result['WordWeights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.word_weights = []
        if m.get('WordWeights') is not None:
            for k1 in m.get('WordWeights'):
                temp_model = main_models.CreateCloudNotePhrasesRequestPhraseWordWeights()
                self.word_weights.append(temp_model.from_map(k1))

        return self

class CreateCloudNotePhrasesRequestPhraseWordWeights(DaraModel):
    def __init__(
        self,
        weight: int = None,
        word: str = None,
    ):
        # This parameter is required.
        self.weight = weight
        # This parameter is required.
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

