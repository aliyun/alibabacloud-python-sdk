# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterBasicInfoRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The ID of the cluster that you want to query.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The dimension from which you want to configure the feature. Valid values:
        # 
        # *   **Cluster**: the ID of the cluster
        # 
        # This parameter is required.
        self.target_type = target_type
        # The type of the feature. Valid values:
        # 
        # *   **containerNetwork**: container network topology
        # *   **interceptionSwitch**: cluster microsegmentation
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

