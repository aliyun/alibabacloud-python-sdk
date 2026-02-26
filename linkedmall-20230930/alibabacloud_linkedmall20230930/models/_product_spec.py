# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class ProductSpec(DaraModel):
    def __init__(
        self,
        key: str = None,
        key_id: int = None,
        values: List[main_models.ProductSpecValue] = None,
    ):
        self.key = key
        self.key_id = key_id
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
        if self.key is not None:
            result['key'] = self.key

        if self.key_id is not None:
            result['keyId'] = self.key_id

        result['values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        self.values = []
        if m.get('values') is not None:
            for k1 in m.get('values'):
                temp_model = main_models.ProductSpecValue()
                self.values.append(temp_model.from_map(k1))

        return self

