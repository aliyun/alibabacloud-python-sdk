# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Schema(DaraModel):
    def __init__(
        self,
        comment: str = None,
        fields: List[main_models.DataField] = None,
        options: Dict[str, str] = None,
        partition_keys: List[str] = None,
        primary_keys: List[str] = None,
    ):
        self.comment = comment
        self.fields = fields
        self.options = options
        self.partition_keys = partition_keys
        self.primary_keys = primary_keys

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.options is not None:
            result['options'] = self.options

        if self.partition_keys is not None:
            result['partitionKeys'] = self.partition_keys

        if self.primary_keys is not None:
            result['primaryKeys'] = self.primary_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.DataField()
                self.fields.append(temp_model.from_map(k1))

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('partitionKeys') is not None:
            self.partition_keys = m.get('partitionKeys')

        if m.get('primaryKeys') is not None:
            self.primary_keys = m.get('primaryKeys')

        return self

