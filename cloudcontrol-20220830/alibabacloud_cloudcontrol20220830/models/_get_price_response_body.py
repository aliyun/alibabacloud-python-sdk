# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class GetPriceResponseBody(DaraModel):
    def __init__(
        self,
        price: main_models.GetPriceResponseBodyPrice = None,
        request_id: str = None,
    ):
        # The price.
        self.price = price
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['price'] = self.price.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('price') is not None:
            temp_model = main_models.GetPriceResponseBodyPrice()
            self.price = temp_model.from_map(m.get('price'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPriceResponseBodyPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        module_details: List[main_models.GetPriceResponseBodyPriceModuleDetails] = None,
        original_price: float = None,
        promotion_details: List[main_models.GetPriceResponseBodyPricePromotionDetails] = None,
        trade_price: float = None,
    ):
        # The currency type. Valid values: CNY: Chinese Yuan. USD: US dollar. JPY: Japanese Yen.
        self.currency = currency
        # The discount.
        self.discount_price = discount_price
        # The order details of the pricing module.
        self.module_details = module_details
        # The original price.
        self.original_price = original_price
        # The details of the promotion.
        self.promotion_details = promotion_details
        # The discount price.
        self.trade_price = trade_price

    def validate(self):
        if self.module_details:
            for v1 in self.module_details:
                 if v1:
                    v1.validate()
        if self.promotion_details:
            for v1 in self.promotion_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['currency'] = self.currency

        if self.discount_price is not None:
            result['discountPrice'] = self.discount_price

        result['moduleDetails'] = []
        if self.module_details is not None:
            for k1 in self.module_details:
                result['moduleDetails'].append(k1.to_map() if k1 else None)

        if self.original_price is not None:
            result['originalPrice'] = self.original_price

        result['promotionDetails'] = []
        if self.promotion_details is not None:
            for k1 in self.promotion_details:
                result['promotionDetails'].append(k1.to_map() if k1 else None)

        if self.trade_price is not None:
            result['tradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('discountPrice') is not None:
            self.discount_price = m.get('discountPrice')

        self.module_details = []
        if m.get('moduleDetails') is not None:
            for k1 in m.get('moduleDetails'):
                temp_model = main_models.GetPriceResponseBodyPriceModuleDetails()
                self.module_details.append(temp_model.from_map(k1))

        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')

        self.promotion_details = []
        if m.get('promotionDetails') is not None:
            for k1 in m.get('promotionDetails'):
                temp_model = main_models.GetPriceResponseBodyPricePromotionDetails()
                self.promotion_details.append(temp_model.from_map(k1))

        if m.get('tradePrice') is not None:
            self.trade_price = m.get('tradePrice')

        return self

class GetPriceResponseBodyPricePromotionDetails(DaraModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_id: int = None,
        promotion_name: str = None,
    ):
        # The description of the promotion.
        self.promotion_desc = promotion_desc
        # The ID of the promotion.
        self.promotion_id = promotion_id
        # The name of the promotion.
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_desc is not None:
            result['promotionDesc'] = self.promotion_desc

        if self.promotion_id is not None:
            result['promotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['promotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promotionDesc') is not None:
            self.promotion_desc = m.get('promotionDesc')

        if m.get('promotionId') is not None:
            self.promotion_id = m.get('promotionId')

        if m.get('promotionName') is not None:
            self.promotion_name = m.get('promotionName')

        return self

class GetPriceResponseBodyPriceModuleDetails(DaraModel):
    def __init__(
        self,
        cost_after_discount: float = None,
        invoice_discount: float = None,
        module_code: str = None,
        module_name: str = None,
        original_cost: float = None,
        price_type: str = None,
    ):
        # The discount price.
        self.cost_after_discount = cost_after_discount
        # The discount.
        self.invoice_discount = invoice_discount
        # The code of the pricing module.
        self.module_code = module_code
        # The name of the pricing module.
        self.module_name = module_name
        # The original price.
        self.original_cost = original_cost
        # The price type.
        self.price_type = price_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_after_discount is not None:
            result['costAfterDiscount'] = self.cost_after_discount

        if self.invoice_discount is not None:
            result['invoiceDiscount'] = self.invoice_discount

        if self.module_code is not None:
            result['moduleCode'] = self.module_code

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.original_cost is not None:
            result['originalCost'] = self.original_cost

        if self.price_type is not None:
            result['priceType'] = self.price_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('costAfterDiscount') is not None:
            self.cost_after_discount = m.get('costAfterDiscount')

        if m.get('invoiceDiscount') is not None:
            self.invoice_discount = m.get('invoiceDiscount')

        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('originalCost') is not None:
            self.original_cost = m.get('originalCost')

        if m.get('priceType') is not None:
            self.price_type = m.get('priceType')

        return self

