# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketQueryOrderResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketQueryOrderResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketQueryOrderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketQueryOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        order: main_models.TicketQueryOrderResponseBodyDataOrder = None,
        vouchers: List[main_models.TicketQueryOrderResponseBodyDataVouchers] = None,
    ):
        self.order = order
        self.vouchers = vouchers

    def validate(self):
        if self.order:
            self.order.validate()
        if self.vouchers:
            for v1 in self.vouchers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        result['Vouchers'] = []
        if self.vouchers is not None:
            for k1 in self.vouchers:
                result['Vouchers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.TicketQueryOrderResponseBodyDataOrder()
            self.order = temp_model.from_map(m.get('Order'))

        self.vouchers = []
        if m.get('Vouchers') is not None:
            for k1 in m.get('Vouchers'):
                temp_model = main_models.TicketQueryOrderResponseBodyDataVouchers()
                self.vouchers.append(temp_model.from_map(k1))

        return self

class TicketQueryOrderResponseBodyDataVouchers(DaraModel):
    def __init__(
        self,
        code: str = None,
        total_times: int = None,
        type: int = None,
        url: str = None,
    ):
        self.code = code
        self.total_times = total_times
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.total_times is not None:
            result['TotalTimes'] = self.total_times

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('TotalTimes') is not None:
            self.total_times = m.get('TotalTimes')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class TicketQueryOrderResponseBodyDataOrder(DaraModel):
    def __init__(
        self,
        fund_status: int = None,
        order_id: str = None,
        order_status: int = None,
    ):
        self.fund_status = fund_status
        self.order_id = order_id
        self.order_status = order_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fund_status is not None:
            result['FundStatus'] = self.fund_status

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundStatus') is not None:
            self.fund_status = m.get('FundStatus')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        return self

