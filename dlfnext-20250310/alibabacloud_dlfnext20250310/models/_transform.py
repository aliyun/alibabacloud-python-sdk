# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Transform(DaraModel):
    def __init__(
        self,
        cast_type: main_models.FullDataType = None,
        field_ref: main_models.FieldRef = None,
        inputs: List[main_models.TransformInput] = None,
        name: str = None,
    ):
        self.cast_type = cast_type
        self.field_ref = field_ref
        self.inputs = inputs
        self.name = name

    def validate(self):
        if self.cast_type:
            self.cast_type.validate()
        if self.field_ref:
            self.field_ref.validate()
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cast_type is not None:
            result['castType'] = self.cast_type.to_map()

        if self.field_ref is not None:
            result['fieldRef'] = self.field_ref.to_map()

        result['inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['inputs'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('castType') is not None:
            temp_model = main_models.FullDataType()
            self.cast_type = temp_model.from_map(m.get('castType'))

        if m.get('fieldRef') is not None:
            temp_model = main_models.FieldRef()
            self.field_ref = temp_model.from_map(m.get('fieldRef'))

        self.inputs = []
        if m.get('inputs') is not None:
            for k1 in m.get('inputs'):
                temp_model = main_models.TransformInput()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

