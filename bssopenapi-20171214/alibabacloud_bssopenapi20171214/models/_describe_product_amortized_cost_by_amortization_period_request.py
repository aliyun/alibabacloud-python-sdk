# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeProductAmortizedCostByAmortizationPeriodRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id_list: List[str] = None,
        bill_user_id_list: List[str] = None,
        billing_cycle: str = None,
        consume_period_filter: List[str] = None,
        cost_unit_code: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        product_detail: str = None,
        subscription_type: str = None,
    ):
        # The IDs of resource owners. The resource owner is the account that uses the resources.
        # You can specify a maximum of 10 IDs.
        self.bill_owner_id_list = bill_owner_id_list
        # The IDs of billable accounts. This parameter is used to filter bills by the RAM user who pays for the resources. If you specify this parameter, you can query the bills of the specified RAM user. If you leave this parameter empty, the bills of the current account and all its RAM users are queried.
        # You can specify a maximum of 10 IDs.
        self.bill_user_id_list = bill_user_id_list
        # The amortization month.
        # Format: YYYY-MM.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The filter for billing cycle months.
        # You can specify a maximum of 10 elements.
        self.consume_period_filter = consume_period_filter
        # The code of the cost center.
        self.cost_unit_code = cost_unit_code
        # The maximum number of entries to return. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The token that marks the position to start the query. If you leave this parameter empty, the query starts from the beginning. Set this parameter to the value of NextToken that is returned in the last response to query the next page of results.
        self.next_token = next_token
        # The product code.
        # For more information about how to obtain this parameter, see QueryProductList and DescribeResourcePackageProduct.
        self.product_code = product_code
        # The details of the product.
        self.product_detail = product_detail
        # The subscription type. Valid values:
        # 
        # - Subscription: subscription.
        # 
        # - PayAsYouGo: pay-as-you-go.
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

