# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeContainerAppRecordsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        order_key: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        # The application ID, which can be obtained by calling the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The sorting field. Valid values:
        # 
        # *   CreateTime: the time when the domain name was associated.
        # *   CreateTime: the time when the domain name was last modified.
        self.order_key = order_key
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   ASC: in ascending order.
        # *   DESC: in descending order.
        self.order_type = order_type
        # The page number. Valid values: **1** to **100000**. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Valid values: 1 to 500.
        self.page_size = page_size
        # The keyword that is used for the search.
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.order_key is not None:
            result['OrderKey'] = self.order_key

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OrderKey') is not None:
            self.order_key = m.get('OrderKey')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        return self

