# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ChangeApplyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.ChangeApplyResponseBodyData = None,
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
            temp_model = main_models.ChangeApplyResponseBodyData()
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

class ChangeApplyResponseBodyData(DaraModel):
    def __init__(
        self,
        change_orders: List[main_models.ChangeApplyResponseBodyDataChangeOrders] = None,
        order_num: int = None,
    ):
        # The list of change order application results.
        self.change_orders = change_orders
        # The order number.
        self.order_num = order_num

    def validate(self):
        if self.change_orders:
            for v1 in self.change_orders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['change_orders'] = []
        if self.change_orders is not None:
            for k1 in self.change_orders:
                result['change_orders'].append(k1.to_map() if k1 else None)

        if self.order_num is not None:
            result['order_num'] = self.order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_orders = []
        if m.get('change_orders') is not None:
            for k1 in m.get('change_orders'):
                temp_model = main_models.ChangeApplyResponseBodyDataChangeOrders()
                self.change_orders.append(temp_model.from_map(k1))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        return self

class ChangeApplyResponseBodyDataChangeOrders(DaraModel):
    def __init__(
        self,
        change_order_num: int = None,
        change_order_status: int = None,
        fail_reason: str = None,
        passengers: List[main_models.ChangeApplyResponseBodyDataChangeOrdersPassengers] = None,
    ):
        # The change order number.
        self.change_order_num = change_order_num
        # The change order status. Valid values:
        # - 0: Change order created.
        # - 5: Change order creation failed.
        self.change_order_status = change_order_status
        # The reason for the change order creation failure.
        self.fail_reason = fail_reason
        # The passenger information of the change order.
        self.passengers = passengers

    def validate(self):
        if self.passengers:
            for v1 in self.passengers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num

        if self.change_order_status is not None:
            result['change_order_status'] = self.change_order_status

        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason

        result['passengers'] = []
        if self.passengers is not None:
            for k1 in self.passengers:
                result['passengers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')

        if m.get('change_order_status') is not None:
            self.change_order_status = m.get('change_order_status')

        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')

        self.passengers = []
        if m.get('passengers') is not None:
            for k1 in m.get('passengers'):
                temp_model = main_models.ChangeApplyResponseBodyDataChangeOrdersPassengers()
                self.passengers.append(temp_model.from_map(k1))

        return self

class ChangeApplyResponseBodyDataChangeOrdersPassengers(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number.
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

