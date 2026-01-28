# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainRealTimePriceResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: main_models.QueryDomainRealTimePriceResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        synchro: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Module') is not None:
            temp_model = main_models.QueryDomainRealTimePriceResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class QueryDomainRealTimePriceResponseBodyModule(DaraModel):
    def __init__(
        self,
        domain_prices: List[main_models.QueryDomainRealTimePriceResponseBodyModuleDomainPrices] = None,
    ):
        self.domain_prices = domain_prices

    def validate(self):
        if self.domain_prices:
            for v1 in self.domain_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainPrices'] = []
        if self.domain_prices is not None:
            for k1 in self.domain_prices:
                result['DomainPrices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_prices = []
        if m.get('DomainPrices') is not None:
            for k1 in m.get('DomainPrices'):
                temp_model = main_models.QueryDomainRealTimePriceResponseBodyModuleDomainPrices()
                self.domain_prices.append(temp_model.from_map(k1))

        return self

class QueryDomainRealTimePriceResponseBodyModuleDomainPrices(DaraModel):
    def __init__(
        self,
        action: str = None,
        avail: int = None,
        currency: str = None,
        domain_name: str = None,
        period: int = None,
        premium: bool = None,
        price: float = None,
        reason: str = None,
    ):
        self.action = action
        self.avail = avail
        self.currency = currency
        self.domain_name = domain_name
        self.period = period
        self.premium = premium
        self.price = price
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.avail is not None:
            result['Avail'] = self.avail

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.period is not None:
            result['Period'] = self.period

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.price is not None:
            result['Price'] = self.price

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Avail') is not None:
            self.avail = m.get('Avail')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

