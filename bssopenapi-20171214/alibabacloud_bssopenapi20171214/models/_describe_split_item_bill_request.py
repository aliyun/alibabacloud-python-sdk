# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSplitItemBillRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        instance_id: str = None,
        is_hide_zero_charge: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_id: int = None,
        pip_code: str = None,
        product_code: str = None,
        product_type: str = None,
        split_item_id: str = None,
        subscription_type: str = None,
        tag_filter: List[main_models.DescribeSplitItemBillRequestTagFilter] = None,
    ):
        # The ID of the resource ownership account. The resource ownership account is the account that actually uses the resource.
        self.bill_owner_id = bill_owner_id
        # The billing cycle. Format: YYYY-MM.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only when Granularity is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The granularity at which bills are queried. Valid values:
        # - MONTHLY: monthly. This value corresponds to the monthly bills on the Split Bill page in the User Center.
        # - DAILY: daily. This value corresponds to the daily bills on the Split Bill page in the User Center.
        # 
        # > If you set this parameter to DAILY, you must specify the BillingDate parameter.
        self.granularity = granularity
        # The instance ID.
        self.instance_id = instance_id
        # Specifies whether to filter out bills where both the original price (PretaxGrossAmount) and the payable amount (PretaxAmount) are 0. Valid values:
        # 
        # - false: does not filter out the bills.
        # - true: filters out the bills.
        self.is_hide_zero_charge = is_hide_zero_charge
        # The maximum number of entries to return in the current call. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The token that specifies the position from which the current call starts to read data. The value must be empty or the value of NextToken returned in the previous response. Otherwise, an error occurs. An empty value indicates that the read operation starts from the beginning.
        self.next_token = next_token
        self.owner_id = owner_id
        # The product code. This value is the same as the product code in the bills of the User Center.
        self.pip_code = pip_code
        # The product code.
        self.product_code = product_code
        # The product type.
        self.product_type = product_type
        # The ID of the attached resource.
        self.split_item_id = split_item_id
        # The subscription type. Valid values:
        # 
        # - Subscription: subscription.
        # - PayAsYouGo: pay-as-you-go.
        # 
        # > This parameter must be used together with the ProductCode parameter.
        self.subscription_type = subscription_type
        # The tag filter conditions. Multiple sets of TagValues query conditions are supported. The logical relationship between multiple sets of TagValues conditions is OR.
        self.tag_filter = tag_filter

    def validate(self):
        if self.tag_filter:
            for v1 in self.tag_filter:
                 if v1:
                    v1.validate()

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

        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k1 in self.tag_filter:
                result['TagFilter'].append(k1.to_map() if k1 else None)

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

        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k1 in m.get('TagFilter'):
                temp_model = main_models.DescribeSplitItemBillRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k1))

        return self

class DescribeSplitItemBillRequestTagFilter(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # TagFilter.N is used to query bills that match the specified tags. It consists of a key-value pair. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # - If you specify only TagFilter.N.TagKey, all bills associated with the tag key are returned.
        # - If you specify multiple tag key-value pairs, bills that match any of the tag key-value pairs are returned.
        # - If the tags on a resource change, you can only query the bills generated during the period when the tags were attached to the resource.
        self.tag_key = tag_key
        # TagValues.N is used to query bills that match the specified tag values. It consists of a list of strings. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # - If you specify TagValues.N, you must also specify TagFilter.N.TagKey. Otherwise, the InvalidParameter.TagValues error is reported.
        # - If you specify multiple tag values, bills that match any of the tag values are returned.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

