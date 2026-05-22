# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeContainerAppVersionsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        order_key: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        search_type: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.order_key = order_key
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.search_type = search_type

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

        if self.search_type is not None:
            result['SearchType'] = self.search_type

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

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        return self

