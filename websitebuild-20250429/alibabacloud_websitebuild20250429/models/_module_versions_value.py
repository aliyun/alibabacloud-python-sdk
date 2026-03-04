# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ModuleVersionsValue(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        components: Dict[str, main_models.ModuleVersionsValueComponentsValue] = None,
    ):
        # code
        self.code = code
        # name
        self.name = name
        # components
        self.components = components

    def validate(self):
        if self.components:
            for v1 in self.components.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        result['Components'] = {}
        if self.components is not None:
            for k1, v1 in self.components.items():
                result['Components'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.components = {}
        if m.get('Components') is not None:
            for k1, v1 in m.get('Components').items():
                temp_model = main_models.ModuleVersionsValueComponentsValue()
                self.components[k1] = temp_model.from_map(v1)

        return self

