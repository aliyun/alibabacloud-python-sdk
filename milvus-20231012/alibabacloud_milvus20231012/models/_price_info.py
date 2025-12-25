# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class PriceInfo(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_amount: str = None,
        optional_promotions: List[main_models.PromotionInfo] = None,
        original_amount: str = None,
        price_modules: List[main_models.PriceInfoPriceModules] = None,
        rules: List[main_models.PriceInfoRules] = None,
        tax_amount: str = None,
        trade_amount: str = None,
    ):
        self.currency = currency
        self.discount_amount = discount_amount
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.price_modules = price_modules
        self.rules = rules
        self.tax_amount = tax_amount
        self.trade_amount = trade_amount

    def validate(self):
        if self.optional_promotions:
            for v1 in self.optional_promotions:
                 if v1:
                    v1.validate()
        if self.price_modules:
            for v1 in self.price_modules:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['currency'] = self.currency

        if self.discount_amount is not None:
            result['discountAmount'] = self.discount_amount

        result['optionalPromotions'] = []
        if self.optional_promotions is not None:
            for k1 in self.optional_promotions:
                result['optionalPromotions'].append(k1.to_map() if k1 else None)

        if self.original_amount is not None:
            result['originalAmount'] = self.original_amount

        result['priceModules'] = []
        if self.price_modules is not None:
            for k1 in self.price_modules:
                result['priceModules'].append(k1.to_map() if k1 else None)

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        if self.trade_amount is not None:
            result['tradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('discountAmount') is not None:
            self.discount_amount = m.get('discountAmount')

        self.optional_promotions = []
        if m.get('optionalPromotions') is not None:
            for k1 in m.get('optionalPromotions'):
                temp_model = main_models.PromotionInfo()
                self.optional_promotions.append(temp_model.from_map(k1))

        if m.get('originalAmount') is not None:
            self.original_amount = m.get('originalAmount')

        self.price_modules = []
        if m.get('priceModules') is not None:
            for k1 in m.get('priceModules'):
                temp_model = main_models.PriceInfoPriceModules()
                self.price_modules.append(temp_model.from_map(k1))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.PriceInfoRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        if m.get('tradeAmount') is not None:
            self.trade_amount = m.get('tradeAmount')

        return self

class PriceInfoRules(DaraModel):
    def __init__(
        self,
        amount: str = None,
        name: str = None,
        rule_id: str = None,
    ):
        self.amount = amount
        self.name = name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.name is not None:
            result['name'] = self.name

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

class PriceInfoPriceModules(DaraModel):
    def __init__(
        self,
        original_amount: str = None,
        type: str = None,
    ):
        self.original_amount = original_amount
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_amount is not None:
            result['originalAmount'] = self.original_amount

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalAmount') is not None:
            self.original_amount = m.get('originalAmount')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

