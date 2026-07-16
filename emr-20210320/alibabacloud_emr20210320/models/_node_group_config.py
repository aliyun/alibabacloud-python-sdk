# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class NodeGroupConfig(DaraModel):
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
        spot_bid_prices: List[main_models.SpotBidPrice] = None,
        spot_instance_remedy: bool = None,
        spot_strategy: str = None,
        subscription_config: main_models.SubscriptionConfig = None,
        system_disk: main_models.SystemDisk = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
    ):
        # The IDs of the additional security groups. In addition to the security group of the cluster, you can specify additional security groups for the node group. You can specify up to two security group IDs.
        self.additional_security_group_ids = additional_security_group_ids
        # The auto scaling policy.
        self.auto_scaling_policy = auto_scaling_policy
        # Specifies whether to automatically create pay-as-you-go instances to meet the required capacity when the number of preemptible instances is insufficient. This parameter is effective only when `nodeResizeStrategy` is set to `COST_OPTIMIZED`.
        self.compensate_with_on_demand = compensate_with_on_demand
        # A list of custom component tags.
        self.component_tags = component_tags
        # The cost optimization settings.
        self.cost_optimized_config = cost_optimized_config
        # The data disks. Currently, the array can contain only one data disk.
        self.data_disks = data_disks
        # The deployment set strategy. Valid values:
        # 
        # - `NONE`: No deployment sets are used.
        # 
        # - `CLUSTER`: The cluster-level deployment set is used.
        # 
        # - `NODE_GROUP`: The node group-level deployment set is used.
        # 
        # Default value: `NONE`.
        self.deployment_set_strategy = deployment_set_strategy
        # Specifies whether to enable graceful shutdown for the components in the node group. Valid values:
        # 
        # - `true`: Enables graceful shutdown.
        # 
        # - `false`: Disables graceful shutdown.
        # 
        # Default value: `false`.
        self.graceful_shutdown = graceful_shutdown
        # The instance types. You can specify 1 to 100 instance types.
        self.instance_types = instance_types
        # The number of nodes in the node group. Valid values: 1 to 1,000.
        self.node_count = node_count
        # The name of the node group. The name can be up to 128 characters in length and must be unique within the cluster.
        self.node_group_name = node_group_name
        # The type of the node group. Valid values:
        # 
        # - `MASTER`: a master node group.
        # 
        # - `CORE`: a core node group.
        # 
        # - `TASK`: a task node group.
        # 
        # This parameter is required.
        self.node_group_type = node_group_type
        # The node scale-out strategy. Valid values:
        # 
        # - `COST_OPTIMIZED`: The cost-optimized strategy.
        # 
        # - `PRIORITY`: The priority-based strategy.
        # 
        # Default value: `PRIORITY`.
        self.node_resize_strategy = node_resize_strategy
        # The billing method of the node group. If you do not specify this parameter, the billing method of the cluster is used. Valid values:
        # 
        # - `PayAsYouGo`: pay-as-you-go.
        # 
        # - `Subscription`: subscription.
        # 
        # Default value: `PayAsYouGo`.
        self.payment_type = payment_type
        # The private pool options. This parameter is effective only when you create pay-as-you-go instances.
        self.private_pool_options = private_pool_options
        # The bid prices for the preemptible instances. This parameter is effective only when `SpotStrategy` is set to `SpotWithPriceLimit`. You can specify up to 100 bid prices.
        self.spot_bid_prices = spot_bid_prices
        # If enabled, the auto scaling group attempts to create a new instance to replace a spot instance that is about to be reclaimed. This process is triggered when the auto scaling group receives a system message about the impending reclamation. Valid values:
        # 
        # - `true`: The auto scaling group attempts to replace a spot instance that is about to be reclaimed.
        # 
        # - `false`: The auto scaling group does not attempt to replace a spot instance that is about to be reclaimed.
        # 
        # Default value: `false`.
        self.spot_instance_remedy = spot_instance_remedy
        # The preemption strategy for preemptible instances. Valid values:
        # 
        # - `NoSpot`: pay-as-you-go instances.
        # 
        # - `SpotWithPriceLimit`: preemptible instances with a user-defined maximum hourly price.
        # 
        # - `SpotAsPriceGo`: preemptible instances that are automatically bid at the pay-as-you-go price.
        # 
        # Default value: `NoSpot`.
        self.spot_strategy = spot_strategy
        # The subscription settings of the node group. If you do not specify this parameter, the subscription settings of the cluster are used.
        self.subscription_config = subscription_config
        # The system disk.
        self.system_disk = system_disk
        # The vSwitch IDs. You can specify 1 to 20 vSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # Specifies whether to assign a public IP address to the instances. Valid values:
        # 
        # - `true`: Assigns a public IP address.
        # 
        # - `false`: Does not assign a public IP address.
        # 
        # Default value: `false`.
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
                temp_model = main_models.SpotBidPrice()
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

