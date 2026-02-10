# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridProxyClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        remark: str = None,
    ):
        # The name of the proxy cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The remarks.
        # 
        # This parameter is required.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

