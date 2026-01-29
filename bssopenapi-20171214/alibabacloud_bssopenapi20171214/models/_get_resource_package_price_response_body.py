# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetResourcePackagePriceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetResourcePackagePriceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetResourcePackagePriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetResourcePackagePriceResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        promotions: main_models.GetResourcePackagePriceResponseBodyDataPromotions = None,
        trade_price: float = None,
    ):
        # The type of the currency.
        self.currency = currency
        # The discounted amount. Unit: CNY.
        self.discount_price = discount_price
        # The original price. Unit: CNY.
        self.original_price = original_price
        # The details of the discount.
        self.promotions = promotions
        # The price at which the transaction is made. Unit: CNY.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            self.promotions.validate()

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

        if self.promotions is not None:
            result['Promotions'] = self.promotions.to_map()

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

        if m.get('Promotions') is not None:
            temp_model = main_models.GetResourcePackagePriceResponseBodyDataPromotions()
            self.promotions = temp_model.from_map(m.get('Promotions'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class GetResourcePackagePriceResponseBodyDataPromotions(DaraModel):
    def __init__(
        self,
        promotion: List[main_models.GetResourcePackagePriceResponseBodyDataPromotionsPromotion] = None,
    ):
        self.promotion = promotion

    def validate(self):
        if self.promotion:
            for v1 in self.promotion:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Promotion'] = []
        if self.promotion is not None:
            for k1 in self.promotion:
                result['Promotion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion = []
        if m.get('Promotion') is not None:
            for k1 in m.get('Promotion'):
                temp_model = main_models.GetResourcePackagePriceResponseBodyDataPromotionsPromotion()
                self.promotion.append(temp_model.from_map(k1))

        return self

class GetResourcePackagePriceResponseBodyDataPromotionsPromotion(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the promotion.
        self.id = id
        # The description of the discount.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

