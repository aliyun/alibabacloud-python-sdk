# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeRecommendInstanceTypeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeRecommendInstanceTypeResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the recommended instance types.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRecommendInstanceTypeResponseBodyData(DaraModel):
    def __init__(
        self,
        recommend_instance_type: List[main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceType] = None,
    ):
        self.recommend_instance_type = recommend_instance_type

    def validate(self):
        if self.recommend_instance_type:
            for v1 in self.recommend_instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecommendInstanceType'] = []
        if self.recommend_instance_type is not None:
            for k1 in self.recommend_instance_type:
                result['RecommendInstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommend_instance_type = []
        if m.get('RecommendInstanceType') is not None:
            for k1 in m.get('RecommendInstanceType'):
                temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceType()
                self.recommend_instance_type.append(temp_model.from_map(k1))

        return self

class DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceType(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        instance_charge_type: str = None,
        instance_type: main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeInstanceType = None,
        network_type: str = None,
        priority: int = None,
        region_id: str = None,
        scene: str = None,
        spot_strategy: str = None,
        zone_id: str = None,
        zones: main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZones = None,
    ):
        # The commodity code of the instance type.
        self.commodity_code = commodity_code
        # The billing method of the instances.
        self.instance_charge_type = instance_charge_type
        # The details of the instance type.
        self.instance_type = instance_type
        # The network type of the ECS instances.
        self.network_type = network_type
        # The priority based on which the system sorts the instance types.
        self.priority = priority
        # The ID of the region in which the instance type is available.
        self.region_id = region_id
        # The scenario in which the instance type is recommended.
        self.scene = scene
        # The bidding policy for the spot instances.
        self.spot_strategy = spot_strategy
        # The ID of the zone in which the instance type is available.
        self.zone_id = zone_id
        # The details of the zones in which the instance type is available.
        self.zones = zones

    def validate(self):
        if self.instance_type:
            self.instance_type.validate()
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type.to_map()

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeInstanceType()
            self.instance_type = temp_model.from_map(m.get('InstanceType'))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('zone') is not None:
            for k1 in m.get('zone'):
                temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZone(DaraModel):
    def __init__(
        self,
        network_types: main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZoneNetworkTypes = None,
        zone_no: str = None,
    ):
        # The details of the network types of the instance type.
        self.network_types = network_types
        # The ID of the zone in which the instance type is available.
        self.zone_no = zone_no

    def validate(self):
        if self.network_types:
            self.network_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types.to_map()

        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkTypes') is not None:
            temp_model = main_models.DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZoneNetworkTypes()
            self.network_types = temp_model.from_map(m.get('NetworkTypes'))

        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')

        return self

class DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeZonesZoneNetworkTypes(DaraModel):
    def __init__(
        self,
        network_type: List[str] = None,
    ):
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        return self

class DescribeRecommendInstanceTypeResponseBodyDataRecommendInstanceTypeInstanceType(DaraModel):
    def __init__(
        self,
        cores: int = None,
        generation: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        memory: int = None,
        support_io_optimized: str = None,
    ):
        # The number of vCPUs of the instance type.
        self.cores = cores
        # The generation of the instance family.
        self.generation = generation
        # The name of the instance type.
        self.instance_type = instance_type
        # The instance family.
        self.instance_type_family = instance_type_family
        # The memory size of the instance type. Unit: MB.
        self.memory = memory
        # Indicates whether the instance type supports I/O optimization.
        self.support_io_optimized = support_io_optimized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.generation is not None:
            result['Generation'] = self.generation

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.support_io_optimized is not None:
            result['SupportIoOptimized'] = self.support_io_optimized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SupportIoOptimized') is not None:
            self.support_io_optimized = m.get('SupportIoOptimized')

        return self

