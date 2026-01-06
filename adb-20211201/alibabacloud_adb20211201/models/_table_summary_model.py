# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class TableSummaryModel(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        created_by_source: str = None,
        created_by_user: str = None,
        description: str = None,
        mv_detail_model: main_models.OpenStructMvDetailModel = None,
        owner: str = None,
        sql: str = None,
        schema_name: str = None,
        table_name: str = None,
        table_size: int = None,
        table_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.created_by_source = created_by_source
        self.created_by_user = created_by_user
        self.description = description
        self.mv_detail_model = mv_detail_model
        self.owner = owner
        self.sql = sql
        self.schema_name = schema_name
        self.table_name = table_name
        self.table_size = table_size
        self.table_type = table_type
        self.update_time = update_time

    def validate(self):
        if self.mv_detail_model:
            self.mv_detail_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by_source is not None:
            result['CreatedBySource'] = self.created_by_source

        if self.created_by_user is not None:
            result['CreatedByUser'] = self.created_by_user

        if self.description is not None:
            result['Description'] = self.description

        if self.mv_detail_model is not None:
            result['MvDetailModel'] = self.mv_detail_model.to_map()

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_size is not None:
            result['TableSize'] = self.table_size

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBySource') is not None:
            self.created_by_source = m.get('CreatedBySource')

        if m.get('CreatedByUser') is not None:
            self.created_by_user = m.get('CreatedByUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MvDetailModel') is not None:
            temp_model = main_models.OpenStructMvDetailModel()
            self.mv_detail_model = temp_model.from_map(m.get('MvDetailModel'))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

