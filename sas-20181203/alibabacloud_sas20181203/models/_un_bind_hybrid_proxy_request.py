# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnBindHybridProxyRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        yundun_uuids: List[str] = None,
    ):
        # The name of the proxy cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The UUIDs of the servers that you want to remove from the proxy cluster.
        # 
        # This parameter is required.
        self.yundun_uuids = yundun_uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.yundun_uuids is not None:
            result['YundunUuids'] = self.yundun_uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('YundunUuids') is not None:
            self.yundun_uuids = m.get('YundunUuids')

        return self

