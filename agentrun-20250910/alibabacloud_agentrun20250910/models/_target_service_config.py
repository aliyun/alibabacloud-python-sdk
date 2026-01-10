# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TargetServiceConfig(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
        model_name_pattern: str = None,
        weight: int = None,
    ):
        self.model_id = model_id
        self.model_name = model_name
        self.model_name_pattern = model_name_pattern
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_name_pattern is not None:
            result['modelNamePattern'] = self.model_name_pattern

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelNamePattern') is not None:
            self.model_name_pattern = m.get('modelNamePattern')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

