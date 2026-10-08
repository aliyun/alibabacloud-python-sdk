# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListK8sIngressRulesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        condition: str = None,
        namespace: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The filter conditions. Set the value to a JSON string in the format of {"field":"Name", "pattern":"my-"}, where:
        # 
        # *   field: the parameter to be matched. Valid values: Name and ClusterName.
        # *   pattern: the content to be matched.
        # 
        # For example, a value of {"field":"Name", "pattern":"my-"} indicates that the specified filter conditions match the routing rules whose names start with my-.
        self.condition = condition
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The ID of the region where the cluster resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.condition is not None:
            result['Condition'] = self.condition

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

