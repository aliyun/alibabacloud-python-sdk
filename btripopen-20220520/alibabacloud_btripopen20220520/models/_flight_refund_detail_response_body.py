# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightRefundDetailResponseBodyModule = None,
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
            temp_model = main_models.FlightRefundDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightRefundDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        btrip_order_id: int = None,
        btrip_sub_order_id: int = None,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        is_voluntary: int = None,
        reason: str = None,
        refund_fee: int = None,
        refund_fee_list: List[main_models.FlightRefundDetailResponseBodyModuleRefundFeeList] = None,
        refund_price: int = None,
        status: str = None,
    ):
        self.btrip_order_id = btrip_order_id
        self.btrip_sub_order_id = btrip_sub_order_id
        self.dis_order_id = dis_order_id
        self.dis_sub_order_id = dis_sub_order_id
        self.is_voluntary = is_voluntary
        self.reason = reason
        self.refund_fee = refund_fee
        self.refund_fee_list = refund_fee_list
        self.refund_price = refund_price
        self.status = status

    def validate(self):
        if self.refund_fee_list:
            for v1 in self.refund_fee_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.btrip_sub_order_id is not None:
            result['btrip_sub_order_id'] = self.btrip_sub_order_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.reason is not None:
            result['reason'] = self.reason

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        result['refund_fee_list'] = []
        if self.refund_fee_list is not None:
            for k1 in self.refund_fee_list:
                result['refund_fee_list'].append(k1.to_map() if k1 else None)

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('btrip_sub_order_id') is not None:
            self.btrip_sub_order_id = m.get('btrip_sub_order_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        self.refund_fee_list = []
        if m.get('refund_fee_list') is not None:
            for k1 in m.get('refund_fee_list'):
                temp_model = main_models.FlightRefundDetailResponseBodyModuleRefundFeeList()
                self.refund_fee_list.append(temp_model.from_map(k1))

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class FlightRefundDetailResponseBodyModuleRefundFeeList(DaraModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        refund_fee: int = None,
        refund_price: int = None,
        status: str = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.refund_fee = refund_fee
        self.refund_price = refund_price
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

