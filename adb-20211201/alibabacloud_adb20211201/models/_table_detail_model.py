# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class TableDetailModel(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        columns: List[main_models.ColDetailModel] = None,
        create_time: str = None,
        created_by_source: str = None,
        created_by_user: str = None,
        description: str = None,
        location: str = None,
        owner: str = None,
        parameters: Dict[str, str] = None,
        schema_name: str = None,
        table_name: str = None,
        table_type: str = None,
        update_time: str = None,
    ):
        self.catalog = catalog
        self.columns = columns
        self.create_time = create_time
        self.created_by_source = created_by_source
        self.created_by_user = created_by_user
        self.description = description
        self.location = location
        self.owner = owner
        self.parameters = parameters
        self.schema_name = schema_name
        self.table_name = table_name
        self.table_type = table_type
        self.update_time = update_time

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by_source is not None:
            result['CreatedBySource'] = self.created_by_source

        if self.created_by_user is not None:
            result['CreatedByUser'] = self.created_by_user

        if self.description is not None:
            result['Description'] = self.description

        if self.location is not None:
            result['Location'] = self.location

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.ColDetailModel()
                self.columns.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBySource') is not None:
            self.created_by_source = m.get('CreatedBySource')

        if m.get('CreatedByUser') is not None:
            self.created_by_user = m.get('CreatedByUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

