# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ModifyCostRuleResponseBody(DaraModel):
    def __init__(
        self,
        affected_model_api_ids: List[str] = None,
        cache_cost_points_per_million: str = None,
        cache_creation_cost_points_per_million: str = None,
        cost_rule_id: str = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        effective_target_type: str = None,
        effective_target_value: str = None,
        explicit_cache_cost_points_per_million: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        gw_cluster_id: str = None,
        image_cost_points_per_count: str = None,
        input_cost_points_per_million: str = None,
        input_token_tier: str = None,
        input_token_tiers: List[main_models.ModifyCostRuleResponseBodyInputTokenTiers] = None,
        model_name: str = None,
        model_service_id: str = None,
        model_service_name: str = None,
        output_cost_points_per_million: str = None,
        request_id: str = None,
        video_cost_points_per_second: str = None,
    ):
        # The list of model API IDs affected by the rule.
        self.affected_model_api_ids = affected_model_api_ids
        # The cache read cost points per million tokens.
        self.cache_cost_points_per_million = cache_cost_points_per_million
        # The cache creation cost points per million tokens.
        self.cache_creation_cost_points_per_million = cache_creation_cost_points_per_million
        # The cost rule ID.
        self.cost_rule_id = cost_rule_id
        # The effective end time.
        self.effective_end_time = effective_end_time
        # The effective start time.
        self.effective_start_time = effective_start_time
        # The effective target type. Valid values: global, consumerGroup, and consumer.
        self.effective_target_type = effective_target_type
        # The effective target value. This parameter has a value when the effective target type is not global.
        self.effective_target_value = effective_target_value
        # The explicit cache read cost points per million tokens.
        self.explicit_cache_cost_points_per_million = explicit_cache_cost_points_per_million
        # The creation time.
        self.gmt_created = gmt_created
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the gateway cluster to which the cost rule belongs.
        self.gw_cluster_id = gw_cluster_id
        # The image input cost points per image.
        self.image_cost_points_per_count = image_cost_points_per_count
        # The input cost points per million tokens.
        self.input_cost_points_per_million = input_cost_points_per_million
        # The input token tier. An empty value indicates the default tier.
        self.input_token_tier = input_token_tier
        # The tiered pricing for input tokens (priced by tier, non-cumulative). Each element contains Tier and InputCostPointsPerMillion.
        self.input_token_tiers = input_token_tiers
        # The name of the pricing model.
        self.model_name = model_name
        # The model service ID.
        self.model_service_id = model_service_id
        # The model service name.
        self.model_service_name = model_service_name
        # The output cost points per million tokens.
        self.output_cost_points_per_million = output_cost_points_per_million
        # Id of the request
        self.request_id = request_id
        # The video input cost points per second.
        self.video_cost_points_per_second = video_cost_points_per_second

    def validate(self):
        if self.input_token_tiers:
            for v1 in self.input_token_tiers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_model_api_ids is not None:
            result['AffectedModelApiIds'] = self.affected_model_api_ids

        if self.cache_cost_points_per_million is not None:
            result['CacheCostPointsPerMillion'] = self.cache_cost_points_per_million

        if self.cache_creation_cost_points_per_million is not None:
            result['CacheCreationCostPointsPerMillion'] = self.cache_creation_cost_points_per_million

        if self.cost_rule_id is not None:
            result['CostRuleId'] = self.cost_rule_id

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.effective_target_type is not None:
            result['EffectiveTargetType'] = self.effective_target_type

        if self.effective_target_value is not None:
            result['EffectiveTargetValue'] = self.effective_target_value

        if self.explicit_cache_cost_points_per_million is not None:
            result['ExplicitCacheCostPointsPerMillion'] = self.explicit_cache_cost_points_per_million

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.image_cost_points_per_count is not None:
            result['ImageCostPointsPerCount'] = self.image_cost_points_per_count

        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.input_token_tier is not None:
            result['InputTokenTier'] = self.input_token_tier

        result['InputTokenTiers'] = []
        if self.input_token_tiers is not None:
            for k1 in self.input_token_tiers:
                result['InputTokenTiers'].append(k1.to_map() if k1 else None)

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.model_service_name is not None:
            result['ModelServiceName'] = self.model_service_name

        if self.output_cost_points_per_million is not None:
            result['OutputCostPointsPerMillion'] = self.output_cost_points_per_million

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_cost_points_per_second is not None:
            result['VideoCostPointsPerSecond'] = self.video_cost_points_per_second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedModelApiIds') is not None:
            self.affected_model_api_ids = m.get('AffectedModelApiIds')

        if m.get('CacheCostPointsPerMillion') is not None:
            self.cache_cost_points_per_million = m.get('CacheCostPointsPerMillion')

        if m.get('CacheCreationCostPointsPerMillion') is not None:
            self.cache_creation_cost_points_per_million = m.get('CacheCreationCostPointsPerMillion')

        if m.get('CostRuleId') is not None:
            self.cost_rule_id = m.get('CostRuleId')

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('EffectiveTargetType') is not None:
            self.effective_target_type = m.get('EffectiveTargetType')

        if m.get('EffectiveTargetValue') is not None:
            self.effective_target_value = m.get('EffectiveTargetValue')

        if m.get('ExplicitCacheCostPointsPerMillion') is not None:
            self.explicit_cache_cost_points_per_million = m.get('ExplicitCacheCostPointsPerMillion')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ImageCostPointsPerCount') is not None:
            self.image_cost_points_per_count = m.get('ImageCostPointsPerCount')

        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('InputTokenTier') is not None:
            self.input_token_tier = m.get('InputTokenTier')

        self.input_token_tiers = []
        if m.get('InputTokenTiers') is not None:
            for k1 in m.get('InputTokenTiers'):
                temp_model = main_models.ModifyCostRuleResponseBodyInputTokenTiers()
                self.input_token_tiers.append(temp_model.from_map(k1))

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('ModelServiceName') is not None:
            self.model_service_name = m.get('ModelServiceName')

        if m.get('OutputCostPointsPerMillion') is not None:
            self.output_cost_points_per_million = m.get('OutputCostPointsPerMillion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoCostPointsPerSecond') is not None:
            self.video_cost_points_per_second = m.get('VideoCostPointsPerSecond')

        return self

class ModifyCostRuleResponseBodyInputTokenTiers(DaraModel):
    def __init__(
        self,
        input_cost_points_per_million: str = None,
        tier: str = None,
    ):
        # The input cost points per million tokens for the tier.
        self.input_cost_points_per_million = input_cost_points_per_million
        # The token tier. Valid values: "" (default tier), 0-32K, 32K-64K, 64K-128K, 128K-256K, 256K-512K, 512K-1M, and 1M+.
        self.tier = tier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_cost_points_per_million is not None:
            result['InputCostPointsPerMillion'] = self.input_cost_points_per_million

        if self.tier is not None:
            result['Tier'] = self.tier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputCostPointsPerMillion') is not None:
            self.input_cost_points_per_million = m.get('InputCostPointsPerMillion')

        if m.get('Tier') is not None:
            self.tier = m.get('Tier')

        return self

