# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySkuPriceListShrinkRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        lang: str = None,
        next_page_token: str = None,
        page_size: int = None,
        price_entity_code: str = None,
        price_factor_condition_map_shrink: str = None,
    ):
        # The commodity code. You can call the **QueryCommodityList** operation to query the commodity code.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The language. Default value: zh (Chinese).
        self.lang = lang
        # The pagination token. Leave this parameter empty for the first page query. The query result returns a token for the next page. An empty token in the result indicates that all data has been retrieved. You can obtain the next page token from the **NextPageToken** field in the query result.
        self.next_page_token = next_page_token
        # The number of entries per page. Maximum value: 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The pricing entity code. You can call the **QueryPriceEntityList** operation to query the pricing entity code.
        # 
        # This parameter is required.
        self.price_entity_code = price_entity_code
        # The collection of pricing factor conditions. You can call the **QueryPriceEntityList** operation to query pricing factor codes and pricing factor values.
        self.price_factor_condition_map_shrink = price_factor_condition_map_shrink

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

        if self.price_factor_condition_map_shrink is not None:
            result['PriceFactorConditionMap'] = self.price_factor_condition_map_shrink

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
            self.price_factor_condition_map_shrink = m.get('PriceFactorConditionMap')

        return self

