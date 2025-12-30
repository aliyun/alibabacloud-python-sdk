# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class CreateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components_shrink: str = None,
        hpn_zone: str = None,
        ignore_failed_node_tasks: bool = None,
        networks_shrink: str = None,
        nimiz_vswitches_shrink: str = None,
        node_groups_shrink: str = None,
        open_eni_jumbo_frame: bool = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateClusterShrinkRequestTag] = None,
    ):
        # Cluster description
        self.cluster_description = cluster_description
        # Cluster name
        self.cluster_name = cluster_name
        # Cluster type
        self.cluster_type = cluster_type
        # Components (software instances)
        self.components_shrink = components_shrink
        # Cluster number
        self.hpn_zone = hpn_zone
        # Whether to allow skipping failed nodes, the default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Network information
        self.networks_shrink = networks_shrink
        # Node VSwitches
        self.nimiz_vswitches_shrink = nimiz_vswitches_shrink
        # Node group list
        self.node_groups_shrink = node_groups_shrink
        # Whether the network interface supports jumbo frames
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource tags
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        if self.networks_shrink is not None:
            result['Networks'] = self.networks_shrink

        if self.nimiz_vswitches_shrink is not None:
            result['NimizVSwitches'] = self.nimiz_vswitches_shrink

        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink

        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        if m.get('Networks') is not None:
            self.networks_shrink = m.get('Networks')

        if m.get('NimizVSwitches') is not None:
            self.nimiz_vswitches_shrink = m.get('NimizVSwitches')

        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')

        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateClusterShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateClusterShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

