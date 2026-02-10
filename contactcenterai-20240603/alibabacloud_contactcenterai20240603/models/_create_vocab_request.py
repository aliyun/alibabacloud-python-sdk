# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class CreateVocabRequest(DaraModel):
    def __init__(
        self,
        audio_model_code: str = None,
        description: str = None,
        name: str = None,
        word_weight_list: List[main_models.CreateVocabRequestWordWeightList] = None,
        workspace_id: str = None,
    ):
        self.audio_model_code = audio_model_code
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.word_weight_list = word_weight_list
        # This parameter is required.
        self.workspace_id = workspace_id

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

        result['wordWeightList'] = []
        if self.word_weight_list is not None:
            for k1 in self.word_weight_list:
                result['wordWeightList'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioModelCode') is not None:
            self.audio_model_code = m.get('audioModelCode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.word_weight_list = []
        if m.get('wordWeightList') is not None:
            for k1 in m.get('wordWeightList'):
                temp_model = main_models.CreateVocabRequestWordWeightList()
                self.word_weight_list.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateVocabRequestWordWeightList(DaraModel):
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

