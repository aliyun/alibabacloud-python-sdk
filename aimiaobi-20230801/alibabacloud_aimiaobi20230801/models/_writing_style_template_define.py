# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class WritingStyleTemplateDefine(DaraModel):
    def __init__(
        self,
        example: List[main_models.WritingStyleTemplateDefineExample] = None,
        fields: List[main_models.WritingStyleTemplateField] = None,
    ):
        self.example = example
        self.fields = fields

    def validate(self):
        if self.example:
            for v1 in self.example:
                 if v1:
                    v1.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Example'] = []
        if self.example is not None:
            for k1 in self.example:
                result['Example'].append(k1.to_map() if k1 else None)

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.example = []
        if m.get('Example') is not None:
            for k1 in m.get('Example'):
                temp_model = main_models.WritingStyleTemplateDefineExample()
                self.example.append(temp_model.from_map(k1))

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.WritingStyleTemplateField()
                self.fields.append(temp_model.from_map(k1))

        return self

class WritingStyleTemplateDefineExample(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

