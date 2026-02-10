# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterInfoListRequest(DaraModel):
    def __init__(
        self,
        target: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The operation value. The value specifies the ID of the cluster.
        self.target = target
        # The dimension based on which you want to configure the feature. Valid values:
        # 
        # *   **Cluster**: the ID of the cluster
        # 
        # This parameter is required.
        self.target_type = target_type
        # The type of the feature. Valid values:
        # 
        # *   **containerNetwork**: container network
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
        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

