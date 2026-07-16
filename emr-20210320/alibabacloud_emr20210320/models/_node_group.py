# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class NodeGroup(DaraModel):
    def __init__(
        self,
        additional_security_group_ids: List[str] = None,
        compensate_with_on_demand: bool = None,
        cost_optimized_config: main_models.CostOptimizedConfig = None,
        data_disks: List[main_models.DataDisk] = None,
        deployment_set_strategy: str = None,
        graceful_shutdown: bool = None,
        instance_types: List[str] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_group_state: str = None,
        node_group_type: str = None,
        node_resize_strategy: str = None,
        payment_type: str = None,
        private_pool_options: main_models.PrivatePoolOptions = None,
        running_node_count: int = None,
        spot_bid_prices: List[main_models.SpotBidPrice] = None,
        spot_instance_remedy: bool = None,
        spot_strategy: str = None,
        state_change_reason: main_models.NodeGroupStateChangeReason = None,
        status: str = None,
        system_disk: main_models.SystemDisk = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
        zone_id: str = None,
    ):
        # The additional security group IDs.
        self.additional_security_group_ids = additional_security_group_ids
        # Applies only when `NodeResizeStrategy` is set to `COST_OPTIMIZED`. If set to `true`, the system creates Pay-As-You-Go instances to meet the target capacity if it fails to create enough spot instances due to price or inventory constraints.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configurations of the cost-optimized mode.
        self.cost_optimized_config = cost_optimized_config
        # The data disks.
        self.data_disks = data_disks
        # The Deployment Set strategy. Valid values:
        # 
        # - NONE: Does not use a Deployment Set.
        # 
        # - CLUSTER: Uses a cluster-level Deployment Set.
        # 
        # - NODE_GROUP: Uses a node group-level Deployment Set.
        # 
        # Default: `NONE`.
        self.deployment_set_strategy = deployment_set_strategy
        # Specifies whether to enable graceful shutdown for components deployed in the node group. Valid values:
        # 
        # - true: Enables graceful shutdown.
        # 
        # - false: Disables graceful shutdown.
        self.graceful_shutdown = graceful_shutdown
        # The instance types.
        self.instance_types = instance_types
        # The node group ID.
        self.node_group_id = node_group_id
        # The node group name.
        self.node_group_name = node_group_name
        # The state of the node group.
        self.node_group_state = node_group_state
        # The type of the node group. Valid values:
        # 
        # - MASTER: A master node.
        # 
        # - CORE: A core node.
        # 
        # - TASK: A task node.
        # 
        # - GATEWAY: A gateway node. This value is not applicable to DATALAKE, OLAP, or DATASERVING clusters.
        self.node_group_type = node_group_type
        # - COST_OPTIMIZED: The cost-optimized strategy.
        # 
        # - PRIORITY: The priority-based strategy.
        self.node_resize_strategy = node_resize_strategy
        # The payment type. Valid values are `Subscription` for the subscription billing method and `PayAsYouGo` for the Pay-As-You-Go billing method.
        self.payment_type = payment_type
        # The private pool options.
        self.private_pool_options = private_pool_options
        # The number of running nodes.
        self.running_node_count = running_node_count
        # The bid prices for the spot instances. This parameter is effective only when `SpotStrategy` is set to `SpotWithPriceLimit`. The array can contain 0 to 100 elements.
        self.spot_bid_prices = spot_bid_prices
        # Specifies whether to enable spot instance remedy. If enabled, the scaling group attempts to create a new instance to replace a spot instance that is about to be reclaimed. Valid values:
        # 
        # - true: Enables spot instance remedy.
        # 
        # - false: Disables spot instance remedy.
        # 
        # Default: `false`.
        self.spot_instance_remedy = spot_instance_remedy
        # The policy for using spot instances. Valid values:
        # 
        # - NoSpot: No spot instances are used.
        # 
        # - SpotWithPriceLimit: Spot instances are created with a user-defined maximum bid price.
        # 
        # - SpotAsPriceGo: The system automatically bids for spot instances. The bid price does not exceed the price of a Pay-As-You-Go instance.
        # 
        # Default: `NoSpot`.
        self.spot_strategy = spot_strategy
        # The reason for the state change.
        self.state_change_reason = state_change_reason
        # The node group state.
        self.status = status
        # The system disk.
        self.system_disk = system_disk
        # The VSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # Specifies whether to assign a public IP address.
        self.with_public_ip = with_public_ip
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
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
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids

        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

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

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_state is not None:
            result['NodeGroupState'] = self.node_group_state

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.running_node_count is not None:
            result['RunningNodeCount'] = self.running_node_count

        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k1 in self.spot_bid_prices:
                result['SpotBidPrices'].append(k1.to_map() if k1 else None)

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.state_change_reason is not None:
            result['StateChangeReason'] = self.state_change_reason.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')

        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

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

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupState') is not None:
            self.node_group_state = m.get('NodeGroupState')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.PrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('RunningNodeCount') is not None:
            self.running_node_count = m.get('RunningNodeCount')

        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k1 in m.get('SpotBidPrices'):
                temp_model = main_models.SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k1))

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StateChangeReason') is not None:
            temp_model = main_models.NodeGroupStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('StateChangeReason'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.SystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

