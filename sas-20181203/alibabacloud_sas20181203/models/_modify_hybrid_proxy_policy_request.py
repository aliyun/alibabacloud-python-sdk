# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridProxyPolicyRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        policy_info: str = None,
    ):
        # The name of the proxy cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The policy of the proxy cluster.
        # 
        # This parameter is required.
        self.policy_info = policy_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.policy_info is not None:
            result['PolicyInfo'] = self.policy_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('PolicyInfo') is not None:
            self.policy_info = m.get('PolicyInfo')

        return self

