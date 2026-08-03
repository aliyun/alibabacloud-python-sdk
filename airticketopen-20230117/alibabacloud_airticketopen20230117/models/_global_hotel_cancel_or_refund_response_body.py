# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelCancelOrRefundResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelCancelOrRefundResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.tracer_id = tracer_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GlobalHotelCancelOrRefundResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelCancelOrRefundResponseBodyData(DaraModel):
    def __init__(
        self,
        refund_order_id: str = None,
        total_penalty_amount: main_models.GlobalHotelCancelOrRefundResponseBodyDataTotalPenaltyAmount = None,
        total_refund_amount: main_models.GlobalHotelCancelOrRefundResponseBodyDataTotalRefundAmount = None,
        tracer_id: str = None,
    ):
        self.refund_order_id = refund_order_id
        self.total_penalty_amount = total_penalty_amount
        self.total_refund_amount = total_refund_amount
        self.tracer_id = tracer_id

    def validate(self):
        if self.total_penalty_amount:
            self.total_penalty_amount.validate()
        if self.total_refund_amount:
            self.total_refund_amount.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refund_order_id is not None:
            result['RefundOrderId'] = self.refund_order_id

        if self.total_penalty_amount is not None:
            result['TotalPenaltyAmount'] = self.total_penalty_amount.to_map()

        if self.total_refund_amount is not None:
            result['TotalRefundAmount'] = self.total_refund_amount.to_map()

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefundOrderId') is not None:
            self.refund_order_id = m.get('RefundOrderId')

        if m.get('TotalPenaltyAmount') is not None:
            temp_model = main_models.GlobalHotelCancelOrRefundResponseBodyDataTotalPenaltyAmount()
            self.total_penalty_amount = temp_model.from_map(m.get('TotalPenaltyAmount'))

        if m.get('TotalRefundAmount') is not None:
            temp_model = main_models.GlobalHotelCancelOrRefundResponseBodyDataTotalRefundAmount()
            self.total_refund_amount = temp_model.from_map(m.get('TotalRefundAmount'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelCancelOrRefundResponseBodyDataTotalRefundAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelCancelOrRefundResponseBodyDataTotalPenaltyAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

