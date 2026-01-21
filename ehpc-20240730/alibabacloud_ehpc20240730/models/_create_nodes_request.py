# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class CreateNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node: main_models.NodeTemplate = None,
        count: int = None,
        deployment_set_id: str = None,
        hpcinter_connect: str = None,
        hostname_prefix: str = None,
        hostname_suffix: str = None,
        hostnames: List[str] = None,
        keep_alive: str = None,
        min_count: int = None,
        queue_name: str = None,
        ram_role: str = None,
        reserved_node_pool_id: str = None,
        v_switch_id: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The hardware configurations of the compute nodes.
        self.compute_node = compute_node
        # The number of compute nodes that you want to add. Valid values: 1 to 99. The MinCount value must be smaller than the Count value.
        # 
        # *   If the number of available Elastic Compute Service (ECS) instances is smaller than the MinCount value, the nodes fail to be added.
        # *   If the number of available ECS instances is larger than the MinCount value but smaller than the Count value, nodes are added based on the MinCount value.
        # *   If the number of available ECS instances is larger than the Count value, nodes are added based on the Count value.
        self.count = count
        # Deployment set ID. You can obtain the deployment set ID through [DescribeDeploymentSets](https://help.aliyun.com/document_detail/91313.html). Currently, only deployment sets with a low network latency strategy are supported.
        self.deployment_set_id = deployment_set_id
        # The type of the network between compute nodes. Valid values:
        # 
        # *   vpc
        # *   eRDMA
        self.hpcinter_connect = hpcinter_connect
        # The hostname prefix of the added compute nodes.
        self.hostname_prefix = hostname_prefix
        # The hostname suffix of the added compute nodes.
        self.hostname_suffix = hostname_suffix
        self.hostnames = hostnames
        # Specifies whether to enable deletion protection for the added compute nodes.
        self.keep_alive = keep_alive
        self.min_count = min_count
        # The name of the queue for which you want to create compute nodes.
        self.queue_name = queue_name
        # The Resource Access Management (RAM) role to be assumed by the added nodes.
        self.ram_role = ram_role
        # Preset node pool ID.
        self.reserved_node_pool_id = reserved_node_pool_id
        # The ID of the vSwitch to be used by the added nodes.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.compute_node:
            self.compute_node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.compute_node is not None:
            result['ComputeNode'] = self.compute_node.to_map()

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

        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

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
            temp_model = main_models.NodeTemplate()
            self.compute_node = temp_model.from_map(m.get('ComputeNode'))

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
            self.hostnames = m.get('Hostnames')

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

