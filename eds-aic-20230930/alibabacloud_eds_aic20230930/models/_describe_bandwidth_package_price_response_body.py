# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeBandwidthPackagePriceResponseBody(DaraModel):
    def __init__(
        self,
        price: main_models.DescribeBandwidthPackagePriceResponseBodyPrice = None,
        request_id: str = None,
        rules: List[main_models.DescribeBandwidthPackagePriceResponseBodyRules] = None,
    ):
        # The price.
        self.price = price
        # Id of the request
        self.request_id = request_id
        # The promotion rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['Price'] = self.price.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.DescribeBandwidthPackagePriceResponseBodyPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeBandwidthPackagePriceResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeBandwidthPackagePriceResponseBodyRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: str = None,
    ):
        # The rule description.
        self.description = description
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeBandwidthPackagePriceResponseBodyPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        promotions: List[main_models.DescribeBandwidthPackagePriceResponseBodyPricePromotions] = None,
        trade_price: float = None,
    ):
        # <props="china">The currency unit (CNY).
        # <props="intl">The currency unit (USD).
        self.currency = currency
        # The discounted price.
        self.discount_price = discount_price
        # The original price.
        # 
        # <props="china">Unit: CNY.
        # 
        # <props="intl">Unit: USD.
        self.original_price = original_price
        # The promotion information.
        self.promotions = promotions
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for v1 in self.promotions:
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

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

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

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribeBandwidthPackagePriceResponseBodyPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeBandwidthPackagePriceResponseBodyPricePromotions(DaraModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The promotion code.
        self.option_code = option_code
        # The promotion description.
        self.promotion_desc = promotion_desc
        # The ID of the promotion.
        self.promotion_id = promotion_id
        # The name of the promotion.
        self.promotion_name = promotion_name
        # Indicates whether the promotion is selected.
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

