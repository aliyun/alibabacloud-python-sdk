# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyCloudNotePhrasesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        phrase: main_models.ModifyCloudNotePhrasesRequestPhrase = None,
    ):
        # The application ID. You can create and query it in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The hotword parameter.
        # 
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
            temp_model = main_models.ModifyCloudNotePhrasesRequestPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class ModifyCloudNotePhrasesRequestPhrase(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        word_weights: List[main_models.ModifyCloudNotePhrasesRequestPhraseWordWeights] = None,
    ):
        # The description. The description must be encoded in UTF-8 and be 1 to 200 characters in length.
        self.description = description
        # The ID of the hotword table.
        # 
        # This parameter is required.
        self.id = id
        # The name of the hotword table. The name must be encoded in UTF-8 and be 1 to 30 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # Each vocabulary can contain up to 300 hotwords. Each hotword can be up to 10 Chinese characters or 5 English words in length.
        # 
        # Hotwords must be encoded in UTF-8 and cannot contain punctuation marks or special characters. Otherwise, the hotwords do not take effect.
        # 
        # The weight of a hotword must be an integer in the range of [-6, 5].
        # 
        # Numbers in the text must be replaced with the corresponding Chinese characters based on their pronunciation. For example, \"59.9元\" must be replaced with \"五十九点九元\".
        # 
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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.word_weights = []
        if m.get('WordWeights') is not None:
            for k1 in m.get('WordWeights'):
                temp_model = main_models.ModifyCloudNotePhrasesRequestPhraseWordWeights()
                self.word_weights.append(temp_model.from_map(k1))

        return self

class ModifyCloudNotePhrasesRequestPhraseWordWeights(DaraModel):
    def __init__(
        self,
        weight: int = None,
        word: str = None,
    ):
        # The weight. The value must be an integer in the range of [-6, 5].
        # - A value greater than 0 increases the probability of recognizing the word, and a value less than 0 decreases the probability.
        # - A value of -6 indicates that the word should not be recognized if possible.
        # - A value of 2 is a common value.
        # If the effect is not obvious, you can increase the weight. However, a large weight may cause negative effects and lead to inaccurate recognition of other words.
        # 
        # This parameter is required.
        self.weight = weight
        # The hotword.
        # 
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

