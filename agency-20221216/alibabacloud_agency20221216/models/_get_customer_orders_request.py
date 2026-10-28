# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomerOrdersRequest(DaraModel):
    def __init__(
        self,
        customer_account: str = None,
        customer_manager: str = None,
        customer_uid: int = None,
        end_date: str = None,
        order_id: int = None,
        order_source: int = None,
        order_status: int = None,
        order_type: str = None,
        page_no: int = None,
        page_size: int = None,
        product_type: str = None,
        start_date: str = None,
        time_type: int = None,
    ):
        # The customer account.
        self.customer_account = customer_account
        # The account manager.
        self.customer_manager = customer_manager
        # The customer UID.
        self.customer_uid = customer_uid
        # The end time. This parameter is used in combination with TimeType. Format: yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The order ID.
        self.order_id = order_id
        # The order source. Valid values:
        # - 0: Regular customer.
        # - 1: Enterprise customer.
        # - 2: Tier-2 distributor.
        self.order_source = order_source
        # The order status. Valid values:
        # - 1: Unpaid.
        # - 2: Canceled.
        # - 3: Paid.
        self.order_status = order_status
        # The order type. Valid values:
        # - BUY: New purchase.
        # - UPGRADE: Upgrade.
        # - DOWNGRADE: Downgrade.
        # - RENEW: Renewal.
        # - REFUND: Refund.
        # - OTHERS: Others.
        self.order_type = order_type
        # The current page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product detail code.
        self.product_type = product_type
        # The start time. This parameter is used in combination with TimeType. Format: yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The time type used as the basis for the query. This is not a date or time value. Valid values:
        # - 1: Payment time.
        # - 2: Order placement time.
        # 
        # This parameter is required.
        self.time_type = time_type

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

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_source is not None:
            result['OrderSource'] = self.order_source

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAccount') is not None:
            self.customer_account = m.get('CustomerAccount')

        if m.get('CustomerManager') is not None:
            self.customer_manager = m.get('CustomerManager')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderSource') is not None:
            self.order_source = m.get('OrderSource')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        return self

