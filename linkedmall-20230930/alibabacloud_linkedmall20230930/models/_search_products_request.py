# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchProductsRequest(DaraModel):
    def __init__(
        self,
        brand_name: str = None,
        category_ids: List[str] = None,
        create_end_time: str = None,
        create_start_time: str = None,
        distribution_high_price: int = None,
        distribution_high_price_ratio: int = None,
        distribution_low_price: int = None,
        distribution_low_price_ratio: int = None,
        high_mark_price: int = None,
        high_price: int = None,
        in_group: bool = None,
        in_group_end_time: str = None,
        in_group_start_time: str = None,
        inventory_risk_level: str = None,
        lm_item_id: str = None,
        low_mark_price: int = None,
        low_price: int = None,
        modify_end_time: str = None,
        modify_start_time: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        product_id: str = None,
        product_name: str = None,
        product_status: str = None,
        purchaser_id: str = None,
        tax_rate: str = None,
        trade_mode_and_credit: str = None,
    ):
        self.brand_name = brand_name
        self.category_ids = category_ids
        self.create_end_time = create_end_time
        self.create_start_time = create_start_time
        self.distribution_high_price = distribution_high_price
        self.distribution_high_price_ratio = distribution_high_price_ratio
        self.distribution_low_price = distribution_low_price
        self.distribution_low_price_ratio = distribution_low_price_ratio
        self.high_mark_price = high_mark_price
        self.high_price = high_price
        self.in_group = in_group
        self.in_group_end_time = in_group_end_time
        self.in_group_start_time = in_group_start_time
        self.inventory_risk_level = inventory_risk_level
        self.lm_item_id = lm_item_id
        self.low_mark_price = low_mark_price
        self.low_price = low_price
        self.modify_end_time = modify_end_time
        self.modify_start_time = modify_start_time
        self.order_by = order_by
        self.order_direction = order_direction
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.platform = platform
        self.product_id = product_id
        self.product_name = product_name
        self.product_status = product_status
        # This parameter is required.
        self.purchaser_id = purchaser_id
        self.tax_rate = tax_rate
        self.trade_mode_and_credit = trade_mode_and_credit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_name is not None:
            result['brandName'] = self.brand_name

        if self.category_ids is not None:
            result['categoryIds'] = self.category_ids

        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time

        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time

        if self.distribution_high_price is not None:
            result['distributionHighPrice'] = self.distribution_high_price

        if self.distribution_high_price_ratio is not None:
            result['distributionHighPriceRatio'] = self.distribution_high_price_ratio

        if self.distribution_low_price is not None:
            result['distributionLowPrice'] = self.distribution_low_price

        if self.distribution_low_price_ratio is not None:
            result['distributionLowPriceRatio'] = self.distribution_low_price_ratio

        if self.high_mark_price is not None:
            result['highMarkPrice'] = self.high_mark_price

        if self.high_price is not None:
            result['highPrice'] = self.high_price

        if self.in_group is not None:
            result['inGroup'] = self.in_group

        if self.in_group_end_time is not None:
            result['inGroupEndTime'] = self.in_group_end_time

        if self.in_group_start_time is not None:
            result['inGroupStartTime'] = self.in_group_start_time

        if self.inventory_risk_level is not None:
            result['inventoryRiskLevel'] = self.inventory_risk_level

        if self.lm_item_id is not None:
            result['lmItemId'] = self.lm_item_id

        if self.low_mark_price is not None:
            result['lowMarkPrice'] = self.low_mark_price

        if self.low_price is not None:
            result['lowPrice'] = self.low_price

        if self.modify_end_time is not None:
            result['modifyEndTime'] = self.modify_end_time

        if self.modify_start_time is not None:
            result['modifyStartTime'] = self.modify_start_time

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.platform is not None:
            result['platform'] = self.platform

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.product_status is not None:
            result['productStatus'] = self.product_status

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        if self.tax_rate is not None:
            result['taxRate'] = self.tax_rate

        if self.trade_mode_and_credit is not None:
            result['tradeModeAndCredit'] = self.trade_mode_and_credit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('brandName') is not None:
            self.brand_name = m.get('brandName')

        if m.get('categoryIds') is not None:
            self.category_ids = m.get('categoryIds')

        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')

        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')

        if m.get('distributionHighPrice') is not None:
            self.distribution_high_price = m.get('distributionHighPrice')

        if m.get('distributionHighPriceRatio') is not None:
            self.distribution_high_price_ratio = m.get('distributionHighPriceRatio')

        if m.get('distributionLowPrice') is not None:
            self.distribution_low_price = m.get('distributionLowPrice')

        if m.get('distributionLowPriceRatio') is not None:
            self.distribution_low_price_ratio = m.get('distributionLowPriceRatio')

        if m.get('highMarkPrice') is not None:
            self.high_mark_price = m.get('highMarkPrice')

        if m.get('highPrice') is not None:
            self.high_price = m.get('highPrice')

        if m.get('inGroup') is not None:
            self.in_group = m.get('inGroup')

        if m.get('inGroupEndTime') is not None:
            self.in_group_end_time = m.get('inGroupEndTime')

        if m.get('inGroupStartTime') is not None:
            self.in_group_start_time = m.get('inGroupStartTime')

        if m.get('inventoryRiskLevel') is not None:
            self.inventory_risk_level = m.get('inventoryRiskLevel')

        if m.get('lmItemId') is not None:
            self.lm_item_id = m.get('lmItemId')

        if m.get('lowMarkPrice') is not None:
            self.low_mark_price = m.get('lowMarkPrice')

        if m.get('lowPrice') is not None:
            self.low_price = m.get('lowPrice')

        if m.get('modifyEndTime') is not None:
            self.modify_end_time = m.get('modifyEndTime')

        if m.get('modifyStartTime') is not None:
            self.modify_start_time = m.get('modifyStartTime')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        if m.get('taxRate') is not None:
            self.tax_rate = m.get('taxRate')

        if m.get('tradeModeAndCredit') is not None:
            self.trade_mode_and_credit = m.get('tradeModeAndCredit')

        return self

