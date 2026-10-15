# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInstanceBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        is_billing_item: bool = None,
        is_hide_zero_charge: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The ID of the account that owns the resources. This account is the actual user of the resources.
        self.bill_owner_id = bill_owner_id
        # The billing cycle in YYYY-MM format. Data from the last 18 months is supported.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only when the **Granularity** parameter is set to DAILY. The value must be in the YYYY-MM-DD format.
        self.billing_date = billing_date
        # The granularity at which to query bills. Valid values:
        # 
        # - MONTHLY: queries bills by month. The data is consistent with the bill details on the Billing Cycle tab of the Bills page in the User Center.
        # 
        # - DAILY: queries bills by day. The data is consistent with the bill details on the By Day tab of the Bills page in the User Center.
        # 
        # If you set this parameter to DAILY, you must also specify the **BillingDate** parameter.
        self.granularity = granularity
        # Specifies whether to query data by billable item.
        # 
        # - false: The data is consistent with the bill details on the Instance tab of the Bills page in the User Center.
        # 
        # - true: The data is consistent with the bill details on the Billable Item tab of the Bills page in the User Center.
        # 
        # Default value: false.
        self.is_billing_item = is_billing_item
        # Specifies whether to filter out bills for which the pretax gross amount (**PretaxGrossAmount**) and pretax amount (**PretaxAmount**) are both 0. Valid values:
        # 
        # - false.
        # 
        # - true.
        self.is_hide_zero_charge = is_hide_zero_charge
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The code of the product.
        self.product_code = product_code
        # The type of the product. Required when the ProductCode parameter is set to the code of an Alibaba Cloud Marketplace product.
        self.product_type = product_type
        # The subscription type. Valid values:
        # 
        # - Subscription: subscription.
        # 
        # - PayAsYouGo: pay-as-you-go.
        # 
        # > This parameter must be used with the **ProductCode** parameter.
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

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.is_billing_item is not None:
            result['IsBillingItem'] = self.is_billing_item

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('IsBillingItem') is not None:
            self.is_billing_item = m.get('IsBillingItem')

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

        return self

