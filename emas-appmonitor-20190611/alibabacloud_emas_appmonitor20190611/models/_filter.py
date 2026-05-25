# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class Filter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List[main_models.Filter] = None,
        values: Any = None,
    ):
        # key
        self.key = key
        # operator
        self.operator = operator
        # subFillter
        self.sub_filters = sub_filters
        # values
        self.values = values

    def validate(self):
        if self.sub_filters:
            for v1 in self.sub_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        result['SubFilters'] = []
        if self.sub_filters is not None:
            for k1 in self.sub_filters:
                result['SubFilters'].append(k1.to_map() if k1 else None)

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        self.sub_filters = []
        if m.get('SubFilters') is not None:
            for k1 in m.get('SubFilters'):
                temp_model = main_models.Filter()
                self.sub_filters.append(temp_model.from_map(k1))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

