# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class QuerySkuPriceListRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        lang: str = None,
        next_page_token: str = None,
        page_size: int = None,
        price_entity_code: str = None,
        price_factor_condition_map: Dict[str, List[str]] = None,
    ):
        # The code of the service.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        self.lang = lang
        # The token that is used to retrieve the next page. You do not need to set this parameter if you query coverage details for the first time. The response returns a token that you can use to query coverage details of the next page. If a null value is returned for the NextPageToken parameter, no more coverage details can be queried.
        self.next_page_token = next_page_token
        # The number of entries to be returned on each page. Maximum value: 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The code of the pricing object.
        # 
        # This parameter is required.
        self.price_entity_code = price_entity_code
        # The conditions of the pricing factors.
        self.price_factor_condition_map = price_factor_condition_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.price_entity_code is not None:
            result['PriceEntityCode'] = self.price_entity_code

        if self.price_factor_condition_map is not None:
            result['PriceFactorConditionMap'] = self.price_factor_condition_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PriceEntityCode') is not None:
            self.price_entity_code = m.get('PriceEntityCode')

        if m.get('PriceFactorConditionMap') is not None:
            self.price_factor_condition_map = m.get('PriceFactorConditionMap')

        return self

