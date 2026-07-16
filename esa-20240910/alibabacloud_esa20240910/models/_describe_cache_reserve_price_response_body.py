# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeCacheReservePriceResponseBody(DaraModel):
    def __init__(
        self,
        price_model: main_models.DescribeCacheReservePriceResponseBodyPriceModel = None,
        request_id: str = None,
    ):
        # The price information.
        self.price_model = price_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceModel') is not None:
            temp_model = main_models.DescribeCacheReservePriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m.get('PriceModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCacheReservePriceResponseBodyPriceModel(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        price: float = None,
        rule: main_models.DescribeCacheReservePriceResponseBodyPriceModelRule = None,
        total_price: float = None,
    ):
        # The currency. Valid values:
        # 
        # - JPY: Japanese Yen.
        # 
        # - USD: US Dollar.
        # 
        # - CNY: Chinese Yuan.
        self.currency = currency
        # The discount amount of the order.
        self.discount_price = discount_price
        # The final order price, which is the actual transaction price.
        self.price = price
        self.rule = rule
        # The original order price. Original order price = actual transaction price + discount amount.
        self.total_price = total_price

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.price is not None:
            result['Price'] = self.price

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        if self.total_price is not None:
            result['TotalPrice'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Rule') is not None:
            temp_model = main_models.DescribeCacheReservePriceResponseBodyPriceModelRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')

        return self

class DescribeCacheReservePriceResponseBodyPriceModelRule(DaraModel):
    def __init__(
        self,
        rule_list: List[main_models.DescribeCacheReservePriceResponseBodyPriceModelRuleRuleList] = None,
    ):
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeCacheReservePriceResponseBodyPriceModelRuleRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class DescribeCacheReservePriceResponseBodyPriceModelRuleRuleList(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_desc_id: int = None,
    ):
        self.name = name
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

