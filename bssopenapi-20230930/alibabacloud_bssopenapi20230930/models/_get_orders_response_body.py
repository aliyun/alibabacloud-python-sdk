# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetOrdersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetOrdersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetOrdersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOrdersResponseBodyData(DaraModel):
    def __init__(
        self,
        host_name: str = None,
        order_list: main_models.GetOrdersResponseBodyDataOrderList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.host_name = host_name
        self.order_list = order_list
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('OrderList') is not None:
            temp_model = main_models.GetOrdersResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m.get('OrderList'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOrdersResponseBodyDataOrderList(DaraModel):
    def __init__(
        self,
        order: List[main_models.GetOrdersResponseBodyDataOrderListOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for v1 in self.order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Order'] = []
        if self.order is not None:
            for k1 in self.order:
                result['Order'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k1 in m.get('Order'):
                temp_model = main_models.GetOrdersResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k1))

        return self

class GetOrdersResponseBodyDataOrderListOrder(DaraModel):
    def __init__(
        self,
        after_tax_amount: str = None,
        commodity_code: str = None,
        create_time: str = None,
        currency: str = None,
        order_id: str = None,
        order_type: str = None,
        payment_currency: str = None,
        payment_status: str = None,
        payment_time: str = None,
        pretax_amount: str = None,
        pretax_amount_local: str = None,
        pretax_gross_amount: str = None,
        product_code: str = None,
        product_type: str = None,
        related_order_id: str = None,
        subscription_type: str = None,
        tax: str = None,
    ):
        self.after_tax_amount = after_tax_amount
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.currency = currency
        self.order_id = order_id
        self.order_type = order_type
        self.payment_currency = payment_currency
        self.payment_status = payment_status
        self.payment_time = payment_time
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.pretax_gross_amount = pretax_gross_amount
        self.product_code = product_code
        self.product_type = product_type
        self.related_order_id = related_order_id
        self.subscription_type = subscription_type
        self.tax = tax

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency

        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status

        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.tax is not None:
            result['Tax'] = self.tax

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')

        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')

        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        return self

