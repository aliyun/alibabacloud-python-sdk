# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundApplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightRefundApplyResponseBodyModule = None,
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
            temp_model = main_models.FlightRefundApplyResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightRefundApplyResponseBodyModule(DaraModel):
    def __init__(
        self,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        refund_apply_id: int = None,
        refund_fee: int = None,
        refund_money: int = None,
    ):
        self.dis_order_id = dis_order_id
        self.dis_sub_order_id = dis_sub_order_id
        self.refund_apply_id = refund_apply_id
        self.refund_fee = refund_fee
        self.refund_money = refund_money

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.refund_money is not None:
            result['refund_money'] = self.refund_money

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('refund_money') is not None:
            self.refund_money = m.get('refund_money')

        return self

