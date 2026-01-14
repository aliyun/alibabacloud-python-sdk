# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GatewayBlackWhiteListShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        desc_sort: bool = None,
        filter_params_shrink: str = None,
        order_item: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # This parameter is unavailable for public use.
        self.desc_sort = desc_sort
        # The filter parameters.
        self.filter_params_shrink = filter_params_shrink
        # This parameter is unavailable for public use.
        self.order_item = order_item
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 1.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.desc_sort is not None:
            result['DescSort'] = self.desc_sort

        if self.filter_params_shrink is not None:
            result['FilterParams'] = self.filter_params_shrink

        if self.order_item is not None:
            result['OrderItem'] = self.order_item

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DescSort') is not None:
            self.desc_sort = m.get('DescSort')

        if m.get('FilterParams') is not None:
            self.filter_params_shrink = m.get('FilterParams')

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

