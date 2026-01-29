# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryBillOverviewRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The ID of the member. If you specify a value for this parameter, you can query the bills of the specified member. If you leave this parameter empty, the bills of the current account are queried by default.
        self.bill_owner_id = bill_owner_id
        # The billing cycle, in the YYYY-MM format.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method
        # *   PayAsYouGo: the pay-as-you-go billing method
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

