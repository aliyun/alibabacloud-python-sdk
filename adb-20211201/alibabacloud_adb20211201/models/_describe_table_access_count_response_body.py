# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeTableAccessCountResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeTableAccessCountResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried tables.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
                temp_model = main_models.DescribeTableAccessCountResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTableAccessCountResponseBodyItems(DaraModel):
    def __init__(
        self,
        access_count: str = None,
        instance_name: str = None,
        report_date: str = None,
        table_name: str = None,
        table_schema: str = None,
    ):
        # The number of accesses to the table.
        self.access_count = access_count
        # The ID of the cluster to which the table belongs.
        self.instance_name = instance_name
        # The date when the table was accessed.
        self.report_date = report_date
        # The name of the table.
        self.table_name = table_name
        # The database to which the table belongs.
        self.table_schema = table_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_count is not None:
            result['AccessCount'] = self.access_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')

        return self

