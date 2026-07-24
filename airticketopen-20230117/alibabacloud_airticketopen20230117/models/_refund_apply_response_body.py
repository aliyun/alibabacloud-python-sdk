# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class RefundApplyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.RefundApplyResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
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
            temp_model = main_models.RefundApplyResponseBodyData()
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

class RefundApplyResponseBodyData(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        refund_results: List[main_models.RefundApplyResponseBodyDataRefundResults] = None,
    ):
        # The order number.
        self.order_num = order_num
        # The list of refund application results.
        self.refund_results = refund_results

    def validate(self):
        if self.refund_results:
            for v1 in self.refund_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_num is not None:
            result['order_num'] = self.order_num

        result['refund_results'] = []
        if self.refund_results is not None:
            for k1 in self.refund_results:
                result['refund_results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        self.refund_results = []
        if m.get('refund_results') is not None:
            for k1 in m.get('refund_results'):
                temp_model = main_models.RefundApplyResponseBodyDataRefundResults()
                self.refund_results.append(temp_model.from_map(k1))

        return self

class RefundApplyResponseBodyDataRefundResults(DaraModel):
    def __init__(
        self,
        fail_reason: str = None,
        refund_order_num: int = None,
        refund_passengers: List[main_models.RefundApplyResponseBodyDataRefundResultsRefundPassengers] = None,
        status: int = None,
    ):
        # The reason for the refund application failure.
        self.fail_reason = fail_reason
        # The refund order number.
        self.refund_order_num = refund_order_num
        # The list of passengers included in the refund order.
        self.refund_passengers = refund_passengers
        # The refund order status. Valid values:
        # - 0: The refund order is created.
        # - 1: The refund order failed to be created.
        self.status = status

    def validate(self):
        if self.refund_passengers:
            for v1 in self.refund_passengers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason

        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num

        result['refund_passengers'] = []
        if self.refund_passengers is not None:
            for k1 in self.refund_passengers:
                result['refund_passengers'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')

        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')

        self.refund_passengers = []
        if m.get('refund_passengers') is not None:
            for k1 in m.get('refund_passengers'):
                temp_model = main_models.RefundApplyResponseBodyDataRefundResultsRefundPassengers()
                self.refund_passengers.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class RefundApplyResponseBodyDataRefundResultsRefundPassengers(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number of the passenger.
        self.document = document
        # The first name of the passenger.
        self.first_name = first_name
        # The last name of the passenger.
        self.last_name = last_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.last_name is not None:
            result['last_name'] = self.last_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        return self

