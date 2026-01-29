# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceAmortizedCostByConsumePeriodRequest(DaraModel):
    def __init__(
        self,
        amortization_period_filter: List[str] = None,
        bill_owner_id_list: List[str] = None,
        bill_user_id_list: List[str] = None,
        billing_cycle: str = None,
        cost_unit_code: str = None,
        instance_id_list: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        product_detail: str = None,
        subscription_type: str = None,
    ):
        self.amortization_period_filter = amortization_period_filter
        self.bill_owner_id_list = bill_owner_id_list
        self.bill_user_id_list = bill_user_id_list
        # This parameter is required.
        self.billing_cycle = billing_cycle
        self.cost_unit_code = cost_unit_code
        self.instance_id_list = instance_id_list
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.product_detail = product_detail
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amortization_period_filter is not None:
            result['AmortizationPeriodFilter'] = self.amortization_period_filter

        if self.bill_owner_id_list is not None:
            result['BillOwnerIdList'] = self.bill_owner_id_list

        if self.bill_user_id_list is not None:
            result['BillUserIdList'] = self.bill_user_id_list

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

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
        if m.get('AmortizationPeriodFilter') is not None:
            self.amortization_period_filter = m.get('AmortizationPeriodFilter')

        if m.get('BillOwnerIdList') is not None:
            self.bill_owner_id_list = m.get('BillOwnerIdList')

        if m.get('BillUserIdList') is not None:
            self.bill_user_id_list = m.get('BillUserIdList')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

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

