# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCostRuleRequest(DaraModel):
    def __init__(
        self,
        cache_cost_points_per_million: str = None,
        cost_rule_id: str = None,
        gw_cluster_id: str = None,
        input_cost_points_per_million: str = None,
        model_name: str = None,
        model_service_id: str = None,
        output_cost_points_per_million: str = None,
        region_id: str = None,
    ):
        self.cache_cost_points_per_million = cache_cost_points_per_million
        # This parameter is required.
        self.cost_rule_id = cost_rule_id
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.input_cost_points_per_million = input_cost_points_per_million
        # This parameter is required.
        self.model_name = model_name
        # This parameter is required.
        self.model_service_id = model_service_id
        self.output_cost_points_per_million = output_cost_points_per_million
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_cost_points_per_million is not None:
            result['CacheCostPointsPerMillion'] = self.cache_cost_points_per_million

        if self.cost_rule_id is not None:
            result['CostRuleId'] = self.cost_rule_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostPointsPerMillion') is not None:
            self.cache_cost_points_per_million = m.get('CacheCostPointsPerMillion')

        if m.get('CostRuleId') is not None:
            self.cost_rule_id = m.get('CostRuleId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

