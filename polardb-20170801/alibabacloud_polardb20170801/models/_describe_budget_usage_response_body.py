# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBudgetUsageResponseBody(DaraModel):
    def __init__(
        self,
        alert_triggered: str = None,
        dimension_ref_id: str = None,
        dimension_type: str = None,
        exceeded: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        policies: List[main_models.DescribeBudgetUsageResponseBodyPolicies] = None,
        request_id: str = None,
        used_points: str = None,
        window_end_time: str = None,
        window_start_time: str = None,
    ):
        # Indicates whether a budget alert is triggered.
        self.alert_triggered = alert_triggered
        # The dimension reference ID of the current budget.
        self.dimension_ref_id = dimension_ref_id
        # The dimension type of the current budget.
        self.dimension_type = dimension_type
        # Indicates whether the budget is exceeded.
        self.exceeded = exceeded
        # The creation time of the budget usage record, in RFC 3339 UTC format.
        self.gmt_created = gmt_created
        # The time when the budget usage record was last modified, in RFC 3339 UTC format.
        self.gmt_modified = gmt_modified
        # The ID of the gateway instance.
        self.gw_cluster_id = gw_cluster_id
        # The list of associated budget policies.
        self.policies = policies
        # The request ID.
        self.request_id = request_id
        # The number of budget points used in the current statistical window.
        self.used_points = used_points
        # The end time of the budget statistical window, in RFC 3339 UTC format.
        self.window_end_time = window_end_time
        # The start time of the budget statistical window, in RFC 3339 UTC format.
        self.window_start_time = window_start_time

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_triggered is not None:
            result['AlertTriggered'] = self.alert_triggered

        if self.dimension_ref_id is not None:
            result['DimensionRefId'] = self.dimension_ref_id

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

        if self.exceeded is not None:
            result['Exceeded'] = self.exceeded

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.used_points is not None:
            result['UsedPoints'] = self.used_points

        if self.window_end_time is not None:
            result['WindowEndTime'] = self.window_end_time

        if self.window_start_time is not None:
            result['WindowStartTime'] = self.window_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTriggered') is not None:
            self.alert_triggered = m.get('AlertTriggered')

        if m.get('DimensionRefId') is not None:
            self.dimension_ref_id = m.get('DimensionRefId')

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        if m.get('Exceeded') is not None:
            self.exceeded = m.get('Exceeded')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeBudgetUsageResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsedPoints') is not None:
            self.used_points = m.get('UsedPoints')

        if m.get('WindowEndTime') is not None:
            self.window_end_time = m.get('WindowEndTime')

        if m.get('WindowStartTime') is not None:
            self.window_start_time = m.get('WindowStartTime')

        return self

class DescribeBudgetUsageResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        alert_threshold_pct: str = None,
        budget_dimension_ref_id: str = None,
        budget_dimension_type: str = None,
        budget_points: str = None,
        budget_policy_id: str = None,
        budget_type: str = None,
        reset_day_of_month: str = None,
        status: str = None,
    ):
        # The usage percentage that triggers a budget alert.
        self.alert_threshold_pct = alert_threshold_pct
        # The reference ID of the budget dimension to which the policy applies.
        self.budget_dimension_ref_id = budget_dimension_ref_id
        # The budget dimension type to which the policy applies.
        self.budget_dimension_type = budget_dimension_type
        # The number of budget points configured in the policy.
        self.budget_points = budget_points
        # The ID of the budget policy.
        self.budget_policy_id = budget_policy_id
        # The budget type.
        self.budget_type = budget_type
        # The day of the month on which the budget is reset. For example, 1 indicates the first day of each month.
        self.reset_day_of_month = reset_day_of_month
        # The status of the budget policy.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_threshold_pct is not None:
            result['AlertThresholdPct'] = self.alert_threshold_pct

        if self.budget_dimension_ref_id is not None:
            result['BudgetDimensionRefId'] = self.budget_dimension_ref_id

        if self.budget_dimension_type is not None:
            result['BudgetDimensionType'] = self.budget_dimension_type

        if self.budget_points is not None:
            result['BudgetPoints'] = self.budget_points

        if self.budget_policy_id is not None:
            result['BudgetPolicyId'] = self.budget_policy_id

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.reset_day_of_month is not None:
            result['ResetDayOfMonth'] = self.reset_day_of_month

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertThresholdPct') is not None:
            self.alert_threshold_pct = m.get('AlertThresholdPct')

        if m.get('BudgetDimensionRefId') is not None:
            self.budget_dimension_ref_id = m.get('BudgetDimensionRefId')

        if m.get('BudgetDimensionType') is not None:
            self.budget_dimension_type = m.get('BudgetDimensionType')

        if m.get('BudgetPoints') is not None:
            self.budget_points = m.get('BudgetPoints')

        if m.get('BudgetPolicyId') is not None:
            self.budget_policy_id = m.get('BudgetPolicyId')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('ResetDayOfMonth') is not None:
            self.reset_day_of_month = m.get('ResetDayOfMonth')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

