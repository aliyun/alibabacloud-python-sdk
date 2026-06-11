# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSubPartnerOrderListRequest(DaraModel):
    def __init__(
        self,
        order_create_after: int = None,
        order_create_before: int = None,
        order_id: int = None,
        order_pay_after: int = None,
        order_pay_before: int = None,
        order_status: int = None,
        order_type_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        pay_amount_after: int = None,
        pay_amount_before: int = None,
        pay_type: int = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        sub_partner_name: str = None,
        sub_partner_uid: int = None,
    ):
        # The UNIX timestamp of the start time for order creation. The time range must not exceed six months.  
        # The time range for order creation and the time range for order payment cannot both be empty.
        self.order_create_after = order_create_after
        # The UNIX timestamp of the end time for order creation. The time range must not exceed six months.  
        # The time range for order creation and the time range for order payment cannot both be empty.
        self.order_create_before = order_create_before
        # Order ID
        self.order_id = order_id
        # The UNIX timestamp of the start time for order payment. The time range must not exceed six months.  
        # The time range for order creation and the time range for order payment cannot both be empty.
        self.order_pay_after = order_pay_after
        # UNIX timestamp of the order payment deadline. The time range cannot exceed six months.
        # The time range for order creation and the time range for order payment cannot both be empty.
        self.order_pay_before = order_pay_before
        # Order status. Valid values:
        # 1: Unpaid
        # 2: Paid
        # 3: Canceled
        self.order_status = order_status
        # List of order types.
        # Valid order types include: BUY, UPGRADE, DOWNGRADE, RENEW, REFUND, OTHERS
        self.order_type_list = order_type_list
        # Page number
        # 
        # This parameter is required.
        self.page_no = page_no
        # Page size
        # 
        # This parameter is required.
        self.page_size = page_size
        # Minimum paid amount
        self.pay_amount_after = pay_amount_after
        # Maximum paid amount
        self.pay_amount_before = pay_amount_before
        # Payment Type:  
        # 1: Non-agent payment  
        # 2: Agent payment
        self.pay_type = pay_type
        # Product code
        self.product_code = product_code
        # Product Name
        self.product_name = product_name
        # Opportunity ID
        self.project_id = project_id
        # Sub-partner name
        self.sub_partner_name = sub_partner_name
        # Sub-partner UID
        self.sub_partner_uid = sub_partner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_create_after is not None:
            result['OrderCreateAfter'] = self.order_create_after

        if self.order_create_before is not None:
            result['OrderCreateBefore'] = self.order_create_before

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_pay_after is not None:
            result['OrderPayAfter'] = self.order_pay_after

        if self.order_pay_before is not None:
            result['OrderPayBefore'] = self.order_pay_before

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type_list is not None:
            result['OrderTypeList'] = self.order_type_list

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_amount_after is not None:
            result['PayAmountAfter'] = self.pay_amount_after

        if self.pay_amount_before is not None:
            result['PayAmountBefore'] = self.pay_amount_before

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

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
        if m.get('OrderCreateAfter') is not None:
            self.order_create_after = m.get('OrderCreateAfter')

        if m.get('OrderCreateBefore') is not None:
            self.order_create_before = m.get('OrderCreateBefore')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderPayAfter') is not None:
            self.order_pay_after = m.get('OrderPayAfter')

        if m.get('OrderPayBefore') is not None:
            self.order_pay_before = m.get('OrderPayBefore')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderTypeList') is not None:
            self.order_type_list = m.get('OrderTypeList')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayAmountAfter') is not None:
            self.pay_amount_after = m.get('PayAmountAfter')

        if m.get('PayAmountBefore') is not None:
            self.pay_amount_before = m.get('PayAmountBefore')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

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

