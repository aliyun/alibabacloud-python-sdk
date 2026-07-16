# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from darabonba.model import DaraModel

class DescribeOrderForIsvResponseBody(DaraModel):
    def __init__(
        self,
        account_quantity: int = None,
        ali_uid: int = None,
        components: Any = None,
        coupon_price: float = None,
        created_on: int = None,
        instance_ids: List[str] = None,
        order_id: int = None,
        order_status: str = None,
        order_type: str = None,
        original_price: float = None,
        paid_on: int = None,
        pay_status: str = None,
        payment_price: float = None,
        period_type: str = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        quantity: int = None,
        request_id: str = None,
        total_price: float = None,
    ):
        self.account_quantity = account_quantity
        self.ali_uid = ali_uid
        self.components = components
        self.coupon_price = coupon_price
        self.created_on = created_on
        # List
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.original_price = original_price
        self.paid_on = paid_on
        self.pay_status = pay_status
        self.payment_price = payment_price
        self.period_type = period_type
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.quantity = quantity
        self.request_id = request_id
        self.total_price = total_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.components is not None:
            result['Components'] = self.components

        if self.coupon_price is not None:
            result['CouponPrice'] = self.coupon_price

        if self.created_on is not None:
            result['CreatedOn'] = self.created_on

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.paid_on is not None:
            result['PaidOn'] = self.paid_on

        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status

        if self.payment_price is not None:
            result['PaymentPrice'] = self.payment_price

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_price is not None:
            result['TotalPrice'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Components') is not None:
            self.components = m.get('Components')

        if m.get('CouponPrice') is not None:
            self.coupon_price = m.get('CouponPrice')

        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('PaidOn') is not None:
            self.paid_on = m.get('PaidOn')

        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')

        if m.get('PaymentPrice') is not None:
            self.payment_price = m.get('PaymentPrice')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')

        return self

