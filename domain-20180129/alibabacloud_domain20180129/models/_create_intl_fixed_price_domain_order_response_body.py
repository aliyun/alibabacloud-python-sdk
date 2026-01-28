# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class CreateIntlFixedPriceDomainOrderResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.CreateIntlFixedPriceDomainOrderResponseBodyModule = None,
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
            temp_model = main_models.CreateIntlFixedPriceDomainOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateIntlFixedPriceDomainOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        order_no: str = None,
        pay_price: int = None,
        pay_url: str = None,
    ):
        self.domain = domain
        self.order_no = order_no
        self.pay_price = pay_price
        self.pay_url = pay_url

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

        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price

        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')

        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')

        return self

