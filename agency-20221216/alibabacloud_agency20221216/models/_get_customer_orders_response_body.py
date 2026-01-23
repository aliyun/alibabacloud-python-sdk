# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetCustomerOrdersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetCustomerOrdersResponseBodyData] = None,
        message: str = None,
        msg: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.msg = msg
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetCustomerOrdersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetCustomerOrdersResponseBodyData(DaraModel):
    def __init__(
        self,
        customer_account: str = None,
        customer_manager: str = None,
        customer_no: int = None,
        order_id: int = None,
        order_source: str = None,
        order_status: int = None,
        order_type: str = None,
        original_cost: float = None,
        payment_method: str = None,
        payment_time: str = None,
        pretax_cost: float = None,
        product_detail: str = None,
        product_type: str = None,
        time_to_order: str = None,
    ):
        self.customer_account = customer_account
        self.customer_manager = customer_manager
        self.customer_no = customer_no
        self.order_id = order_id
        self.order_source = order_source
        self.order_status = order_status
        self.order_type = order_type
        self.original_cost = original_cost
        self.payment_method = payment_method
        self.payment_time = payment_time
        self.pretax_cost = pretax_cost
        self.product_detail = product_detail
        self.product_type = product_type
        self.time_to_order = time_to_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_account is not None:
            result['CustomerAccount'] = self.customer_account

        if self.customer_manager is not None:
            result['CustomerManager'] = self.customer_manager

        if self.customer_no is not None:
            result['CustomerNo'] = self.customer_no

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_source is not None:
            result['OrderSource'] = self.order_source

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time

        if self.pretax_cost is not None:
            result['PretaxCost'] = self.pretax_cost

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.time_to_order is not None:
            result['TimeToOrder'] = self.time_to_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAccount') is not None:
            self.customer_account = m.get('CustomerAccount')

        if m.get('CustomerManager') is not None:
            self.customer_manager = m.get('CustomerManager')

        if m.get('CustomerNo') is not None:
            self.customer_no = m.get('CustomerNo')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderSource') is not None:
            self.order_source = m.get('OrderSource')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')

        if m.get('PretaxCost') is not None:
            self.pretax_cost = m.get('PretaxCost')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('TimeToOrder') is not None:
            self.time_to_order = m.get('TimeToOrder')

        return self

