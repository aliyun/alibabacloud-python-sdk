# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetResourceRenewPriceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetResourceRenewPriceResponseBodyData = None,
        request_id: str = None,
    ):
        # The price object.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetResourceRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetResourceRenewPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        price: main_models.GetResourceRenewPriceResponseBodyDataPrice = None,
        rules: List[main_models.GetResourceRenewPriceResponseBodyDataRules] = None,
    ):
        # The price details.
        self.price = price
        # The price calculation rules.
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

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.GetResourceRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m.get('Price'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetResourceRenewPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class GetResourceRenewPriceResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the price calculation rule.
        self.description = description
        # The ID of the price calculation rule.
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

class GetResourceRenewPriceResponseBodyDataPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[main_models.GetResourceRenewPriceResponseBodyDataPricePromotions] = None,
        trade_price: str = None,
    ):
        # The currency type.
        self.currency = currency
        # The discount. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The coupon description.
        self.promotions = promotions
        # The actual price. The actual price is calculated based on the following formula: Actual price = Original price - Discount.
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
                temp_model = main_models.GetResourceRenewPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class GetResourceRenewPriceResponseBodyDataPricePromotions(DaraModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The coupon code.
        self.option_code = option_code
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The coupon ID.
        self.promotion_id = promotion_id
        # The coupon name.
        self.promotion_name = promotion_name
        # Indicates whether the coupon was used.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
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

