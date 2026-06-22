# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CreateNodeGroupConfig(DaraModel):
    def __init__(
        self,
        additional_security_group_ids: List[str] = None,
        auto_scaling_policy: main_models.AutoScalingPolicy = None,
        compensate_with_on_demand: bool = None,
        component_tags: List[str] = None,
        cost_optimized_config: main_models.CostOptimizedConfig = None,
        data_disks: List[main_models.DataDisk] = None,
        deployment_set_strategy: str = None,
        graceful_shutdown: bool = None,
        instance_types: List[str] = None,
        node_count: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        node_resize_strategy: str = None,
        payment_type: str = None,
        private_pool_options: main_models.PrivatePoolOptions = None,
        spot_bid_prices: List[main_models.CreateNodeGroupConfigSpotBidPrices] = None,
        spot_instance_remedy: bool = None,
        spot_strategy: str = None,
        subscription_config: main_models.SubscriptionConfig = None,
        system_disk: main_models.SystemDisk = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
    ):
        # 附加安全组。除集群设置的安全组外，为节点组单独设置的附加安全组。数组元数个数N的取值范围：0~2。
        self.additional_security_group_ids = additional_security_group_ids
        self.auto_scaling_policy = auto_scaling_policy
        self.compensate_with_on_demand = compensate_with_on_demand
        self.component_tags = component_tags
        # 成本优化模式配置。
        self.cost_optimized_config = cost_optimized_config
        # 数据盘。当前数据盘只支持一种磁盘类型，即数组元数个数N的取值范围：1~1。
        self.data_disks = data_disks
        # 部署集策略。取值范围：
        # - NONE：不适用部署集。
        # - CLUSTER：使用集群级别部署集。
        # - NODE_GROUP：使用节点组级别部署集。
        # 
        # 默认值：NONE。
        self.deployment_set_strategy = deployment_set_strategy
        # 节点组上部署的组件是否开启优雅下线。取值范围：
        # - true：开启优雅下线。
        # - false：不开启优雅下线。
        # 
        # 默认值：false。
        self.graceful_shutdown = graceful_shutdown
        # 节点实例类型列表。数组元数个数N的取值范围：1~100。
        self.instance_types = instance_types
        # 节点数量。取值范围：1~1000。
        self.node_count = node_count
        # 节点组名称。最大长度128个字符。集群内要求节点组名称唯一。
        self.node_group_name = node_group_name
        # 节点组类型。取值范围：
        # - MASTER：管理类型节点组。
        # - CORE：存储类型节点组。
        # - TASK：计算类型节点组。
        # 
        # This parameter is required.
        self.node_group_type = node_group_type
        # 节点扩容策略。取值范围：
        # - COST_OPTIMIZED：成本优化策略。
        # - PRIORITY：优先级策略。
        # 
        # 默认值：PRIORITY。
        self.node_resize_strategy = node_resize_strategy
        # 节点组付费类型。不传入时默认和集群付费类型一致。取值范围：
        # - PayAsYouGo：后付费，按量付费。
        # - Subscription：预付费，包年包月。
        # 
        # 默认值：PayAsYouGo。
        self.payment_type = payment_type
        self.private_pool_options = private_pool_options
        # 抢占式Spot实例出价价格。参数SpotStrategy取值为SpotWithPriceLimit时生效。数组元数个数N的取值范围：0~100。
        self.spot_bid_prices = spot_bid_prices
        # 开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。取值范围：
        # - true：开启补齐抢占式实例。
        # - false：不开启补齐抢占式实例。
        # 
        # 默认值：false。
        self.spot_instance_remedy = spot_instance_remedy
        # 抢占式Spot实例策略。取值范围：
        # - NoSpot：正常按量付费实例。
        # - SpotWithPriceLimit：设置最高出价的抢占式实例。
        # - SpotAsPriceGo：系统自动出价，最高按量付费价格的抢占式实例。
        # 
        # 默认值：NoSpot。
        self.spot_strategy = spot_strategy
        # 节点组预付费配置。不传入时默认和集群预付费配置一致。
        self.subscription_config = subscription_config
        # 系统盘。
        self.system_disk = system_disk
        # 虚拟机交换机ID列表。数组元数个数N的取值范围：1~20。
        self.v_switch_ids = v_switch_ids
        # 是否开公网IP。取值范围：
        # - true：开公网。
        # - false：不开公网。
        # 
        # 默认值：false。
        self.with_public_ip = with_public_ip

    def validate(self):
        if self.auto_scaling_policy:
            self.auto_scaling_policy.validate()
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.spot_bid_prices:
            for v1 in self.spot_bid_prices:
                 if v1:
                    v1.validate()
        if self.subscription_config:
            self.subscription_config.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids

        if self.auto_scaling_policy is not None:
            result['AutoScalingPolicy'] = self.auto_scaling_policy.to_map()

        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

        if self.component_tags is not None:
            result['ComponentTags'] = self.component_tags

        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.deployment_set_strategy is not None:
            result['DeploymentSetStrategy'] = self.deployment_set_strategy

        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k1 in self.spot_bid_prices:
                result['SpotBidPrices'].append(k1.to_map() if k1 else None)

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.subscription_config is not None:
            result['SubscriptionConfig'] = self.subscription_config.to_map()

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')

        if m.get('AutoScalingPolicy') is not None:
            temp_model = main_models.AutoScalingPolicy()
            self.auto_scaling_policy = temp_model.from_map(m.get('AutoScalingPolicy'))

        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

        if m.get('ComponentTags') is not None:
            self.component_tags = m.get('ComponentTags')

        if m.get('CostOptimizedConfig') is not None:
            temp_model = main_models.CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m.get('CostOptimizedConfig'))

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.DataDisk()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('DeploymentSetStrategy') is not None:
            self.deployment_set_strategy = m.get('DeploymentSetStrategy')

        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.PrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k1 in m.get('SpotBidPrices'):
                temp_model = main_models.CreateNodeGroupConfigSpotBidPrices()
                self.spot_bid_prices.append(temp_model.from_map(k1))

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SubscriptionConfig') is not None:
            temp_model = main_models.SubscriptionConfig()
            self.subscription_config = temp_model.from_map(m.get('SubscriptionConfig'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.SystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')

        return self

class CreateNodeGroupConfigSpotBidPrices(DaraModel):
    def __init__(
        self,
        bid_price: float = None,
        instance_type: str = None,
    ):
        # 实例的每小时最高出价。支持最大3位小数，参数SpotStrategy=SpotWithPriceLimit时，该参数生效。
        self.bid_price = bid_price
        # 实例类型。
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid_price is not None:
            result['BidPrice'] = self.bid_price

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BidPrice') is not None:
            self.bid_price = m.get('BidPrice')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

