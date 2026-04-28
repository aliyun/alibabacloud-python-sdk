# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Aggregation(DaraModel):
    def __init__(
        self,
        field: bytes = None,
        groups: List[main_models.AggregationsGroup] = None,
        operation: bytes = None,
        value: float = None,
    ):
        self.field = field
        self.groups = groups
        self.operation = operation
        self.value = value

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.operation is not None:
            result['operation'] = self.operation

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.AggregationsGroup()
                self.groups.append(temp_model.from_map(k1))

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

