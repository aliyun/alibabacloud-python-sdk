# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceIndexUsageResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceIndexUsageResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried index usage.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceIndexUsageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceIndexUsageResponseBodyItems(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        index_def: str = None,
        index_name: str = None,
        index_scan_times: int = None,
        index_size: str = None,
        is_partition_table: bool = None,
        parent_table_name: str = None,
        schema_name: str = None,
        table_name: str = None,
        time_last_updated: str = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The definition of the index.
        self.index_def = index_def
        # The name of the index.
        self.index_name = index_name
        # The number of index scans.
        self.index_scan_times = index_scan_times
        # The size of the index. Unit: bytes.
        self.index_size = index_size
        # Indicates whether the table is a partitioned table. Valid values:
        # 
        # *   **true**: The table is a partitioned table.
        # *   **false**: The table is not a partitioned table.
        self.is_partition_table = is_partition_table
        # The name of the parent table.
        self.parent_table_name = parent_table_name
        # The name of the schema.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.index_def is not None:
            result['IndexDef'] = self.index_def

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.index_scan_times is not None:
            result['IndexScanTimes'] = self.index_scan_times

        if self.index_size is not None:
            result['IndexSize'] = self.index_size

        if self.is_partition_table is not None:
            result['IsPartitionTable'] = self.is_partition_table

        if self.parent_table_name is not None:
            result['ParentTableName'] = self.parent_table_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('IndexDef') is not None:
            self.index_def = m.get('IndexDef')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('IndexScanTimes') is not None:
            self.index_scan_times = m.get('IndexScanTimes')

        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')

        if m.get('IsPartitionTable') is not None:
            self.is_partition_table = m.get('IsPartitionTable')

        if m.get('ParentTableName') is not None:
            self.parent_table_name = m.get('ParentTableName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')

        return self

