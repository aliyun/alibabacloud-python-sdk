# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeRenewalPriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribeRenewalPriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # Details about the prices and promotion rules.
        self.price_info = price_info
        # The ID of the request.
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
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRenewalPriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        price: main_models.DescribeRenewalPriceResponseBodyPriceInfoPrice = None,
        rules: main_models.DescribeRenewalPriceResponseBodyPriceInfoRules = None,
    ):
        # The price.
        self.price = price
        # The information about the promotion rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['Price'] = self.price.to_map()

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class DescribeRenewalPriceResponseBodyPriceInfoRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeRenewalPriceResponseBodyPriceInfoRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyPriceInfoRulesRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the promotion rule.
        self.description = description
        # The ID of the promotion rule.
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

class DescribeRenewalPriceResponseBodyPriceInfoPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        detail_infos: main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfos = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        # The currency unit.
        # 
        # Alibaba Cloud China site (aliyun.com): CNY.
        # 
        # Alibaba Cloud International site (alibabacloud.com): USD.
        self.currency = currency
        # Details about the resource prices.
        self.detail_infos = detail_infos
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.detail_infos:
            self.detail_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.detail_infos is not None:
            result['DetailInfos'] = self.detail_infos.to_map()

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DetailInfos') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfos()
            self.detail_infos = temp_model.from_map(m.get('DetailInfos'))

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfos(DaraModel):
    def __init__(
        self,
        detail_info: List[main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo] = None,
    ):
        self.detail_info = detail_info

    def validate(self):
        if self.detail_info:
            for v1 in self.detail_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailInfo'] = []
        if self.detail_info is not None:
            for k1 in self.detail_info:
                result['DetailInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_info = []
        if m.get('DetailInfo') is not None:
            for k1 in m.get('DetailInfo'):
                temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo()
                self.detail_info.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfo(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        resource: str = None,
        sub_rules: main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules = None,
        trade_price: float = None,
    ):
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The name of the resource that corresponds to the price.
        self.resource = resource
        # The pricing rules.
        self.sub_rules = sub_rules
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.sub_rules:
            self.sub_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.sub_rules is not None:
            result['SubRules'] = self.sub_rules.to_map()

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('SubRules') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules()
            self.sub_rules = temp_model.from_map(m.get('SubRules'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the pricing rule.
        self.description = description
        # The ID of the pricing rule.
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

