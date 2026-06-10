# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node_shrink: str = None,
        count: int = None,
        deployment_set_id: str = None,
        hpcinter_connect: str = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        hostnames_shrink: str = None,
        keep_alive: str = None,
        min_count: int = None,
        queue_name: str = None,
        ram_role: str = None,
        reserved_node_pool_id: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # You can call [ListClusters](https://help.aliyun.com/document_detail/87116.html) to obtain the cluster ID.
        self.cluster_id = cluster_id
        # Specifies the hardware configuration of the compute node.
        self.compute_node_shrink = compute_node_shrink
        # The number of compute nodes to add. Valid values: 1 to 99. The value of MinCount must be less than the value of Count.
        # 
        # - If the ECS inventory is less than MinCount, the operation fails.
        # 
        # - If the ECS inventory is between MinCount and Count, the number of nodes specified by MinCount is added.
        # 
        # - If the ECS inventory is greater than Count, the number of nodes specified by Count is added.
        self.count = count
        # The ID of the deployment set. You can call the [DescribeDeploymentSets](https://help.aliyun.com/document_detail/91313.html) operation to obtain the ID. Only deployment sets that use the low-latency network policy are supported.
        self.deployment_set_id = deployment_set_id
        # Specifies the network type for communication between compute nodes. Valid values:
        # 
        # - vpc
        # 
        # - eRDMA
        self.hpcinter_connect = hpcinter_connect
        # The hostname prefix for the compute nodes in the queue.
        self.hostname_prefix = hostname_prefix
        # The hostname suffix of the compute nodes in the queue.
        self.hostname_suffix = hostname_suffix
        # The ID of the reserved node pool.
        self.hostnames_shrink = hostnames_shrink
        # Specifies whether deletion protection is enabled for the compute node.
        self.keep_alive = keep_alive
        self.min_count = min_count
        # The name of the queue to which the compute nodes belong.
        self.queue_name = queue_name
        # The name of the authorized instance role to be attached to the compute nodes in the queue.
        self.ram_role = ram_role
        # The ID of the reserved node pool.
        self.reserved_node_pool_id = reserved_node_pool_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.compute_node_shrink is not None:
            result['ComputeNode'] = self.compute_node_shrink

        if self.count is not None:
            result['Count'] = self.count

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect

        if self.hostname_prefix is not None:
            result['HostnamePrefix'] = self.hostname_prefix

        if self.hostname_suffix is not None:
            result['HostnameSuffix'] = self.hostname_suffix

        if self.hostnames_shrink is not None:
            result['Hostnames'] = self.hostnames_shrink

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.reserved_node_pool_id is not None:
            result['ReservedNodePoolId'] = self.reserved_node_pool_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComputeNode') is not None:
            self.compute_node_shrink = m.get('ComputeNode')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')

        if m.get('HostnamePrefix') is not None:
            self.hostname_prefix = m.get('HostnamePrefix')

        if m.get('HostnameSuffix') is not None:
            self.hostname_suffix = m.get('HostnameSuffix')

        if m.get('Hostnames') is not None:
            self.hostnames_shrink = m.get('Hostnames')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('ReservedNodePoolId') is not None:
            self.reserved_node_pool_id = m.get('ReservedNodePoolId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

