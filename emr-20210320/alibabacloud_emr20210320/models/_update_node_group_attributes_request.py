# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class UpdateNodeGroupAttributesRequest(DaraModel):
    def __init__(
        self,
        ack_config: main_models.AckConfig = None,
        additional_security_group_ids: List[str] = None,
        auto_compensate_state: bool = None,
        cluster_id: str = None,
        cost_optimized_config: main_models.CostOptimizedConfig = None,
        description: str = None,
        ecs_spot_strategy: str = None,
        enable_graceful_decommission: bool = None,
        instance_type_list: List[str] = None,
        key_pair_name: str = None,
        max_size: int = None,
        min_size: int = None,
        node_count: int = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_resize_strategy: str = None,
        region_id: str = None,
        spot_bid_prices: List[main_models.SpotBidPrice] = None,
        spot_instance_remedy: bool = None,
        v_switch_id: str = None,
    ):
        # The ACK cluster configuration.
        self.ack_config = ack_config
        # The list of security group IDs.
        self.additional_security_group_ids = additional_security_group_ids
        # The automatic compensation state.
        self.auto_compensate_state = auto_compensate_state
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The cost-optimized mode configuration.
        self.cost_optimized_config = cost_optimized_config
        # The node group description.
        self.description = description
        # The spot instance strategy.
        self.ecs_spot_strategy = ecs_spot_strategy
        # Specifies whether to enable graceful decommission. When a cluster is created in V303, graceful decommission is disabled by default for task groups.
        self.enable_graceful_decommission = enable_graceful_decommission
        # The list of ECS instance types.
        self.instance_type_list = instance_type_list
        # The key pair for ECS logon.
        self.key_pair_name = key_pair_name
        # The maximum number of instances in the node group.
        self.max_size = max_size
        # The minimum number of instances in the node group.
        self.min_size = min_size
        # The target number of nodes in the node group.
        self.node_count = node_count
        # The node group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The node group name.
        self.node_group_name = node_group_name
        # The node scale-out strategy. Valid values: COST_OPTIMIZED and PRIORITY. Default value: PRIORITY.
        self.node_resize_strategy = node_resize_strategy
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The maximum bid prices for spot instances. This parameter takes effect only when spotStrategy is set to SpotWithPriceLimit.
        self.spot_bid_prices = spot_bid_prices
        # Specifies whether to enable spot instance supplementation. If this feature is enabled, the scaling group attempts to create new instances to replace spot instances that are about to be reclaimed when the system sends a reclamation notification. Default value: false.
        self.spot_instance_remedy = spot_instance_remedy
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.ack_config:
            self.ack_config.validate()
        if self.cost_optimized_config:
            self.cost_optimized_config.validate()
        if self.spot_bid_prices:
            for v1 in self.spot_bid_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_config is not None:
            result['AckConfig'] = self.ack_config.to_map()

        if self.additional_security_group_ids is not None:
            result['AdditionalSecurityGroupIds'] = self.additional_security_group_ids

        if self.auto_compensate_state is not None:
            result['AutoCompensateState'] = self.auto_compensate_state

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cost_optimized_config is not None:
            result['CostOptimizedConfig'] = self.cost_optimized_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_spot_strategy is not None:
            result['EcsSpotStrategy'] = self.ecs_spot_strategy

        if self.enable_graceful_decommission is not None:
            result['EnableGracefulDecommission'] = self.enable_graceful_decommission

        if self.instance_type_list is not None:
            result['InstanceTypeList'] = self.instance_type_list

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_resize_strategy is not None:
            result['NodeResizeStrategy'] = self.node_resize_strategy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['SpotBidPrices'] = []
        if self.spot_bid_prices is not None:
            for k1 in self.spot_bid_prices:
                result['SpotBidPrices'].append(k1.to_map() if k1 else None)

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckConfig') is not None:
            temp_model = main_models.AckConfig()
            self.ack_config = temp_model.from_map(m.get('AckConfig'))

        if m.get('AdditionalSecurityGroupIds') is not None:
            self.additional_security_group_ids = m.get('AdditionalSecurityGroupIds')

        if m.get('AutoCompensateState') is not None:
            self.auto_compensate_state = m.get('AutoCompensateState')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CostOptimizedConfig') is not None:
            temp_model = main_models.CostOptimizedConfig()
            self.cost_optimized_config = temp_model.from_map(m.get('CostOptimizedConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsSpotStrategy') is not None:
            self.ecs_spot_strategy = m.get('EcsSpotStrategy')

        if m.get('EnableGracefulDecommission') is not None:
            self.enable_graceful_decommission = m.get('EnableGracefulDecommission')

        if m.get('InstanceTypeList') is not None:
            self.instance_type_list = m.get('InstanceTypeList')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeResizeStrategy') is not None:
            self.node_resize_strategy = m.get('NodeResizeStrategy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.spot_bid_prices = []
        if m.get('SpotBidPrices') is not None:
            for k1 in m.get('SpotBidPrices'):
                temp_model = main_models.SpotBidPrice()
                self.spot_bid_prices.append(temp_model.from_map(k1))

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

