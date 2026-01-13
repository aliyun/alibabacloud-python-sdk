# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateTableMetaRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        fields: List[main_models.UpdateTableMetaRequestFields] = None,
        instance_id: str = None,
        module: str = None,
        name: str = None,
        resource_id: str = None,
        table_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.fields = fields
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.module = module
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
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
        if self.description is not None:
            result['Description'] = self.description

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module is not None:
            result['Module'] = self.module

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.UpdateTableMetaRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class UpdateTableMetaRequestFields(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        is_dimension_field: bool = None,
        is_partition_field: str = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.data_type = data_type
        # This parameter is required.
        self.is_dimension_field = is_dimension_field
        # This parameter is required.
        self.is_partition_field = is_partition_field
        # This parameter is required.
        self.meaning = meaning
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

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
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

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

