# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPartitionsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        table_id: str = None,
    ):
        # The partition name.
        self.name = name
        # The sort order. Default: Asc. Valid values:
        # 
        # *   Asc: Ascending order.
        # *   Desc: Descending order.
        self.order = order
        # The page number. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The sort field. Default value: CreateTime. Valid values:
        # 
        # *   CreateTime: Creation time. Supported only for MaxCompute tables.
        # *   ModifyTime: Modification time. Supported only for MaxCompute tables.
        # *   Name: Name. Used for HMS-type tables.
        # *   RecordCount: Record count. Supported only for MaxCompute tables.
        # *   DataSize: Storage size. Supported only for MaxCompute tables.
        self.sort_by = sort_by
        # The ID of the data table.You can refer to the ListTables API response and [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # This parameter is required.
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.table_id is not None:
            result['TableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        return self

