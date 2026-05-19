# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCostByCostCenterRequest(DaraModel):
    def __init__(
        self,
        billing_month: int = None,
        display_zero_amount_bills: bool = None,
        group_by_cost_center_level: bool = None,
        metrics: str = None,
        owner_account_id: int = None,
    ):
        # This parameter is required.
        self.billing_month = billing_month
        self.display_zero_amount_bills = display_zero_amount_bills
        self.group_by_cost_center_level = group_by_cost_center_level
        # This parameter is required.
        self.metrics = metrics
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_month is not None:
            result['BillingMonth'] = self.billing_month

        if self.display_zero_amount_bills is not None:
            result['DisplayZeroAmountBills'] = self.display_zero_amount_bills

        if self.group_by_cost_center_level is not None:
            result['GroupByCostCenterLevel'] = self.group_by_cost_center_level

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingMonth') is not None:
            self.billing_month = m.get('BillingMonth')

        if m.get('DisplayZeroAmountBills') is not None:
            self.display_zero_amount_bills = m.get('DisplayZeroAmountBills')

        if m.get('GroupByCostCenterLevel') is not None:
            self.group_by_cost_center_level = m.get('GroupByCostCenterLevel')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        return self

