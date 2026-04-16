# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRowDTO(DaraModel):
    def __init__(
        self,
        model_code: str = None,
        model_id: int = None,
        model_name: str = None,
        values: str = None,
    ):
        self.model_code = model_code
        self.model_id = model_id
        self.model_name = model_name
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

