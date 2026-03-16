# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GetServiceInstanceSubscriptionEstimateCostResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_prices: List[main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of resource price information.
        self.resource_prices = resource_prices

    def validate(self):
        if self.resource_prices:
            for v1 in self.resource_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcePrices'] = []
        if self.resource_prices is not None:
            for k1 in self.resource_prices:
                result['ResourcePrices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_prices = []
        if m.get('ResourcePrices') is not None:
            for k1 in m.get('ResourcePrices'):
                temp_model = main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices()
                self.resource_prices.append(temp_model.from_map(k1))

        return self

class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices(DaraModel):
    def __init__(
        self,
        currency: str = None,
        detail_infos: List[main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos] = None,
        discount_amount: float = None,
        original_amount: float = None,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
        rules: List[main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules] = None,
        trade_amount: float = None,
    ):
        # Currency. Valid values:
        # - CNY: Chinese Yuan.
        # - USD: US Dollar.
        # - JPY: Japanese Yen.
        self.currency = currency
        # The price details of the pricing module.
        self.detail_infos = detail_infos
        # Discount.
        self.discount_amount = discount_amount
        # Original price.
        self.original_amount = original_amount
        # Renewal duration. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration, which is the unit of the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn
        # Promotion details.
        self.rules = rules
        # Discounted price.
        self.trade_amount = trade_amount

    def validate(self):
        if self.detail_infos:
            for v1 in self.detail_infos:
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
            result['Currency'] = self.currency

        result['DetailInfos'] = []
        if self.detail_infos is not None:
            for k1 in self.detail_infos:
                result['DetailInfos'].append(k1.to_map() if k1 else None)

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        self.detail_infos = []
        if m.get('DetailInfos') is not None:
            for k1 in m.get('DetailInfos'):
                temp_model = main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos()
                self.detail_infos.append(temp_model.from_map(k1))

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        rule_desc_id: int = None,
    ):
        # Promotion description.
        self.description = description
        # Promotion name.
        self.name = name
        # Promotion ID.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        resource: str = None,
        trade_amount: float = None,
    ):
        # Discount amount.
        self.discount_amount = discount_amount
        # Original price.
        self.original_amount = original_amount
        # Pricing module identifier.
        self.resource = resource
        # Discounted price.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

