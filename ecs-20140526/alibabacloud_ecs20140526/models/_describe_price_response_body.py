# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # The information about the prices and promotion rules.
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
        price: main_models.DescribePriceResponseBodyPriceInfoPrice = None,
        related_price: main_models.DescribePriceResponseBodyPriceInfoRelatedPrice = None,
        rules: main_models.DescribePriceResponseBodyPriceInfoRules = None,
    ):
        # The price.
        self.price = price
        # The related price.
        self.related_price = related_price
        # The information about the promotion rules.
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.related_price:
            self.related_price.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['Price'] = self.price.to_map()

        if self.related_price is not None:
            result['RelatedPrice'] = self.related_price.to_map()

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('RelatedPrice') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoRelatedPrice()
            self.related_price = temp_model.from_map(m.get('RelatedPrice'))

        if m.get('Rules') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class DescribePriceResponseBodyPriceInfoRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribePriceResponseBodyPriceInfoRulesRule] = None,
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
                temp_model = main_models.DescribePriceResponseBodyPriceInfoRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoRulesRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The description of the promotion rule.
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

class DescribePriceResponseBodyPriceInfoRelatedPrice(DaraModel):
    def __init__(
        self,
        marketplace_image_price: main_models.DescribePriceResponseBodyPriceInfoRelatedPriceMarketplaceImagePrice = None,
    ):
        # The Alibaba Cloud Marketplace image price.
        self.marketplace_image_price = marketplace_image_price

    def validate(self):
        if self.marketplace_image_price:
            self.marketplace_image_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marketplace_image_price is not None:
            result['MarketplaceImagePrice'] = self.marketplace_image_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarketplaceImagePrice') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoRelatedPriceMarketplaceImagePrice()
            self.marketplace_image_price = temp_model.from_map(m.get('MarketplaceImagePrice'))

        return self

class DescribePriceResponseBodyPriceInfoRelatedPriceMarketplaceImagePrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        # The currency unit.
        # 
        # China site (aliyun.com): CNY
        # 
        # International site (alibabacloud.com): USD
        self.currency = currency
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        pass

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

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        detail_infos: main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfos = None,
        discount_price: float = None,
        original_price: float = None,
        reserved_instance_hour_price: float = None,
        trade_price: float = None,
    ):
        # The currency unit.
        # 
        # Alibaba Cloud China site (aliyun.com): CNY.
        # 
        # Alibaba Cloud International site (alibabacloud.com): USD.
        self.currency = currency
        # The information about the price.
        # 
        # >  This parameter is returned only when ResourceType is set to instance.
        self.detail_infos = detail_infos
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The hourly price of the reserved instance for which the No Upfront or Partial Upfront payment option is used.
        self.reserved_instance_hour_price = reserved_instance_hour_price
        # The transaction price of the order. The transaction price is equal to the original price minus the discount.
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

        if self.reserved_instance_hour_price is not None:
            result['ReservedInstanceHourPrice'] = self.reserved_instance_hour_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DetailInfos') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfos()
            self.detail_infos = temp_model.from_map(m.get('DetailInfos'))

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('ReservedInstanceHourPrice') is not None:
            self.reserved_instance_hour_price = m.get('ReservedInstanceHourPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfos(DaraModel):
    def __init__(
        self,
        detail_info: List[main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfo] = None,
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
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfo()
                self.detail_info.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfo(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        resource: str = None,
        sub_rules: main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules = None,
        trade_price: float = None,
    ):
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The resource name. Valid values:
        # 
        # *   InstanceType
        # *   bandwidth
        # *   image
        # *   SystemDisk
        # *   DataDisk
        self.resource = resource
        # Details about the pricing rules.
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
            temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules()
            self.sub_rules = temp_model.from_map(m.get('SubRules'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule] = None,
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
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfosDetailInfoSubRulesRule(DaraModel):
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

