# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class CheckDomainResponseBody(DaraModel):
    def __init__(
        self,
        avail: str = None,
        domain_name: str = None,
        dynamic_check: bool = None,
        premium: str = None,
        price: int = None,
        reason: str = None,
        request_id: str = None,
        static_price_info: main_models.CheckDomainResponseBodyStaticPriceInfo = None,
    ):
        self.avail = avail
        self.domain_name = domain_name
        self.dynamic_check = dynamic_check
        self.premium = premium
        self.price = price
        self.reason = reason
        self.request_id = request_id
        self.static_price_info = static_price_info

    def validate(self):
        if self.static_price_info:
            self.static_price_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avail is not None:
            result['Avail'] = self.avail

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.dynamic_check is not None:
            result['DynamicCheck'] = self.dynamic_check

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.price is not None:
            result['Price'] = self.price

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.static_price_info is not None:
            result['StaticPriceInfo'] = self.static_price_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avail') is not None:
            self.avail = m.get('Avail')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DynamicCheck') is not None:
            self.dynamic_check = m.get('DynamicCheck')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StaticPriceInfo') is not None:
            temp_model = main_models.CheckDomainResponseBodyStaticPriceInfo()
            self.static_price_info = temp_model.from_map(m.get('StaticPriceInfo'))

        return self

class CheckDomainResponseBodyStaticPriceInfo(DaraModel):
    def __init__(
        self,
        price_info: List[main_models.CheckDomainResponseBodyStaticPriceInfoPriceInfo] = None,
    ):
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            for v1 in self.price_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PriceInfo'] = []
        if self.price_info is not None:
            for k1 in self.price_info:
                result['PriceInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.price_info = []
        if m.get('PriceInfo') is not None:
            for k1 in m.get('PriceInfo'):
                temp_model = main_models.CheckDomainResponseBodyStaticPriceInfoPriceInfo()
                self.price_info.append(temp_model.from_map(k1))

        return self

class CheckDomainResponseBodyStaticPriceInfoPriceInfo(DaraModel):
    def __init__(
        self,
        action: str = None,
        money: float = None,
        period: int = None,
    ):
        self.action = action
        self.money = money
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.money is not None:
            result['money'] = self.money

        if self.period is not None:
            result['period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('money') is not None:
            self.money = m.get('money')

        if m.get('period') is not None:
            self.period = m.get('period')

        return self

