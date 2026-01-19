# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceClusterInfoRequest(DaraModel):
    def __init__(
        self,
        instance_cluster_name: str = None,
        security_token: str = None,
    ):
        # The name of the dedicated instance cluster.
        self.instance_cluster_name = instance_cluster_name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_cluster_name is not None:
            result['InstanceClusterName'] = self.instance_cluster_name

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClusterName') is not None:
            self.instance_cluster_name = m.get('InstanceClusterName')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

