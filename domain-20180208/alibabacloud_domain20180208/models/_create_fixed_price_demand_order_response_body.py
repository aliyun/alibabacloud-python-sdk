# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class CreateFixedPriceDemandOrderResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: main_models.CreateFixedPriceDemandOrderResponseBodyModule = None,
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
            temp_model = main_models.CreateFixedPriceDemandOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateFixedPriceDemandOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        order_no: str = None,
        price: int = None,
    ):
        self.domain = domain
        self.order_no = order_no
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        if self.price is not None:
            result['Price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        return self

