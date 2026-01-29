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
        # The ID of the member. If you specify this parameter, the bills of the member are queried. If you do not specify this parameter, the bills of the current account are queried by default.
        self.bill_owner_id = bill_owner_id
        # The billing cycle. Specify the parameter in the YYYY-MM format.
        # Only the latest 18 month billing cycle is supported.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only when the Granularity parameter is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The granularity at which bills are queried. Valid values:
        # 
        # *   MONTHLY: queries bills on a monthly basis. The data that you query is the same as the data searched by instances on the Billing Details tab of the Bill Details page in the User Center console.
        # *   DAILY: queries bills on a daily basis. The data that you query is the same as the data searched by days on the Billing Details tab of the Bill Details page in the User Center console.
        # 
        # The BillingDate parameter is required if you set the Granularity parameter to DAILY.
        self.granularity = granularity
        # The ID of the instance.
        self.instance_id = instance_id
        # Specifies whether to query data by billable items. Valid values:
        # 
        # *   false: The data that you query is the same as the data searched by instances on the Billing Details tab of the Bill Details page in the User Center console.
        # *   true: The data that you query is the same as the data searched by billable items on the Billing Details tab of the Bill Details page in the User Center console.
        # 
        # Default value: false.
        self.is_billing_item = is_billing_item
        # Specifies whether to filter bills if both the pretax gross amount and pretax amount are 0. Valid values:
        # 
        # *   false: does not filter bills.
        # *   true: filters bills.
        self.is_hide_zero_charge = is_hide_zero_charge
        # The maximum number of entries to return. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The token that is used to indicate the position where the results for the current call start. The parameter must be left empty or set to the value of the NextToken parameter that is returned from the last call. Otherwise, an error is returned. If the parameter is left empty, data is queried from the first item.
        self.next_token = next_token
        self.owner_id = owner_id
        # The code of the service. The code is the same as that in Cost Center.
        self.pip_code = pip_code
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method.
        # *   PayAsYouGo: the pay-as-you-go billing method.
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

