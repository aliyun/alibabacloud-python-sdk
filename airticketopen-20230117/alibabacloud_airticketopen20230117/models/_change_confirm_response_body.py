# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ChangeConfirmResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.ChangeConfirmResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned for a failed request.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful requests.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.ChangeConfirmResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ChangeConfirmResponseBodyData(DaraModel):
    def __init__(
        self,
        pay_amount: float = None,
        pay_time: int = None,
        transaction_no: str = None,
    ):
        # The payment amount for the flight change.
        self.pay_amount = pay_amount
        self.pay_time = pay_time
        # The payment transaction number for the flight change.
        self.transaction_no = transaction_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pay_amount is not None:
            result['pay_amount'] = self.pay_amount

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pay_amount') is not None:
            self.pay_amount = m.get('pay_amount')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        return self

