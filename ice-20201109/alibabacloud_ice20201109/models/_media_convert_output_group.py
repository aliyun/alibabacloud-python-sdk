# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertOutputGroup(DaraModel):
    def __init__(
        self,
        group_config: main_models.MediaConvertOutputGroupConfig = None,
        name: str = None,
        outputs: List[main_models.MediaConvertOutputGroupOutput] = None,
    ):
        self.group_config = group_config
        self.name = name
        self.outputs = outputs

    def validate(self):
        if self.group_config:
            self.group_config.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_config is not None:
            result['GroupConfig'] = self.group_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupConfig') is not None:
            temp_model = main_models.MediaConvertOutputGroupConfig()
            self.group_config = temp_model.from_map(m.get('GroupConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.MediaConvertOutputGroupOutput()
                self.outputs.append(temp_model.from_map(k1))

        return self

