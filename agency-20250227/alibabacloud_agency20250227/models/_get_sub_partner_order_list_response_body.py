# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class GetSubPartnerOrderListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetSubPartnerOrderListResponseBodyData] = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # Status code
        self.code = code
        # Returned data
        self.data = data
        # Message
        self.message = message
        # Page number
        self.page_no = page_no
        # Paging size
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # Indicates whether the operation succeeded
        self.success = success
        # TotalCount indicates the total amount of data under the current request conditions. This parameter is optional and is not returned by default.
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
                temp_model = main_models.GetSubPartnerOrderListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

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

class GetSubPartnerOrderListResponseBodyData(DaraModel):
    def __init__(
        self,
        amount_discount: float = None,
        amount_due: float = None,
        created_at: str = None,
        customer_classification: str = None,
        deducted_amount_by_coupons: float = None,
        discounted_price: float = None,
        order_id: int = None,
        order_status: int = None,
        order_type: str = None,
        paid_at: str = None,
        pay_type: int = None,
        price: float = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        sub_partner_name: str = None,
        sub_partner_uid: int = None,
    ):
        # Order discount
        self.amount_discount = amount_discount
        # Actual payment amount
        self.amount_due = amount_due
        # Creation Time
        self.created_at = created_at
        # Customer classification
        self.customer_classification = customer_classification
        # Coupon amount
        self.deducted_amount_by_coupons = deducted_amount_by_coupons
        # Discounted price
        self.discounted_price = discounted_price
        # Order ID
        self.order_id = order_id
        # Order status:  
        # - 1 Unpaid  
        # - 2 Abandoned  
        # - 3 Paid
        self.order_status = order_status
        # Order type:  
        # - BUY: New purchase  
        # - UPGRADE: Upgrade  
        # - DOWNGRADE: Downgrade  
        # - RENEW: Renewal  
        # - REFUND: Refund  
        # - OTHERS: Others
        self.order_type = order_type
        # Payment Time
        self.paid_at = paid_at
        # Payment type:  
        # 1: Non-agent payment  
        # 2: Agent payment
        self.pay_type = pay_type
        # Original price/List price
        self.price = price
        # Product code
        self.product_code = product_code
        # Product name.
        self.product_name = product_name
        # Opportunity ID
        self.project_id = project_id
        # Sub-partner Name
        self.sub_partner_name = sub_partner_name
        # Secondary partner UID
        self.sub_partner_uid = sub_partner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_discount is not None:
            result['AmountDiscount'] = self.amount_discount

        if self.amount_due is not None:
            result['AmountDue'] = self.amount_due

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.customer_classification is not None:
            result['CustomerClassification'] = self.customer_classification

        if self.deducted_amount_by_coupons is not None:
            result['DeductedAmountByCoupons'] = self.deducted_amount_by_coupons

        if self.discounted_price is not None:
            result['DiscountedPrice'] = self.discounted_price

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.paid_at is not None:
            result['PaidAt'] = self.paid_at

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.price is not None:
            result['Price'] = self.price

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sub_partner_name is not None:
            result['SubPartnerName'] = self.sub_partner_name

        if self.sub_partner_uid is not None:
            result['SubPartnerUid'] = self.sub_partner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountDiscount') is not None:
            self.amount_discount = m.get('AmountDiscount')

        if m.get('AmountDue') is not None:
            self.amount_due = m.get('AmountDue')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('CustomerClassification') is not None:
            self.customer_classification = m.get('CustomerClassification')

        if m.get('DeductedAmountByCoupons') is not None:
            self.deducted_amount_by_coupons = m.get('DeductedAmountByCoupons')

        if m.get('DiscountedPrice') is not None:
            self.discounted_price = m.get('DiscountedPrice')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PaidAt') is not None:
            self.paid_at = m.get('PaidAt')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubPartnerName') is not None:
            self.sub_partner_name = m.get('SubPartnerName')

        if m.get('SubPartnerUid') is not None:
            self.sub_partner_uid = m.get('SubPartnerUid')

        return self

