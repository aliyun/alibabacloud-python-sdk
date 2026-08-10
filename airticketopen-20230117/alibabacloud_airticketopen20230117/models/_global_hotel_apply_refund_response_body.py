# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelApplyRefundResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelApplyRefundResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # TraceId
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
            temp_model = main_models.GlobalHotelApplyRefundResponseBodyData()
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

class GlobalHotelApplyRefundResponseBodyData(DaraModel):
    def __init__(
        self,
        sell_refund_order_id: int = None,
        total_penalty_amount: main_models.GlobalHotelApplyRefundResponseBodyDataTotalPenaltyAmount = None,
        total_refund_amount: main_models.GlobalHotelApplyRefundResponseBodyDataTotalRefundAmount = None,
        tracer_id: str = None,
    ):
        # The after-sales refund order ID.
        self.sell_refund_order_id = sell_refund_order_id
        # The total penalty amount.
        self.total_penalty_amount = total_penalty_amount
        # The total refund amount.
        self.total_refund_amount = total_refund_amount
        # TraceId
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
        if self.sell_refund_order_id is not None:
            result['SellRefundOrderId'] = self.sell_refund_order_id

        if self.total_penalty_amount is not None:
            result['TotalPenaltyAmount'] = self.total_penalty_amount.to_map()

        if self.total_refund_amount is not None:
            result['TotalRefundAmount'] = self.total_refund_amount.to_map()

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SellRefundOrderId') is not None:
            self.sell_refund_order_id = m.get('SellRefundOrderId')

        if m.get('TotalPenaltyAmount') is not None:
            temp_model = main_models.GlobalHotelApplyRefundResponseBodyDataTotalPenaltyAmount()
            self.total_penalty_amount = temp_model.from_map(m.get('TotalPenaltyAmount'))

        if m.get('TotalRefundAmount') is not None:
            temp_model = main_models.GlobalHotelApplyRefundResponseBodyDataTotalRefundAmount()
            self.total_refund_amount = temp_model.from_map(m.get('TotalRefundAmount'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelApplyRefundResponseBodyDataTotalRefundAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TraceId
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

class GlobalHotelApplyRefundResponseBodyDataTotalPenaltyAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TraceId
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

