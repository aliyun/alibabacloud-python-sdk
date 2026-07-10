# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExtendClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        ip_allocation_policy_shrink: str = None,
        node_groups_shrink: str = None,
        v_switch_zone_id: str = None,
        vpd_subnets_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to skip failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The combined IP allocation policy. Each policy can use only one policy type, and multiple policies can be combined.
        self.ip_allocation_policy_shrink = ip_allocation_policy_shrink
        # The node groups.
        self.node_groups_shrink = node_groups_shrink
        # The zone ID of the vSwitch.
        self.v_switch_zone_id = v_switch_zone_id
        # The list of cluster subnets.
        self.vpd_subnets_shrink = vpd_subnets_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        if self.ip_allocation_policy_shrink is not None:
            result['IpAllocationPolicy'] = self.ip_allocation_policy_shrink

        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink

        if self.v_switch_zone_id is not None:
            result['VSwitchZoneId'] = self.v_switch_zone_id

        if self.vpd_subnets_shrink is not None:
            result['VpdSubnets'] = self.vpd_subnets_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        if m.get('IpAllocationPolicy') is not None:
            self.ip_allocation_policy_shrink = m.get('IpAllocationPolicy')

        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')

        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')

        if m.get('VpdSubnets') is not None:
            self.vpd_subnets_shrink = m.get('VpdSubnets')

        return self

