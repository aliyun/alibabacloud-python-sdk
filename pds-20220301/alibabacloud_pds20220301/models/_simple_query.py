# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class SimpleQuery(DaraModel):
    def __init__(
        self,
        field: bytes = None,
        operation: bytes = None,
        sub_queries: List[main_models.SimpleQuery] = None,
        value: bytes = None,
    ):
        self.field = field
        self.operation = operation
        self.sub_queries = sub_queries
        self.value = value

    def validate(self):
        if self.sub_queries:
            for v1 in self.sub_queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.operation is not None:
            result['operation'] = self.operation

        result['sub_queries'] = []
        if self.sub_queries is not None:
            for k1 in self.sub_queries:
                result['sub_queries'].append(k1.to_map() if k1 else None)

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        self.sub_queries = []
        if m.get('sub_queries') is not None:
            for k1 in m.get('sub_queries'):
                temp_model = main_models.SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k1))

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

