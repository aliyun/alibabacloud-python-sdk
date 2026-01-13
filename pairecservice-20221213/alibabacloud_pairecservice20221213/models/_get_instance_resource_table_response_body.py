# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResourceTableResponseBody(DaraModel):
    def __init__(
        self,
        fields: List[main_models.GetInstanceResourceTableResponseBodyFields] = None,
        request_id: str = None,
        table_name: str = None,
    ):
        self.fields = fields
        self.request_id = request_id
        self.table_name = table_name

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
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetInstanceResourceTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetInstanceResourceTableResponseBodyFields(DaraModel):
    def __init__(
        self,
        is_dimension_field: bool = None,
        is_partition_field: bool = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.is_dimension_field = is_dimension_field
        self.is_partition_field = is_partition_field
        self.meaning = meaning
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_dimension_field is not None:
            result['IsDimensionField'] = self.is_dimension_field

        if self.is_partition_field is not None:
            result['IsPartitionField'] = self.is_partition_field

        if self.meaning is not None:
            result['Meaning'] = self.meaning

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDimensionField') is not None:
            self.is_dimension_field = m.get('IsDimensionField')

        if m.get('IsPartitionField') is not None:
            self.is_partition_field = m.get('IsPartitionField')

        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

