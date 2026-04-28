# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBudgetPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeBudgetPoliciesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeBudgetPoliciesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeBudgetPoliciesResponseBodyItems(DaraModel):
    def __init__(
        self,
        alert_threshold_pct: str = None,
        alert_triggered: bool = None,
        budget_dimension_ref_id: str = None,
        budget_dimension_type: str = None,
        budget_points: str = None,
        budget_policy_id: str = None,
        budget_type: str = None,
        exceeded: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        reset_day_of_month: str = None,
        status: str = None,
        used_points: int = None,
    ):
        self.alert_threshold_pct = alert_threshold_pct
        self.alert_triggered = alert_triggered
        self.budget_dimension_ref_id = budget_dimension_ref_id
        self.budget_dimension_type = budget_dimension_type
        self.budget_points = budget_points
        self.budget_policy_id = budget_policy_id
        self.budget_type = budget_type
        self.exceeded = exceeded
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.gw_cluster_id = gw_cluster_id
        self.reset_day_of_month = reset_day_of_month
        self.status = status
        self.used_points = used_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_threshold_pct is not None:
            result['AlertThresholdPct'] = self.alert_threshold_pct

        if self.alert_triggered is not None:
            result['AlertTriggered'] = self.alert_triggered

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

        if self.exceeded is not None:
            result['Exceeded'] = self.exceeded

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.reset_day_of_month is not None:
            result['ResetDayOfMonth'] = self.reset_day_of_month

        if self.status is not None:
            result['Status'] = self.status

        if self.used_points is not None:
            result['UsedPoints'] = self.used_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertThresholdPct') is not None:
            self.alert_threshold_pct = m.get('AlertThresholdPct')

        if m.get('AlertTriggered') is not None:
            self.alert_triggered = m.get('AlertTriggered')

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

        if m.get('Exceeded') is not None:
            self.exceeded = m.get('Exceeded')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ResetDayOfMonth') is not None:
            self.reset_day_of_month = m.get('ResetDayOfMonth')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UsedPoints') is not None:
            self.used_points = m.get('UsedPoints')

        return self

