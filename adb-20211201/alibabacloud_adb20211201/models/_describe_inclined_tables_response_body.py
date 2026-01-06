# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeInclinedTablesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        detection_items: List[main_models.DescribeInclinedTablesResponseBodyDetectionItems] = None,
        items: main_models.DescribeInclinedTablesResponseBodyItems = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The queried tables.
        self.items = items
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The total number of pages.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeInclinedTablesResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('Items') is not None:
            temp_model = main_models.DescribeInclinedTablesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInclinedTablesResponseBodyItems(DaraModel):
    def __init__(
        self,
        table: List[main_models.DescribeInclinedTablesResponseBodyItemsTable] = None,
    ):
        # The queried table.
        self.table = table

    def validate(self):
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['Table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k1 in m.get('Table'):
                temp_model = main_models.DescribeInclinedTablesResponseBodyItemsTable()
                self.table.append(temp_model.from_map(k1))

        return self

class DescribeInclinedTablesResponseBodyItemsTable(DaraModel):
    def __init__(
        self,
        is_incline: bool = None,
        name: str = None,
        row_count: int = None,
        schema: str = None,
        size: int = None,
        space_ratio: float = None,
        total_size: int = None,
        type: str = None,
    ):
        # Indicates whether data is skewed in the table.
        self.is_incline = is_incline
        # The name of the table.
        self.name = name
        # The number of rows in the table.
        self.row_count = row_count
        # The name of the database.
        self.schema = schema
        # The number of rows in the table.
        self.size = size
        # The percentage of the table size. Unit: %.
        # 
        # >  Formula: Table storage percentage = Total data size of a table/Total data size of the cluster × 100%.
        self.space_ratio = space_ratio
        # The total data size of the table. Unit: bytes.
        # 
        # >  The following formulas can be used to calculate the total data size:
        # 
        # *   Formula 1: Total data size = Hot data size + Cold data size.
        # *   Formula 2: Total data size = Data size of table records + Data size of regular indexes + Data size of primary key indexes + Data size of other data.
        self.total_size = total_size
        # The detection type of the table.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_incline is not None:
            result['IsIncline'] = self.is_incline

        if self.name is not None:
            result['Name'] = self.name

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.size is not None:
            result['Size'] = self.size

        if self.space_ratio is not None:
            result['SpaceRatio'] = self.space_ratio

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsIncline') is not None:
            self.is_incline = m.get('IsIncline')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SpaceRatio') is not None:
            self.space_ratio = m.get('SpaceRatio')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeInclinedTablesResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        status: str = None,
    ):
        # The message of the detection result.
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

