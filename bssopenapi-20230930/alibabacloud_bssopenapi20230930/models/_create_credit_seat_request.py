# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateCreditSeatRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        client_token: str = None,
        period: int = None,
        period_unit: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_configs: List[main_models.CreateCreditSeatRequestSubscriptionConfigs] = None,
        subscription_type: str = None,
    ):
        self.auto_renew = auto_renew
        self.client_token = client_token
        # This parameter is required.
        self.period = period
        self.period_unit = period_unit
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_configs = subscription_configs
        self.subscription_type = subscription_type

    def validate(self):
        if self.subscription_configs:
            for v1 in self.subscription_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        result['SubscriptionConfigs'] = []
        if self.subscription_configs is not None:
            for k1 in self.subscription_configs:
                result['SubscriptionConfigs'].append(k1.to_map() if k1 else None)

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.subscription_configs = []
        if m.get('SubscriptionConfigs') is not None:
            for k1 in m.get('SubscriptionConfigs'):
                temp_model = main_models.CreateCreditSeatRequestSubscriptionConfigs()
                self.subscription_configs.append(temp_model.from_map(k1))

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

class CreateCreditSeatRequestSubscriptionConfigs(DaraModel):
    def __init__(
        self,
        configs: List[main_models.CreateCreditSeatRequestSubscriptionConfigsConfigs] = None,
        seats: int = None,
    ):
        self.configs = configs
        # This parameter is required.
        self.seats = seats

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.seats is not None:
            result['Seats'] = self.seats

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.CreateCreditSeatRequestSubscriptionConfigsConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('Seats') is not None:
            self.seats = m.get('Seats')

        return self

class CreateCreditSeatRequestSubscriptionConfigsConfigs(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

