# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticStrengthResponseBody(DaraModel):
    def __init__(
        self,
        elastic_strength: str = None,
        elastic_strength_models: List[main_models.DescribeElasticStrengthResponseBodyElasticStrengthModels] = None,
        request_id: str = None,
        resource_pools: List[main_models.DescribeElasticStrengthResponseBodyResourcePools] = None,
        total_strength: float = None,
    ):
        # The elastic strength of the current scaling group. Valid values:
        # 
        # - Strong: high elastic strength.
        # 
        # - Medium: medium elastic strength.
        # 
        # - Weak: weak elastic strength.
        self.elastic_strength = elastic_strength
        # An array of elastic strength details, returned when the API call targets multiple scaling groups.
        self.elastic_strength_models = elastic_strength_models
        # The request ID.
        self.request_id = request_id
        # An array of resource pools. This parameter is returned when the API call targets a single scaling group.
        self.resource_pools = resource_pools
        # The total elastic strength of the scaling group. The strength is the sum of scores from all configured instance type and zone combinations. Each combination is scored from 0 (low strength) to 1 (high strength) based on resource availability.>Warning:  This parameter is deprecated.
        self.total_strength = total_strength

    def validate(self):
        if self.elastic_strength_models:
            for v1 in self.elastic_strength_models:
                 if v1:
                    v1.validate()
        if self.resource_pools:
            for v1 in self.resource_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_strength is not None:
            result['ElasticStrength'] = self.elastic_strength

        result['ElasticStrengthModels'] = []
        if self.elastic_strength_models is not None:
            for k1 in self.elastic_strength_models:
                result['ElasticStrengthModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcePools'] = []
        if self.resource_pools is not None:
            for k1 in self.resource_pools:
                result['ResourcePools'].append(k1.to_map() if k1 else None)

        if self.total_strength is not None:
            result['TotalStrength'] = self.total_strength

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticStrength') is not None:
            self.elastic_strength = m.get('ElasticStrength')

        self.elastic_strength_models = []
        if m.get('ElasticStrengthModels') is not None:
            for k1 in m.get('ElasticStrengthModels'):
                temp_model = main_models.DescribeElasticStrengthResponseBodyElasticStrengthModels()
                self.elastic_strength_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_pools = []
        if m.get('ResourcePools') is not None:
            for k1 in m.get('ResourcePools'):
                temp_model = main_models.DescribeElasticStrengthResponseBodyResourcePools()
                self.resource_pools.append(temp_model.from_map(k1))

        if m.get('TotalStrength') is not None:
            self.total_strength = m.get('TotalStrength')

        return self

class DescribeElasticStrengthResponseBodyResourcePools(DaraModel):
    def __init__(
        self,
        code: str = None,
        elastic_strength: str = None,
        instance_type: str = None,
        inventory_health: main_models.DescribeElasticStrengthResponseBodyResourcePoolsInventoryHealth = None,
        msg: str = None,
        status: str = None,
        strength: float = None,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The error code returned when the elastic strength is 0.
        self.code = code
        # The elastic strength of the resource pool, which is based on its inventory health and current stock. Valid values:
        # 
        # - Strong: high elastic strength.
        # 
        # - Medium: medium elastic strength.
        # 
        # - Weak: weak elastic strength.
        self.elastic_strength = elastic_strength
        # The instance type of the resource pool.
        self.instance_type = instance_type
        # The inventory health.
        self.inventory_health = inventory_health
        # The error message returned when the elastic strength is 0.
        self.msg = msg
        # The availability of the resource pool. Valid values:
        # 
        # - Available: The resource pool is available.
        # 
        # - Unavailable: The resource pool is unavailable. This can occur if the instance type is not deployed in the zone, has insufficient inventory, or does not meet other constraints.
        self.status = status
        # The elastic strength of the resource pool.
        self.strength = strength
        # The VSwitches in the zone of the resource pool.
        self.v_switch_ids = v_switch_ids
        # The zone ID of the resource pool.
        self.zone_id = zone_id

    def validate(self):
        if self.inventory_health:
            self.inventory_health.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.elastic_strength is not None:
            result['ElasticStrength'] = self.elastic_strength

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.inventory_health is not None:
            result['InventoryHealth'] = self.inventory_health.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.strength is not None:
            result['Strength'] = self.strength

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ElasticStrength') is not None:
            self.elastic_strength = m.get('ElasticStrength')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InventoryHealth') is not None:
            temp_model = main_models.DescribeElasticStrengthResponseBodyResourcePoolsInventoryHealth()
            self.inventory_health = temp_model.from_map(m.get('InventoryHealth'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strength') is not None:
            self.strength = m.get('Strength')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeElasticStrengthResponseBodyResourcePoolsInventoryHealth(DaraModel):
    def __init__(
        self,
        adequacy_score: int = None,
        health_score: int = None,
        hot_score: int = None,
        supply_score: int = None,
    ):
        # The adequacy score.
        # 
        # Valid values: 0 to 3.
        self.adequacy_score = adequacy_score
        # The health score.
        # 
        # - A score from 5 to 6 indicates high confidence in supply.
        # 
        # - A score from 1 to 4 indicates that supply is not guaranteed. Consider making on-demand reservations.
        # 
        # - A score from -3 to 0 indicates a supply health alert. Consider using a different instance type.
        # 
        # The health score is calculated using the formula: `HealthScore` = `AdequacyScore` + `SupplyScore` - `HotScore`.
        self.health_score = health_score
        # The hot score.
        # 
        # Valid values: 0 to 3.
        self.hot_score = hot_score
        # The supply score.
        # 
        # Valid values: 0 to 3.
        self.supply_score = supply_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adequacy_score is not None:
            result['AdequacyScore'] = self.adequacy_score

        if self.health_score is not None:
            result['HealthScore'] = self.health_score

        if self.hot_score is not None:
            result['HotScore'] = self.hot_score

        if self.supply_score is not None:
            result['SupplyScore'] = self.supply_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdequacyScore') is not None:
            self.adequacy_score = m.get('AdequacyScore')

        if m.get('HealthScore') is not None:
            self.health_score = m.get('HealthScore')

        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')

        if m.get('SupplyScore') is not None:
            self.supply_score = m.get('SupplyScore')

        return self

class DescribeElasticStrengthResponseBodyElasticStrengthModels(DaraModel):
    def __init__(
        self,
        elastic_strength: str = None,
        resource_pools: List[main_models.DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePools] = None,
        scaling_group_id: str = None,
        total_strength: float = None,
    ):
        # The elastic strength of the current scaling group. Valid values:
        # 
        # - Strong: high elastic strength.
        # 
        # - Medium: medium elastic strength.
        # 
        # - Weak: weak elastic strength.
        self.elastic_strength = elastic_strength
        # Details of the resource pools within the scaling group.
        self.resource_pools = resource_pools
        # The scaling group ID.
        self.scaling_group_id = scaling_group_id
        # The total elastic strength of the scaling group. The strength is the sum of scores from all configured instance type and zone combinations. Each combination is scored from 0 (low strength) to 1 (high strength) based on resource availability.>Warning:  This parameter is deprecated.
        self.total_strength = total_strength

    def validate(self):
        if self.resource_pools:
            for v1 in self.resource_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_strength is not None:
            result['ElasticStrength'] = self.elastic_strength

        result['ResourcePools'] = []
        if self.resource_pools is not None:
            for k1 in self.resource_pools:
                result['ResourcePools'].append(k1.to_map() if k1 else None)

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.total_strength is not None:
            result['TotalStrength'] = self.total_strength

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticStrength') is not None:
            self.elastic_strength = m.get('ElasticStrength')

        self.resource_pools = []
        if m.get('ResourcePools') is not None:
            for k1 in m.get('ResourcePools'):
                temp_model = main_models.DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePools()
                self.resource_pools.append(temp_model.from_map(k1))

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('TotalStrength') is not None:
            self.total_strength = m.get('TotalStrength')

        return self

class DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePools(DaraModel):
    def __init__(
        self,
        code: str = None,
        elastic_strength: str = None,
        instance_type: str = None,
        inventory_health: main_models.DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePoolsInventoryHealth = None,
        msg: str = None,
        status: str = None,
        strength: float = None,
        v_switch_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The error code returned when the elastic strength is 0.
        self.code = code
        # The elastic strength of the resource pool, which is based on its inventory health and current stock. Valid values:
        # 
        # - Strong: high elastic strength.
        # 
        # - Medium: medium elastic strength.
        # 
        # - Weak: weak elastic strength.
        self.elastic_strength = elastic_strength
        # The instance type of the resource pool.
        self.instance_type = instance_type
        # The inventory health.
        self.inventory_health = inventory_health
        # The error message returned when the elastic strength is 0.
        self.msg = msg
        # The availability of the resource pool. Valid values:
        # 
        # - Available: The resource pool is available.
        # 
        # - Unavailable: The resource pool is unavailable. This can occur if the instance type is not deployed in the zone, has insufficient inventory, or does not meet other constraints.
        self.status = status
        # The elastic strength of the resource pool.>Warning:  This parameter is deprecated.
        self.strength = strength
        # The VSwitches in the zone of the resource pool.
        self.v_switch_ids = v_switch_ids
        # The zone ID of the resource pool.
        self.zone_id = zone_id

    def validate(self):
        if self.inventory_health:
            self.inventory_health.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.elastic_strength is not None:
            result['ElasticStrength'] = self.elastic_strength

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.inventory_health is not None:
            result['InventoryHealth'] = self.inventory_health.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.strength is not None:
            result['Strength'] = self.strength

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ElasticStrength') is not None:
            self.elastic_strength = m.get('ElasticStrength')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InventoryHealth') is not None:
            temp_model = main_models.DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePoolsInventoryHealth()
            self.inventory_health = temp_model.from_map(m.get('InventoryHealth'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strength') is not None:
            self.strength = m.get('Strength')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeElasticStrengthResponseBodyElasticStrengthModelsResourcePoolsInventoryHealth(DaraModel):
    def __init__(
        self,
        adequacy_score: int = None,
        health_score: int = None,
        hot_score: int = None,
        supply_score: int = None,
    ):
        # The adequacy score.
        # 
        # Valid values: 0 to 3.
        self.adequacy_score = adequacy_score
        # The health score.
        # 
        # - A score from 5 to 6 indicates high confidence in supply.
        # 
        # - A score from 1 to 4 indicates that supply is not guaranteed. Consider making on-demand reservations.
        # 
        # - A score from -3 to 0 indicates a supply health alert. Consider using a different instance type.
        # 
        # The health score is calculated using the formula: `HealthScore` = `AdequacyScore` + `SupplyScore` - `HotScore`.
        self.health_score = health_score
        # The hot score.
        # 
        # Valid values: 0 to 3.
        self.hot_score = hot_score
        # The supply score.
        # 
        # Valid values: 0 to 3.
        self.supply_score = supply_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adequacy_score is not None:
            result['AdequacyScore'] = self.adequacy_score

        if self.health_score is not None:
            result['HealthScore'] = self.health_score

        if self.hot_score is not None:
            result['HotScore'] = self.hot_score

        if self.supply_score is not None:
            result['SupplyScore'] = self.supply_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdequacyScore') is not None:
            self.adequacy_score = m.get('AdequacyScore')

        if m.get('HealthScore') is not None:
            self.health_score = m.get('HealthScore')

        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')

        if m.get('SupplyScore') is not None:
            self.supply_score = m.get('SupplyScore')

        return self

