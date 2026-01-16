# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CreateLayerVersionInput(DaraModel):
    def __init__(
        self,
        code: main_models.InputCodeLocation = None,
        compatible_runtime: List[str] = None,
        description: str = None,
        license: str = None,
    ):
        self.code = code
        self.compatible_runtime = compatible_runtime
        self.description = description
        self.license = license

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code.to_map()

        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime

        if self.description is not None:
            result['description'] = self.description

        if self.license is not None:
            result['license'] = self.license

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = main_models.InputCodeLocation()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('license') is not None:
            self.license = m.get('license')

        return self

