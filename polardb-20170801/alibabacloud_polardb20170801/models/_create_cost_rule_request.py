# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCostRuleRequest(DaraModel):
    def __init__(
        self,
        cache_cost_points_per_million: str = None,
        effective_target_type: str = None,
        effective_target_value: str = None,
        gw_cluster_id: str = None,
        input_cost_points_per_million: str = None,
        model_name: str = None,
        model_service_id: str = None,
        output_cost_points_per_million: str = None,
        region_id: str = None,
    ):
        # The cost points per million cached tokens. Default value: 0.
        self.cache_cost_points_per_million = cache_cost_points_per_million
        # The effective target type. Valid values:
        # 
        # - global
        # - consumerGroup
        # - consumer
        # 
        # Default value: global.
        self.effective_target_type = effective_target_type
        # The effective target value. This parameter is required when EffectiveTargetType is not set to global.
        self.effective_target_value = effective_target_value
        # The gateway instance ID.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # The cost points per million input tokens. Default value: 0.
        self.input_cost_points_per_million = input_cost_points_per_million
        # The model name, such as gpt-4 or qwen-turbo.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model service ID.
        # 
        # This parameter is required.
        self.model_service_id = model_service_id
        # The cost points per million output tokens. Default value: 0.
        self.output_cost_points_per_million = output_cost_points_per_million
        # The region ID.
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

        if self.effective_target_type is not None:
            result['EffectiveTargetType'] = self.effective_target_type

        if self.effective_target_value is not None:
            result['EffectiveTargetValue'] = self.effective_target_value

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

        if m.get('EffectiveTargetType') is not None:
            self.effective_target_type = m.get('EffectiveTargetType')

        if m.get('EffectiveTargetValue') is not None:
            self.effective_target_value = m.get('EffectiveTargetValue')

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

