# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeMetaListResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: List[main_models.DescribeMetaListResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_page_count: str = None,
        total_record_count: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The details of databases and tables that can be restored.
        self.items = items
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned pages.
        self.total_page_count = total_page_count
        # The total number of entries.
        self.total_record_count = total_record_count

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeMetaListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeMetaListResponseBodyItems(DaraModel):
    def __init__(
        self,
        database: str = None,
        size: List[int] = None,
        tables: List[str] = None,
    ):
        # The name of the database that can be restored.
        self.database = database
        self.size = size
        # The name of the table that can be restored.
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.size is not None:
            result['Size'] = self.size

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

