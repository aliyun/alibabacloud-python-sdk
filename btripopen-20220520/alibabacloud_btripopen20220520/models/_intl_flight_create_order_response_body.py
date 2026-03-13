# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightCreateOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightCreateOrderResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.IntlFlightCreateOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightCreateOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        async_create_order_key: str = None,
        order_id: str = None,
        out_order_id: str = None,
        pay_latest_time: str = None,
        pay_status: int = None,
        status: int = None,
        total_price: int = None,
    ):
        self.async_create_order_key = async_create_order_key
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.pay_latest_time = pay_latest_time
        self.pay_status = pay_status
        self.status = status
        self.total_price = total_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_create_order_key is not None:
            result['async_create_order_key'] = self.async_create_order_key

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.pay_latest_time is not None:
            result['pay_latest_time'] = self.pay_latest_time

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.status is not None:
            result['status'] = self.status

        if self.total_price is not None:
            result['total_price'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_create_order_key') is not None:
            self.async_create_order_key = m.get('async_create_order_key')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('pay_latest_time') is not None:
            self.pay_latest_time = m.get('pay_latest_time')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        return self

