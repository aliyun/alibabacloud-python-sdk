# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceAmortizedCostByAmortizationPeriodRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id_list: List[str] = None,
        bill_user_id_list: List[str] = None,
        billing_cycle: str = None,
        consume_period_filter: List[str] = None,
        cost_unit_code: str = None,
        instance_id_list: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        product_detail: str = None,
        subscription_type: str = None,
    ):
        # The ID of the member to which the bill belongs. The member ID is used to filter bills. If you specify a value for this parameter, you can query the bills of the specified member. If you leave this parameter empty, the bills of the current account and all members of the current account are queried. You can specify a maximum of 10 IDs.
        self.bill_owner_id_list = bill_owner_id_list
        # The ID of the member that needs to settle the bill. The member ID is used to filter bills. If you specify a value for this parameter, you can query the bills of the specified member account. If you leave this parameter empty, the bills of the current account and all members of the current account are queried by default. You can specify a maximum of 10 IDs.
        self.bill_user_id_list = bill_user_id_list
        # The allocation month. Format: YYYY-MM.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing cycle that is used to filter bills. You can specify a maximum of 10 billing cycles.
        self.consume_period_filter = consume_period_filter
        # The code of the cost center.
        self.cost_unit_code = cost_unit_code
        # The instance ID that is used to filter bills. You can specify multiple instance IDs to query bills of multiple instances. If you leave this parameter empty, the bills of all instances are queried by default. You can specify a maximum of 10 instance IDs.
        self.instance_id_list = instance_id_list
        # The maximum number of entries to return. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The position from which the query starts. The parameter must be left empty or set to the value of the NextToken parameter returned from the last call. Otherwise, an error is returned. If this parameter is left empty, data is queried from the beginning.
        self.next_token = next_token
        # The code of the service. You can obtain the value of this parameter by calling the QueryProductList operation or the DescribeResourcePackageProduct operation.
        self.product_code = product_code
        # The specific service resource.
        self.product_detail = product_detail
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
        if self.bill_owner_id_list is not None:
            result['BillOwnerIdList'] = self.bill_owner_id_list

        if self.bill_user_id_list is not None:
            result['BillUserIdList'] = self.bill_user_id_list

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.consume_period_filter is not None:
            result['ConsumePeriodFilter'] = self.consume_period_filter

        if self.cost_unit_code is not None:
            result['CostUnitCode'] = self.cost_unit_code

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerIdList') is not None:
            self.bill_owner_id_list = m.get('BillOwnerIdList')

        if m.get('BillUserIdList') is not None:
            self.bill_user_id_list = m.get('BillUserIdList')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('ConsumePeriodFilter') is not None:
            self.consume_period_filter = m.get('ConsumePeriodFilter')

        if m.get('CostUnitCode') is not None:
            self.cost_unit_code = m.get('CostUnitCode')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

