# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class CheckSelectedDomainStatusResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: main_models.CheckSelectedDomainStatusResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Module') is not None:
            temp_model = main_models.CheckSelectedDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckSelectedDomainStatusResponseBodyModule(DaraModel):
    def __init__(
        self,
        dead_date: int = None,
        domain: str = None,
        end_time: int = None,
        premium: bool = None,
        price: float = None,
        reg_date: int = None,
    ):
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

