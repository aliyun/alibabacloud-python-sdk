# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOrdersRequest(DaraModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        order_type: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        payment_status: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The end time of the period during which the orders were created. By default, orders within the last hour are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.create_time_end = create_time_end
        # The start time of the period during which the orders were created. By default, orders within the last hour are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.create_time_start = create_time_start
        # The type of the order. Valid values:
        # 
        # *   New: purchases an instance.
        # *   Renew: renews an instance.
        # *   Upgrade: upgrades the configurations of an instance.
        # *   Refund: applies for a refund.
        self.order_type = order_type
        self.owner_id = owner_id
        # The page number of the page to return.
        self.page_num = page_num
        # The number of entries to return per page.
        self.page_size = page_size
        # The status of payment. Valid values for a non-refund order:
        # 
        # *   Unpaid: The order is not paid.
        # *   Paid: The order is paid.
        # *   Cancelled: The order is canceled.
        # 
        # > : You can set this parameter to NULL for a refund order.
        self.payment_status = payment_status
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

