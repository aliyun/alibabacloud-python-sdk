# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBudgetPolicyRequest(DaraModel):
    def __init__(
        self,
        alert_threshold_pct: str = None,
        budget_points: str = None,
        budget_policy_id: str = None,
        gw_cluster_id: str = None,
        region_id: str = None,
        reset_day_of_month: str = None,
    ):
        self.alert_threshold_pct = alert_threshold_pct
        self.budget_points = budget_points
        # This parameter is required.
        self.budget_policy_id = budget_policy_id
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.region_id = region_id
        self.reset_day_of_month = reset_day_of_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_threshold_pct is not None:
            result['AlertThresholdPct'] = self.alert_threshold_pct

        if self.budget_points is not None:
            result['BudgetPoints'] = self.budget_points

        if self.budget_policy_id is not None:
            result['BudgetPolicyId'] = self.budget_policy_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_day_of_month is not None:
            result['ResetDayOfMonth'] = self.reset_day_of_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertThresholdPct') is not None:
            self.alert_threshold_pct = m.get('AlertThresholdPct')

        if m.get('BudgetPoints') is not None:
            self.budget_points = m.get('BudgetPoints')

        if m.get('BudgetPolicyId') is not None:
            self.budget_policy_id = m.get('BudgetPolicyId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetDayOfMonth') is not None:
            self.reset_day_of_month = m.get('ResetDayOfMonth')

        return self

