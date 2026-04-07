# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTablesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListTablesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        table_entity_list: List[main_models.ListTablesResponseBodyDataTableEntityList] = None,
        total: int = None,
    ):
        # Pagination information, which specifies the starting point of the next read.
        self.next_token = next_token
        # An array of entities.
        self.table_entity_list = table_entity_list
        # The total number.
        self.total = total

    def validate(self):
        if self.table_entity_list:
            for v1 in self.table_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['TableEntityList'] = []
        if self.table_entity_list is not None:
            for k1 in self.table_entity_list:
                result['TableEntityList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.table_entity_list = []
        if m.get('TableEntityList') is not None:
            for k1 in m.get('TableEntityList'):
                temp_model = main_models.ListTablesResponseBodyDataTableEntityList()
                self.table_entity_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTablesResponseBodyDataTableEntityList(DaraModel):
    def __init__(
        self,
        entity_content: main_models.ListTablesResponseBodyDataTableEntityListEntityContent = None,
        entity_qualified_name: str = None,
    ):
        # The information about the table.
        self.entity_content = entity_content
        # The unique identifier of the table entity.
        self.entity_qualified_name = entity_qualified_name

    def validate(self):
        if self.entity_content:
            self.entity_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_content is not None:
            result['EntityContent'] = self.entity_content.to_map()

        if self.entity_qualified_name is not None:
            result['EntityQualifiedName'] = self.entity_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityContent') is not None:
            temp_model = main_models.ListTablesResponseBodyDataTableEntityListEntityContent()
            self.entity_content = temp_model.from_map(m.get('EntityContent'))

        if m.get('EntityQualifiedName') is not None:
            self.entity_qualified_name = m.get('EntityQualifiedName')

        return self

class ListTablesResponseBodyDataTableEntityListEntityContent(DaraModel):
    def __init__(
        self,
        data_source_qualified_name: str = None,
        data_source_unique_id: str = None,
        database_name: str = None,
        instance_id: str = None,
        project_name: str = None,
        table_name: str = None,
    ):
        # The unique identifier of the data source.
        self.data_source_qualified_name = data_source_qualified_name
        # The unique ID of the data source identifier.
        self.data_source_unique_id = data_source_unique_id
        # The name of the database.
        self.database_name = database_name
        # The ID of the data source instance.
        self.instance_id = instance_id
        # The name of the ODPS project.
        self.project_name = project_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_qualified_name is not None:
            result['DataSourceQualifiedName'] = self.data_source_qualified_name

        if self.data_source_unique_id is not None:
            result['DataSourceUniqueId'] = self.data_source_unique_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceQualifiedName') is not None:
            self.data_source_qualified_name = m.get('DataSourceQualifiedName')

        if m.get('DataSourceUniqueId') is not None:
            self.data_source_unique_id = m.get('DataSourceUniqueId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

