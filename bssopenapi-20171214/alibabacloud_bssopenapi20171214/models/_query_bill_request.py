# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        is_display_local_currency: bool = None,
        is_hide_zero_charge: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        type: str = None,
    ):
        # The ID of the member.
        self.bill_owner_id = bill_owner_id
        # The billing cycle, in the YYYY-MM format.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # Specifies whether to display local currency information in bills. The parameter will be discontinued.
        self.is_display_local_currency = is_display_local_currency
        # Specifies whether to filter out a bill whose pretax gross amount is 0. By default, a bill whose pretax gross amount is 0 is not filtered out. Valid values:
        # 
        # *   true: filters out a bill whose pretax gross amount is 0.
        # *   false: does not filter out a bill whose pretax gross amount is 0.
        self.is_hide_zero_charge = is_hide_zero_charge
        self.owner_id = owner_id
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription
        # *   PayAsYouGo
        # 
        # This parameter must be used together with the ProductCode parameter.
        self.subscription_type = subscription_type
        # The type of the bill. Valid values:
        # 
        # *   SubscriptionOrder
        # *   PayAsYouGoBill
        # *   Refund
        # *   Adjustment
        self.type = type

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

        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency

        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')

        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

