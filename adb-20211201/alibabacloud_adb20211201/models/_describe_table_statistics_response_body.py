# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeTableStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: main_models.DescribeTableStatisticsResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        schema_names: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried table statistics.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The names of databases.
        self.schema_names = schema_names
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_names is not None:
            result['SchemaNames'] = self.schema_names

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeTableStatisticsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaNames') is not None:
            self.schema_names = m.get('SchemaNames')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTableStatisticsResponseBodyItems(DaraModel):
    def __init__(
        self,
        table_statistic_records: List[main_models.DescribeTableStatisticsResponseBodyItemsTableStatisticRecords] = None,
    ):
        self.table_statistic_records = table_statistic_records

    def validate(self):
        if self.table_statistic_records:
            for v1 in self.table_statistic_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TableStatisticRecords'] = []
        if self.table_statistic_records is not None:
            for k1 in self.table_statistic_records:
                result['TableStatisticRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table_statistic_records = []
        if m.get('TableStatisticRecords') is not None:
            for k1 in m.get('TableStatisticRecords'):
                temp_model = main_models.DescribeTableStatisticsResponseBodyItemsTableStatisticRecords()
                self.table_statistic_records.append(temp_model.from_map(k1))

        return self

class DescribeTableStatisticsResponseBodyItemsTableStatisticRecords(DaraModel):
    def __init__(
        self,
        cold_data_size: int = None,
        data_size: int = None,
        hot_data_size: int = None,
        index_size: int = None,
        other_size: int = None,
        partition_count: int = None,
        primary_key_index_size: int = None,
        row_count: int = None,
        schema_name: str = None,
        space_ratio: float = None,
        table_name: str = None,
        total_size: int = None,
    ):
        # The size of cold data. Unit: bytes.
        # 
        # >  This parameter is supported only for AnalyticDB for MySQL clusters of V3.1.3.4 or later.
        self.cold_data_size = cold_data_size
        # The data size of the table. Unit: bytes.
        self.data_size = data_size
        # The size of hot data. Unit: bytes.
        self.hot_data_size = hot_data_size
        # The data size of indexes. Unit: bytes.
        self.index_size = index_size
        # The data size of other data. Unit: bytes.
        self.other_size = other_size
        # The number of partitions.
        self.partition_count = partition_count
        # The data size of the primary key index. Unit: bytes.
        self.primary_key_index_size = primary_key_index_size
        # The number of rows in the table.
        self.row_count = row_count
        # The name of the database.
        self.schema_name = schema_name
        # The percentage of the table size. Unit: %.
        # 
        # >  Formula: Table storage percentage = Total data size of a table/Total data size of the cluster × 100%.
        self.space_ratio = space_ratio
        # The name of the table.
        self.table_name = table_name
        # The total data size of the table. Unit: bytes.
        # 
        # >  The following formulas can be used to calculate the total data size:
        # 
        # *   Formula 1: Total data size = Hot data size + Cold data size.
        # *   Formula 2: Total data size = Data size of table records + Data size of regular indexes + Data size of primary key indexes + Data size of other data.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.hot_data_size is not None:
            result['HotDataSize'] = self.hot_data_size

        if self.index_size is not None:
            result['IndexSize'] = self.index_size

        if self.other_size is not None:
            result['OtherSize'] = self.other_size

        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count

        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.space_ratio is not None:
            result['SpaceRatio'] = self.space_ratio

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdDataSize') is not None:
            self.cold_data_size = m.get('ColdDataSize')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('HotDataSize') is not None:
            self.hot_data_size = m.get('HotDataSize')

        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')

        if m.get('OtherSize') is not None:
            self.other_size = m.get('OtherSize')

        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')

        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SpaceRatio') is not None:
            self.space_ratio = m.get('SpaceRatio')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

