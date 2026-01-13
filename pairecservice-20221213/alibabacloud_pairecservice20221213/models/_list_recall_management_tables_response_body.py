# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListRecallManagementTablesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        recall_management_tables: List[main_models.ListRecallManagementTablesResponseBodyRecallManagementTables] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.recall_management_tables = recall_management_tables
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.recall_management_tables:
            for v1 in self.recall_management_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['RecallManagementTables'] = []
        if self.recall_management_tables is not None:
            for k1 in self.recall_management_tables:
                result['RecallManagementTables'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.recall_management_tables = []
        if m.get('RecallManagementTables') is not None:
            for k1 in m.get('RecallManagementTables'):
                temp_model = main_models.ListRecallManagementTablesResponseBodyRecallManagementTables()
                self.recall_management_tables.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecallManagementTablesResponseBodyRecallManagementTables(DaraModel):
    def __init__(
        self,
        can_delete: bool = None,
        data_source: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        index_effective_time: str = None,
        index_version_id: str = None,
        maxcompute_project_name: str = None,
        maxcompute_schema: str = None,
        maxcompute_table_name: str = None,
        name: str = None,
        partition_fields: str = None,
        recall_management_table_id: str = None,
        recall_type: str = None,
        type: str = None,
    ):
        self.can_delete = can_delete
        self.data_source = data_source
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.index_effective_time = index_effective_time
        self.index_version_id = index_version_id
        self.maxcompute_project_name = maxcompute_project_name
        # maxcompute schema。
        self.maxcompute_schema = maxcompute_schema
        self.maxcompute_table_name = maxcompute_table_name
        self.name = name
        self.partition_fields = partition_fields
        self.recall_management_table_id = recall_management_table_id
        self.recall_type = recall_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.index_effective_time is not None:
            result['IndexEffectiveTime'] = self.index_effective_time

        if self.index_version_id is not None:
            result['IndexVersionId'] = self.index_version_id

        if self.maxcompute_project_name is not None:
            result['MaxcomputeProjectName'] = self.maxcompute_project_name

        if self.maxcompute_schema is not None:
            result['MaxcomputeSchema'] = self.maxcompute_schema

        if self.maxcompute_table_name is not None:
            result['MaxcomputeTableName'] = self.maxcompute_table_name

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_fields is not None:
            result['PartitionFields'] = self.partition_fields

        if self.recall_management_table_id is not None:
            result['RecallManagementTableId'] = self.recall_management_table_id

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IndexEffectiveTime') is not None:
            self.index_effective_time = m.get('IndexEffectiveTime')

        if m.get('IndexVersionId') is not None:
            self.index_version_id = m.get('IndexVersionId')

        if m.get('MaxcomputeProjectName') is not None:
            self.maxcompute_project_name = m.get('MaxcomputeProjectName')

        if m.get('MaxcomputeSchema') is not None:
            self.maxcompute_schema = m.get('MaxcomputeSchema')

        if m.get('MaxcomputeTableName') is not None:
            self.maxcompute_table_name = m.get('MaxcomputeTableName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionFields') is not None:
            self.partition_fields = m.get('PartitionFields')

        if m.get('RecallManagementTableId') is not None:
            self.recall_management_table_id = m.get('RecallManagementTableId')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

