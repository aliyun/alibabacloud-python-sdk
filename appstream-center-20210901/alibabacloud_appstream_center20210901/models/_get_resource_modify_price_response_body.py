# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetResourceModifyPriceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetResourceModifyPriceResponseBodyData = None,
        request_id: str = None,
    ):
        # The quote for the resource scale-out of the delivery group, which includes the price details and pricing rules.
        self.data = data
        # The unique ID of the request, which is used to locate and troubleshoot request issues.
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
            temp_model = main_models.GetResourceModifyPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetResourceModifyPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        price: main_models.GetResourceModifyPriceResponseBodyDataPrice = None,
        rules: List[main_models.GetResourceModifyPriceResponseBodyDataRules] = None,
    ):
        # The price details of the scale-out. For the currency, see Currency. For the coupon selection status, see Promotions.
        self.price = price
        # The list of pricing rules for the quote, which describes the applicable pricing or discount rules.
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
            temp_model = main_models.GetResourceModifyPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m.get('Price'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetResourceModifyPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class GetResourceModifyPriceResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the pricing rule, such as the user discount applicable to the quote.
        self.description = description
        # The ID of the pricing rule, which is used to identify the rule applied in the quote.
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

class GetResourceModifyPriceResponseBodyDataPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        promotions: List[main_models.GetResourceModifyPriceResponseBodyDataPricePromotions] = None,
        trade_price: float = None,
    ):
        # The currency code of the price amount. CNY indicates Chinese Yuan. Use this field to interpret the amounts in OriginalPrice, DiscountPrice, and TradePrice.
        self.currency = currency
        # The discount amount for the scale-out, not the discount percentage.
        # 
        # The final price TradePrice is obtained by subtracting this value from the original price OriginalPrice. For the currency, see Currency.
        self.discount_price = discount_price
        # The original price of the scale-out, which is the amount before discounts. For the currency, see Currency.
        self.original_price = original_price
        # The list of available coupons returned in the quote. Each item includes the coupon ID, name, description, and selection status.
        self.promotions = promotions
        # The final price of the scale-out after discounts.
        # 
        # Calculation formula: TradePrice = OriginalPrice - DiscountPrice. For the currency, see Currency. This operation returns only a quote and does not execute payment.
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
                temp_model = main_models.GetResourceModifyPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class GetResourceModifyPriceResponseBodyDataPricePromotions(DaraModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The option code of the coupon, which identifies the coupon returned in the quote together with PromotionId.
        self.option_code = option_code
        # The description of the coupon, which is used to display information about the discount.
        self.promotion_desc = promotion_desc
        # The ID of the coupon, which is used to identify the coupon returned in the quote.
        self.promotion_id = promotion_id
        # The name of the coupon, which is used to display the available discount in the quote.
        self.promotion_name = promotion_name
        # Specifies whether the coupon is selected in the quote. Valid values:
        # 
        # - true: Selected. The coupon is applied in the quote.
        # - false: Not selected. The coupon is not applied in the quote.
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

