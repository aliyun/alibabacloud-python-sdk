# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class Hotword(DaraModel):
    def __init__(
        self,
        language: str = None,
        text: str = None,
        transposition_result_list: List[main_models.TranspositionResult] = None,
        weight: int = None,
    ):
        self.language = language
        self.text = text
        self.transposition_result_list = transposition_result_list
        self.weight = weight

    def validate(self):
        if self.transposition_result_list:
            for v1 in self.transposition_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.text is not None:
            result['Text'] = self.text

        result['TranspositionResultList'] = []
        if self.transposition_result_list is not None:
            for k1 in self.transposition_result_list:
                result['TranspositionResultList'].append(k1.to_map() if k1 else None)

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        self.transposition_result_list = []
        if m.get('TranspositionResultList') is not None:
            for k1 in m.get('TranspositionResultList'):
                temp_model = main_models.TranspositionResult()
                self.transposition_result_list.append(temp_model.from_map(k1))

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

