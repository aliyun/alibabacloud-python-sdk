# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ScalingGroupConfig(DaraModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_count: int = None,
        data_disk_size: int = None,
        default_cool_down_time: int = None,
        instance_type_list: List[main_models.ScalingGroupConfigInstanceTypeList] = None,
        multi_available_policy: main_models.ScalingGroupConfigMultiAvailablePolicy = None,
        node_offline_policy: main_models.ScalingGroupConfigNodeOfflinePolicy = None,
        private_pool_options: main_models.ScalingGroupConfigPrivatePoolOptions = None,
        scaling_max_size: int = None,
        scaling_min_size: int = None,
        spot_strategy: str = None,
        sys_disk_category: str = None,
        sys_disk_size: int = None,
        trigger_mode: str = None,
    ):
        # 数据盘类型。
        self.data_disk_category = data_disk_category
        # 数据盘个数。
        self.data_disk_count = data_disk_count
        # 数据盘大小,单位GB。
        self.data_disk_size = data_disk_size
        # 默认冷却时间。
        self.default_cool_down_time = default_cool_down_time
        # 抢占实例列表。
        self.instance_type_list = instance_type_list
        # 资源可用性策略(成本优化参数)。
        self.multi_available_policy = multi_available_policy
        # 节点下线策略。
        self.node_offline_policy = node_offline_policy
        # 私有池选项	。
        self.private_pool_options = private_pool_options
        # 伸缩组节点最大个数。
        self.scaling_max_size = scaling_max_size
        # 伸缩组节点最小个数。
        self.scaling_min_size = scaling_min_size
        # 抢占式Spot实例策略。
        self.spot_strategy = spot_strategy
        # 系统盘类型。
        self.sys_disk_category = sys_disk_category
        # 系统盘大小,单位GB。
        self.sys_disk_size = sys_disk_size
        # 伸缩活动触发模式。
        self.trigger_mode = trigger_mode

    def validate(self):
        if self.instance_type_list:
            for v1 in self.instance_type_list:
                 if v1:
                    v1.validate()
        if self.multi_available_policy:
            self.multi_available_policy.validate()
        if self.node_offline_policy:
            self.node_offline_policy.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_count is not None:
            result['DataDiskCount'] = self.data_disk_count

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.default_cool_down_time is not None:
            result['DefaultCoolDownTime'] = self.default_cool_down_time

        result['InstanceTypeList'] = []
        if self.instance_type_list is not None:
            for k1 in self.instance_type_list:
                result['InstanceTypeList'].append(k1.to_map() if k1 else None)

        if self.multi_available_policy is not None:
            result['MultiAvailablePolicy'] = self.multi_available_policy.to_map()

        if self.node_offline_policy is not None:
            result['NodeOfflinePolicy'] = self.node_offline_policy.to_map()

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.scaling_max_size is not None:
            result['ScalingMaxSize'] = self.scaling_max_size

        if self.scaling_min_size is not None:
            result['ScalingMinSize'] = self.scaling_min_size

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.sys_disk_category is not None:
            result['SysDiskCategory'] = self.sys_disk_category

        if self.sys_disk_size is not None:
            result['SysDiskSize'] = self.sys_disk_size

        if self.trigger_mode is not None:
            result['TriggerMode'] = self.trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskCount') is not None:
            self.data_disk_count = m.get('DataDiskCount')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DefaultCoolDownTime') is not None:
            self.default_cool_down_time = m.get('DefaultCoolDownTime')

        self.instance_type_list = []
        if m.get('InstanceTypeList') is not None:
            for k1 in m.get('InstanceTypeList'):
                temp_model = main_models.ScalingGroupConfigInstanceTypeList()
                self.instance_type_list.append(temp_model.from_map(k1))

        if m.get('MultiAvailablePolicy') is not None:
            temp_model = main_models.ScalingGroupConfigMultiAvailablePolicy()
            self.multi_available_policy = temp_model.from_map(m.get('MultiAvailablePolicy'))

        if m.get('NodeOfflinePolicy') is not None:
            temp_model = main_models.ScalingGroupConfigNodeOfflinePolicy()
            self.node_offline_policy = temp_model.from_map(m.get('NodeOfflinePolicy'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.ScalingGroupConfigPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('ScalingMaxSize') is not None:
            self.scaling_max_size = m.get('ScalingMaxSize')

        if m.get('ScalingMinSize') is not None:
            self.scaling_min_size = m.get('ScalingMinSize')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SysDiskCategory') is not None:
            self.sys_disk_category = m.get('SysDiskCategory')

        if m.get('SysDiskSize') is not None:
            self.sys_disk_size = m.get('SysDiskSize')

        if m.get('TriggerMode') is not None:
            self.trigger_mode = m.get('TriggerMode')

        return self

class ScalingGroupConfigPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # 私有池id。
        self.id = id
        # 实例启动的私有池容量选项。。
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        return self

class ScalingGroupConfigNodeOfflinePolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        timeout_ms: int = None,
    ):
        # 下线模式,是否为优雅下线。
        self.mode = mode
        # 下线超时时间,单位毫秒。
        self.timeout_ms = timeout_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.timeout_ms is not None:
            result['TimeoutMs'] = self.timeout_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('TimeoutMs') is not None:
            self.timeout_ms = m.get('TimeoutMs')

        return self

class ScalingGroupConfigMultiAvailablePolicy(DaraModel):
    def __init__(
        self,
        policy_param: main_models.ScalingGroupConfigMultiAvailablePolicyPolicyParam = None,
        policy_type: str = None,
    ):
        # 资源可用性策略(成本优化参数)。
        self.policy_param = policy_param
        # 策略类型。
        self.policy_type = policy_type

    def validate(self):
        if self.policy_param:
            self.policy_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_param is not None:
            result['PolicyParam'] = self.policy_param.to_map()

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyParam') is not None:
            temp_model = main_models.ScalingGroupConfigMultiAvailablePolicyPolicyParam()
            self.policy_param = temp_model.from_map(m.get('PolicyParam'))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

class ScalingGroupConfigMultiAvailablePolicyPolicyParam(DaraModel):
    def __init__(
        self,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
    ):
        # 按需实例最小个数。
        self.on_demand_base_capacity = on_demand_base_capacity
        # 按需实例百分比。
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # 抢占实例类型池规模。
        self.spot_instance_pools = spot_instance_pools
        # 是否使用按量补偿。
        self.spot_instance_remedy = spot_instance_remedy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity

        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity

        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')

        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')

        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        return self

class ScalingGroupConfigInstanceTypeList(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
    ):
        # Ecs类型。
        self.instance_type = instance_type
        # 抢占价格上限,可空。
        self.spot_price_limit = spot_price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        return self

