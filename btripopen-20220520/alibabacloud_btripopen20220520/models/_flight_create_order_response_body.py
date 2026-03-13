# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightCreateOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightCreateOrderResponseBodyModule = None,
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
            temp_model = main_models.FlightCreateOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightCreateOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        btrip_order_id: int = None,
        dis_order_id: str = None,
        last_pay_time: str = None,
        order_status: int = None,
        pay_status: int = None,
        payment_price: int = None,
        total_price: int = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.btrip_order_id = btrip_order_id
        self.dis_order_id = dis_order_id
        self.last_pay_time = last_pay_time
        self.order_status = order_status
        self.pay_status = pay_status
        self.payment_price = payment_price
        self.total_price = total_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no

        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.last_pay_time is not None:
            result['last_pay_time'] = self.last_pay_time

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.payment_price is not None:
            result['payment_price'] = self.payment_price

        if self.total_price is not None:
            result['total_price'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')

        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('last_pay_time') is not None:
            self.last_pay_time = m.get('last_pay_time')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('payment_price') is not None:
            self.payment_price = m.get('payment_price')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        return self

