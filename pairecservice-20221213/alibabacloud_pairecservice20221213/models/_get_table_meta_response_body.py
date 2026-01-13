# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetTableMetaResponseBody(DaraModel):
    def __init__(
        self,
        can_delete: bool = None,
        config: str = None,
        description: str = None,
        fields: List[main_models.GetTableMetaResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_imported_time: str = None,
        gmt_modified_time: str = None,
        module: str = None,
        name: str = None,
        request_id: str = None,
        resource_id: str = None,
        table_meta_id: str = None,
        table_name: str = None,
        type: str = None,
        url: str = None,
    ):
        self.can_delete = can_delete
        self.config = config
        self.description = description
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_imported_time = gmt_imported_time
        self.gmt_modified_time = gmt_modified_time
        self.module = module
        self.name = name
        self.request_id = request_id
        self.resource_id = resource_id
        self.table_meta_id = table_meta_id
        self.table_name = table_name
        self.type = type
        self.url = url

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
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_imported_time is not None:
            result['GmtImportedTime'] = self.gmt_imported_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.module is not None:
            result['Module'] = self.module

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetTableMetaResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtImportedTime') is not None:
            self.gmt_imported_time = m.get('GmtImportedTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetTableMetaResponseBodyFields(DaraModel):
    def __init__(
        self,
        is_dimension_field: bool = None,
        meaning: str = None,
        name: str = None,
        type: str = None,
    ):
        self.is_dimension_field = is_dimension_field
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

        if m.get('Meaning') is not None:
            self.meaning = m.get('Meaning')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

