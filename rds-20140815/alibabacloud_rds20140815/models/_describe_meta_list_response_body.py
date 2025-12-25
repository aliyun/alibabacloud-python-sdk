# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeMetaListResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        items: main_models.DescribeMetaListResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_page_count: int = None,
        total_record_count: int = None,
    ):
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The information about the databases and tables whose data is included in the backup set.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of pages returned.
        self.total_page_count = total_page_count
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeMetaListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

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
        meta: List[main_models.DescribeMetaListResponseBodyItemsMeta] = None,
    ):
        self.meta = meta

    def validate(self):
        if self.meta:
            for v1 in self.meta:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Meta'] = []
        if self.meta is not None:
            for k1 in self.meta:
                result['Meta'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta = []
        if m.get('Meta') is not None:
            for k1 in m.get('Meta'):
                temp_model = main_models.DescribeMetaListResponseBodyItemsMeta()
                self.meta.append(temp_model.from_map(k1))

        return self

class DescribeMetaListResponseBodyItemsMeta(DaraModel):
    def __init__(
        self,
        database: str = None,
        size: str = None,
        tables: str = None,
    ):
        # The database name.
        self.database = database
        # The table size. Unit: KB.
        self.size = size
        # The table name.
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

