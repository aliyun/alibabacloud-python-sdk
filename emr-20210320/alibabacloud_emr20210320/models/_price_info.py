# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class PriceInfo(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        pay_type: str = None,
        promotion_results: List[main_models.PromotionInfo] = None,
        resource_type: str = None,
        spot_instance_type_original_price: str = None,
        spot_instance_type_price: str = None,
        spot_original_price: str = None,
        spot_price: str = None,
        tax_price: str = None,
        trade_price: str = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.pay_type = pay_type
        self.promotion_results = promotion_results
        self.resource_type = resource_type
        self.spot_instance_type_original_price = spot_instance_type_original_price
        self.spot_instance_type_price = spot_instance_type_price
        self.spot_original_price = spot_original_price
        self.spot_price = spot_price
        self.tax_price = tax_price
        self.trade_price = trade_price

    def validate(self):
        if self.promotion_results:
            for v1 in self.promotion_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        result['PromotionResults'] = []
        if self.promotion_results is not None:
            for k1 in self.promotion_results:
                result['PromotionResults'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.spot_instance_type_original_price is not None:
            result['SpotInstanceTypeOriginalPrice'] = self.spot_instance_type_original_price

        if self.spot_instance_type_price is not None:
            result['SpotInstanceTypePrice'] = self.spot_instance_type_price

        if self.spot_original_price is not None:
            result['SpotOriginalPrice'] = self.spot_original_price

        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price

        if self.tax_price is not None:
            result['TaxPrice'] = self.tax_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        self.promotion_results = []
        if m.get('PromotionResults') is not None:
            for k1 in m.get('PromotionResults'):
                temp_model = main_models.PromotionInfo()
                self.promotion_results.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SpotInstanceTypeOriginalPrice') is not None:
            self.spot_instance_type_original_price = m.get('SpotInstanceTypeOriginalPrice')

        if m.get('SpotInstanceTypePrice') is not None:
            self.spot_instance_type_price = m.get('SpotInstanceTypePrice')

        if m.get('SpotOriginalPrice') is not None:
            self.spot_original_price = m.get('SpotOriginalPrice')

        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')

        if m.get('TaxPrice') is not None:
            self.tax_price = m.get('TaxPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

