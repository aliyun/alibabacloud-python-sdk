# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class EventFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        op: str = None,
        sub_filters: List[main_models.EventFilter] = None,
        values: List[str] = None,
    ):
        # key
        self.key = key
        # op
        # 
        # This parameter is required.
        self.op = op
        # filters
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

        if self.op is not None:
            result['Op'] = self.op

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

        if m.get('Op') is not None:
            self.op = m.get('Op')

        self.sub_filters = []
        if m.get('SubFilters') is not None:
            for k1 in m.get('SubFilters'):
                temp_model = main_models.EventFilter()
                self.sub_filters.append(temp_model.from_map(k1))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

