# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        instance_id: str = None,
        is_billing_item: bool = None,
        is_hide_zero_charge: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_id: int = None,
        pip_code: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The ID of the resource ownership account. The resource ownership account is the account that actually uses the resource.
        self.bill_owner_id = bill_owner_id
        # The billing cycle in the YYYY-MM format. Only the last 18 billing cycles are supported.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only when Granularity is set to DAILY. Format: YYYY-MM-DD.
        # 
        # > The value of BillingDate must be in the same month as the value of BillingCycle. For example, if BillingCycle is set to 2020-03, BillingDate must be set to 2020-03-DD. If the months are inconsistent, the query results are returned based on the time specified by BillingCycle.
        self.billing_date = billing_date
        # The granularity at which bills are queried. Valid values:
        # 
        # - MONTHLY: monthly. The data is consistent with the monthly bills in Expenses and Costs > Bills > Bill Details > Monthly Bills.
        # - DAILY: daily. The data is consistent with the daily bills in Expenses and Costs > Bills > Bill Details > Daily Bills.
        # 
        # > If you select DAILY, you must specify BillingDate.
        self.granularity = granularity
        # The instance ID.
        self.instance_id = instance_id
        # Specifies whether to retrieve data by billable item. Valid values:
        # - false (default): The data is consistent with the instance bills in Expenses and Costs > Bills > Bill Details > Instance Bills.
        # - true: The data is consistent with the billable item bills in Expenses and Costs > Bills > Bill Details > Billable Item Bills.
        self.is_billing_item = is_billing_item
        # Specifies whether to filter out records where both the original price (PretaxGrossAmount) and the payable amount (PretaxAmount) are 0. Valid values:
        # - false
        # - true
        self.is_hide_zero_charge = is_hide_zero_charge
        # The maximum number of data records to read in the current call. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The position from which the current call starts to read data. The value must be empty or set to the NextToken value returned in the previous response. Otherwise, an error occurs. An empty value indicates that the reading starts from the beginning.
        self.next_token = next_token
        self.owner_id = owner_id
        # The product code, which is consistent with the product code in the bills of the User Center.
        self.pip_code = pip_code
        # The product code.
        self.product_code = product_code
        # The product type.
        self.product_type = product_type
        # The subscription type. Valid values:
        # - Subscription: subscription.
        # - PayAsYouGo: pay-as-you-go.
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.is_billing_item is not None:
            result['IsBillingItem'] = self.is_billing_item

        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pip_code is not None:
            result['PipCode'] = self.pip_code

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

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('IsBillingItem') is not None:
            self.is_billing_item = m.get('IsBillingItem')

        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

