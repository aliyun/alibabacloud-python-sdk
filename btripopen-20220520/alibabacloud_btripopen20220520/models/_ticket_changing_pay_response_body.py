# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingPayResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TicketChangingPayResponseBodyModule = None,
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
            temp_model = main_models.TicketChangingPayResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TicketChangingPayResponseBodyModule(DaraModel):
    def __init__(
        self,
        can_retry: bool = None,
        pay_price: int = None,
        pay_status: int = None,
        pay_time: str = None,
        trade_no: str = None,
    ):
        self.can_retry = can_retry
        self.pay_price = pay_price
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.trade_no = trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_retry is not None:
            result['can_retry'] = self.can_retry

        if self.pay_price is not None:
            result['pay_price'] = self.pay_price

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.trade_no is not None:
            result['trade_no'] = self.trade_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_retry') is not None:
            self.can_retry = m.get('can_retry')

        if m.get('pay_price') is not None:
            self.pay_price = m.get('pay_price')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('trade_no') is not None:
            self.trade_no = m.get('trade_no')

        return self

