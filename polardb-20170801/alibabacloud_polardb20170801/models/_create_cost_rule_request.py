# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCostRuleRequest(DaraModel):
    def __init__(
        self,
        cache_cost_points_per_million: str = None,
        cache_creation_cost_points_per_million: str = None,
        effective_start_time: str = None,
        effective_target_type: str = None,
        effective_target_value: str = None,
        explicit_cache_cost_points_per_million: str = None,
        gw_cluster_id: str = None,
        image_cost_points_per_count: str = None,
        input_cost_points_per_million: str = None,
        input_token_tiers: str = None,
        model_name: str = None,
        model_service_id: str = None,
        output_cost_points_per_million: str = None,
        region_id: str = None,
        video_cost_points_per_second: str = None,
    ):
        # The cache read cost points per million tokens. Default value: 0.
        self.cache_cost_points_per_million = cache_cost_points_per_million
        # The cache creation cost points per million tokens.
        self.cache_creation_cost_points_per_million = cache_creation_cost_points_per_million
        # The effective start time in the yyyy-MM-dd HH:mm:ss format. If this parameter is not specified, the rule takes effect immediately.
        self.effective_start_time = effective_start_time
        # The effective target type. Valid values: global, consumerGroup, and consumer. Default value: global.
        self.effective_target_type = effective_target_type
        # The effective target value. This parameter is required when the effective target type is not global.
        self.effective_target_value = effective_target_value
        # The explicit cache read cost points per million tokens.
        self.explicit_cache_cost_points_per_million = explicit_cache_cost_points_per_million
        # The gateway instance ID.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # The image input cost points per image.
        self.image_cost_points_per_count = image_cost_points_per_count
        # The input cost points per million tokens. Default value: 0.
        self.input_cost_points_per_million = input_cost_points_per_million
        # The tiered price for input tokens (non-cumulative). The value is a JSON array character string. Each element contains Tier and InputCostPointsPerMillion. Valid values for Tier: "" (default tier), 0-32K, 32K-64K, 64K-128K, 128K-256K, 256K-512K, 512K-1M, and 1M+. Example: [{"Tier":"0-32K","InputCostPointsPerMillion":"1000"},{"Tier":"32K-64K","InputCostPointsPerMillion":"1800"}]. If this parameter is specified, it takes precedence over InputCostPointsPerMillion. An empty array [] is not allowed.
        self.input_token_tiers = input_token_tiers
        # The name of the model, such as gpt-4 or qwen-turbo.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The ID of the model service.
        # 
        # This parameter is required.
        self.model_service_id = model_service_id
        # The output cost points per million tokens. Default value: 0.
        self.output_cost_points_per_million = output_cost_points_per_million
        # The region ID.
        self.region_id = region_id
        # The video input cost points per second.
        self.video_cost_points_per_second = video_cost_points_per_second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_cost_points_per_million is not None:
            result['CacheCostPointsPerMillion'] = self.cache_cost_points_per_million

        if self.cache_creation_cost_points_per_million is not None:
            result['CacheCreationCostPointsPerMillion'] = self.cache_creation_cost_points_per_million

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.effective_target_type is not None:
            result['EffectiveTargetType'] = self.effective_target_type

        if self.effective_target_value is not None:
            result['EffectiveTargetValue'] = self.effective_target_value

        if self.explicit_cache_cost_points_per_million is not None:
            result['ExplicitCacheCostPointsPerMillion'] = self.explicit_cache_cost_points_per_million

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.image_cost_points_per_count is not None:
            result['ImageCostPointsPerCount'] = self.image_cost_points_per_count

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.input_token_tiers is not None:
            result['InputTokenTiers'] = self.input_token_tiers

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.video_cost_points_per_second is not None:
            result['VideoCostPointsPerSecond'] = self.video_cost_points_per_second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostPointsPerMillion') is not None:
            self.cache_cost_points_per_million = m.get('CacheCostPointsPerMillion')

        if m.get('CacheCreationCostPointsPerMillion') is not None:
            self.cache_creation_cost_points_per_million = m.get('CacheCreationCostPointsPerMillion')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('EffectiveTargetType') is not None:
            self.effective_target_type = m.get('EffectiveTargetType')

        if m.get('EffectiveTargetValue') is not None:
            self.effective_target_value = m.get('EffectiveTargetValue')

        if m.get('ExplicitCacheCostPointsPerMillion') is not None:
            self.explicit_cache_cost_points_per_million = m.get('ExplicitCacheCostPointsPerMillion')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ImageCostPointsPerCount') is not None:
            self.image_cost_points_per_count = m.get('ImageCostPointsPerCount')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('InputTokenTiers') is not None:
            self.input_token_tiers = m.get('InputTokenTiers')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VideoCostPointsPerSecond') is not None:
            self.video_cost_points_per_second = m.get('VideoCostPointsPerSecond')

        return self

