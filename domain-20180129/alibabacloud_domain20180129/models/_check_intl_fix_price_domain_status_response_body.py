# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class CheckIntlFixPriceDomainStatusResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.CheckIntlFixPriceDomainStatusResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.CheckIntlFixPriceDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckIntlFixPriceDomainStatusResponseBodyModule(DaraModel):
    def __init__(
        self,
        currency: str = None,
        dead_date: int = None,
        domain: str = None,
        end_time: int = None,
        premium: bool = None,
        price: int = None,
        reg_date: int = None,
    ):
        self.currency = currency
        self.dead_date = dead_date
        self.domain = domain
        self.end_time = end_time
        self.premium = premium
        self.price = price
        self.reg_date = reg_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.price is not None:
            result['Price'] = self.price

        if self.reg_date is not None:
            result['RegDate'] = self.reg_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')

        return self

