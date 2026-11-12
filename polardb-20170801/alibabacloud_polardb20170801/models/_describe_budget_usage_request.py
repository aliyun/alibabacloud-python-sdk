# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBudgetUsageRequest(DaraModel):
    def __init__(
        self,
        budget_dimension_ref_id: str = None,
        budget_dimension_type: str = None,
        gw_cluster_id: str = None,
        region_id: str = None,
    ):
        # The reference ID of the budget dimension. If BudgetDimensionType is set to Global, set this parameter to Global. If BudgetDimensionType is set to Consumer, set this parameter to the consumer ID returned by DescribeBudgetPolicies, such as consumer-xxx. If BudgetDimensionType is set to ConsumerGroup, set this parameter to the consumer group ID, such as cg-xxx.
        self.budget_dimension_ref_id = budget_dimension_ref_id
        # The budget dimension type. Valid values: Global (global budget), Consumer (consumer budget), and ConsumerGroup (consumer group budget).
        self.budget_dimension_type = budget_dimension_type
        # The ID of the gateway instance to query. This parameter is required. If this parameter is not specified, the API returns InvalidPolarGatewayInstanceId.NotFound (404).
        self.gw_cluster_id = gw_cluster_id
        # The ID of the region where the gateway instance resides.
        self.region_id = region_id

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

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetDimensionRefId') is not None:
            self.budget_dimension_ref_id = m.get('BudgetDimensionRefId')

        if m.get('BudgetDimensionType') is not None:
            self.budget_dimension_type = m.get('BudgetDimensionType')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

