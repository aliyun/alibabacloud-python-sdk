# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribePresetsResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        presets: List[main_models.DescribePresetsResponseBodyPresets] = None,
        request_id: str = None,
    ):
        self.id = id
        self.presets = presets
        self.request_id = request_id

    def validate(self):
        if self.presets:
            for v1 in self.presets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['Presets'] = []
        if self.presets is not None:
            for k1 in self.presets:
                result['Presets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.presets = []
        if m.get('Presets') is not None:
            for k1 in m.get('Presets'):
                temp_model = main_models.DescribePresetsResponseBodyPresets()
                self.presets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePresetsResponseBodyPresets(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

