# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeExcessivePrimaryKeysResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeExcessivePrimaryKeysResponseBodyDetectionItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tables: List[main_models.DescribeExcessivePrimaryKeysResponseBodyTables] = None,
        total_count: str = None,
    ):
        # The queried information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried tables that have excessive primary key fields.
        self.tables = tables
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeExcessivePrimaryKeysResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.DescribeExcessivePrimaryKeysResponseBodyTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExcessivePrimaryKeysResponseBodyTables(DaraModel):
    def __init__(
        self,
        column_count: int = None,
        primary_key_columns: str = None,
        primary_key_count: int = None,
        primary_key_index_size: int = None,
        schema_name: str = None,
        space_ratio: float = None,
        table_name: str = None,
        total_size: int = None,
    ):
        # The total number of columns.
        self.column_count = column_count
        # The queried primary key fields.
        self.primary_key_columns = primary_key_columns
        # The number of primary key fields.
        self.primary_key_count = primary_key_count
        # The data size of primary key indexes. Unit: bytes.
        self.primary_key_index_size = primary_key_index_size
        # The name of the database.
        self.schema_name = schema_name
        # The percentage of the table size. Unit: %.
        # 
        # >  Formula: Table storage percentage = Total data size of a table/Total data size of the cluster × 100%.
        self.space_ratio = space_ratio
        # The name of the table
        self.table_name = table_name
        # The cold data size. Unit: bytes.
        # 
        # >  Formula: Cold data size = Data size of table records + Data size of regular indexes + Data size of primary key indexes + Data size of other data.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count

        if self.primary_key_columns is not None:
            result['PrimaryKeyColumns'] = self.primary_key_columns

        if self.primary_key_count is not None:
            result['PrimaryKeyCount'] = self.primary_key_count

        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size

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
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')

        if m.get('PrimaryKeyColumns') is not None:
            self.primary_key_columns = m.get('PrimaryKeyColumns')

        if m.get('PrimaryKeyCount') is not None:
            self.primary_key_count = m.get('PrimaryKeyCount')

        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SpaceRatio') is not None:
            self.space_ratio = m.get('SpaceRatio')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeExcessivePrimaryKeysResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        status: str = None,
    ):
        # The detection result.
        self.message = message
        # The name of the detection item.
        self.name = name
        # The severity level of the detection result.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

