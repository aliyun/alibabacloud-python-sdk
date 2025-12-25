# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeContainerAppsRequest(DaraModel):
    def __init__(
        self,
        order_key: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        search_type: str = None,
    ):
        # The sorting field. This parameter is left empty by default. Valid values:
        # 
        # *   Name: the version name.
        # *   CreateTime: the time when the version was created.
        # *   UpdateTime: the time when the version was last modified.
        self.order_key = order_key
        # The order in which you want to sort the query results. This parameter is left empty by default. Valid values:
        # 
        # *   ASC: in ascending order.
        # *   DESC: in descending order.
        self.order_type = order_type
        # The page number. Default value: **1**. Valid values: 1 to 65535.
        self.page_number = page_number
        # The number of entries per page. Default value: **20**. Valid values: 1 to 500.
        self.page_size = page_size
        # The search keyword.
        self.search_key = search_key
        # The search criterion based on which you want to perform fuzzy search. Valid values:
        # 
        # *   Appid: the application ID.
        # *   Name: the application name.
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        return self

