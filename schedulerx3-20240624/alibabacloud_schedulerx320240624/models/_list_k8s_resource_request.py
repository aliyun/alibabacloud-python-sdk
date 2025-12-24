# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListK8sResourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        k_8s_cluster_id: str = None,
        k_8s_namespace: str = None,
        resource_type: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.k_8s_cluster_id = k_8s_cluster_id
        self.k_8s_namespace = k_8s_namespace
        # This parameter is required.
        self.resource_type = resource_type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id

        if self.k_8s_namespace is not None:
            result['K8sNamespace'] = self.k_8s_namespace

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')

        if m.get('K8sNamespace') is not None:
            self.k_8s_namespace = m.get('K8sNamespace')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

