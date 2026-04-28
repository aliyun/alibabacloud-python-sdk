# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBudgetPoliciesRequest(DaraModel):
    def __init__(
        self,
        budget_dimension_ref_id: str = None,
        budget_dimension_type: str = None,
        budget_policy_id: str = None,
        gw_cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        status: str = None,
    ):
        self.budget_dimension_ref_id = budget_dimension_ref_id
        self.budget_dimension_type = budget_dimension_type
        self.budget_policy_id = budget_policy_id
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget_dimension_ref_id is not None:
            result['BudgetDimensionRefId'] = self.budget_dimension_ref_id

        if self.budget_dimension_type is not None:
            result['BudgetDimensionType'] = self.budget_dimension_type

        if self.budget_policy_id is not None:
            result['BudgetPolicyId'] = self.budget_policy_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetDimensionRefId') is not None:
            self.budget_dimension_ref_id = m.get('BudgetDimensionRefId')

        if m.get('BudgetDimensionType') is not None:
            self.budget_dimension_type = m.get('BudgetDimensionType')

        if m.get('BudgetPolicyId') is not None:
            self.budget_policy_id = m.get('BudgetPolicyId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

