# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterNodePoolShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        kubernetes_config_shrink: str = None,
        nodepool_info_shrink: str = None,
        scaling_group_shrink: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.kubernetes_config_shrink = kubernetes_config_shrink
        # This parameter is required.
        self.nodepool_info_shrink = nodepool_info_shrink
        # This parameter is required.
        self.scaling_group_shrink = scaling_group_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.kubernetes_config_shrink is not None:
            result['KubernetesConfig'] = self.kubernetes_config_shrink

        if self.nodepool_info_shrink is not None:
            result['NodepoolInfo'] = self.nodepool_info_shrink

        if self.scaling_group_shrink is not None:
            result['ScalingGroup'] = self.scaling_group_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('KubernetesConfig') is not None:
            self.kubernetes_config_shrink = m.get('KubernetesConfig')

        if m.get('NodepoolInfo') is not None:
            self.nodepool_info_shrink = m.get('NodepoolInfo')

        if m.get('ScalingGroup') is not None:
            self.scaling_group_shrink = m.get('ScalingGroup')

        return self

