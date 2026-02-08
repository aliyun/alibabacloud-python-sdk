# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMaterialFileSummaryInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        directory_id: str = None,
        name: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        status_list_shrink: str = None,
        type_list_shrink: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.directory_id = directory_id
        self.name = name
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size
        self.status_list_shrink = status_list_shrink
        self.type_list_shrink = type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.name is not None:
            result['Name'] = self.name

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list_shrink is not None:
            result['StatusList'] = self.status_list_shrink

        if self.type_list_shrink is not None:
            result['TypeList'] = self.type_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list_shrink = m.get('StatusList')

        if m.get('TypeList') is not None:
            self.type_list_shrink = m.get('TypeList')

        return self

