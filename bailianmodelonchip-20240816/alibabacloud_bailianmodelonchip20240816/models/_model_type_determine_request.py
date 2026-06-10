# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianmodelonchip20240816 import models as main_models
from darabonba.model import DaraModel

class ModelTypeDetermineRequest(DaraModel):
    def __init__(
        self,
        history: List[main_models.ModelTypeDetermineRequestHistory] = None,
        input_text: str = None,
    ):
        self.history = history
        # This parameter is required.
        self.input_text = input_text

    def validate(self):
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['history'] = []
        if self.history is not None:
            for k1 in self.history:
                result['history'].append(k1.to_map() if k1 else None)

        if self.input_text is not None:
            result['inputText'] = self.input_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history = []
        if m.get('history') is not None:
            for k1 in m.get('history'):
                temp_model = main_models.ModelTypeDetermineRequestHistory()
                self.history.append(temp_model.from_map(k1))

        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')

        return self

class ModelTypeDetermineRequestHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

