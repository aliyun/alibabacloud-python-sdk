# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # The price details.
        self.price_info = price_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        free_cds_quota: bool = None,
        free_cds_size: int = None,
        price: main_models.DescribePriceResponseBodyPriceInfoPrice = None,
        rules: List[main_models.DescribePriceResponseBodyPriceInfoRules] = None,
    ):
        # Indicates whether a free enterprise drive is available.
        self.free_cds_quota = free_cds_quota
        # The free capacity provided by the enterprise drive. Unit: GiB.
        self.free_cds_size = free_cds_size
        # The price.
        self.price = price
        # The details of the promotion rules.
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
        if self.free_cds_quota is not None:
            result['FreeCdsQuota'] = self.free_cds_quota

        if self.free_cds_size is not None:
            result['FreeCdsSize'] = self.free_cds_size

        if self.price is not None:
            result['Price'] = self.price.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeCdsQuota') is not None:
            self.free_cds_quota = m.get('FreeCdsQuota')

        if m.get('FreeCdsSize') is not None:
            self.free_cds_size = m.get('FreeCdsSize')

        if m.get('Price') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m.get('Price'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the rule.
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

class DescribePriceResponseBodyPriceInfoPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        order_lines: Dict[str, str] = None,
        original_price: float = None,
        promotions: List[main_models.DescribePriceResponseBodyPriceInfoPricePromotions] = None,
        sp_price: int = None,
        trade_price: float = None,
    ):
        # The unit of currency (USD).
        self.currency = currency
        # The discounted amount.
        self.discount_price = discount_price
        # The orders.
        self.order_lines = order_lines
        # The original price.
        self.original_price = original_price
        # The promotions.
        self.promotions = promotions
        # The price under an effective savings plan.
        self.sp_price = sp_price
        # The actual price. The original price minus the discounted amount equals the actual price.
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

        if self.order_lines is not None:
            result['OrderLines'] = self.order_lines

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.sp_price is not None:
            result['SpPrice'] = self.sp_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OrderLines') is not None:
            self.order_lines = m.get('OrderLines')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('SpPrice') is not None:
            self.sp_price = m.get('SpPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPricePromotions(DaraModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The description of the promotion rule.
        self.option_code = option_code
        # The description of the promotion.
        self.promotion_desc = promotion_desc
        # The promotion ID.
        self.promotion_id = promotion_id
        # The promotion name.
        self.promotion_name = promotion_name
        # Indicates whether an item is selected.
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

