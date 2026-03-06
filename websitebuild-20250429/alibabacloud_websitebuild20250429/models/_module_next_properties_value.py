# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ModuleNextPropertiesValue(DaraModel):
    def __init__(
        self,
        code: str = None,
        values: List[main_models.ModuleNextPropertiesValueValues] = None,
    ):
        self.code = code
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.ModuleNextPropertiesValueValues()
                self.values.append(temp_model.from_map(k1))

        return self

class ModuleNextPropertiesValueValues(DaraModel):
    def __init__(
        self,
        value: str = None,
    ):
        # placeholder
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

