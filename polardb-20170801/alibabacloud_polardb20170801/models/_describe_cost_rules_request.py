# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCostRulesRequest(DaraModel):
    def __init__(
        self,
        cost_rule_id: str = None,
        effective_target_type: str = None,
        effective_target_value: str = None,
        gw_cluster_id: str = None,
        input_token_tier: str = None,
        model_name: str = None,
        model_service_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the cost rule.
        self.cost_rule_id = cost_rule_id
        # The effective target type used to filter the results. Valid values: global, consumerGroup, and consumer.
        self.effective_target_type = effective_target_type
        # The effective target value used to filter the results.
        self.effective_target_value = effective_target_value
        # The gateway instance ID.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # The input token tier used to filter the results. Returns rules that include this tier. Valid values: 0-32K, 32K-64K, 64K-128K, 128K-256K, 256K-512K, 512K-1M, and 1M+.
        self.input_token_tier = input_token_tier
        # The name of the model, such as gpt-4 or qwen-turbo.
        self.model_name = model_name
        # The ID of the model service.
        self.model_service_id = model_service_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # * **30**
        # * **50**
        # * **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_rule_id is not None:
            result['CostRuleId'] = self.cost_rule_id

        if self.effective_target_type is not None:
            result['EffectiveTargetType'] = self.effective_target_type

        if self.effective_target_value is not None:
            result['EffectiveTargetValue'] = self.effective_target_value

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.input_token_tier is not None:
            result['InputTokenTier'] = self.input_token_tier

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostRuleId') is not None:
            self.cost_rule_id = m.get('CostRuleId')

        if m.get('EffectiveTargetType') is not None:
            self.effective_target_type = m.get('EffectiveTargetType')

        if m.get('EffectiveTargetValue') is not None:
            self.effective_target_value = m.get('EffectiveTargetValue')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('InputTokenTier') is not None:
            self.input_token_tier = m.get('InputTokenTier')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

