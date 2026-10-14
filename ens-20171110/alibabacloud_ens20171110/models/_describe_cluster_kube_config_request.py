# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterKubeConfigRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is essentially required. If it is not provided, the service returns BadRequest. The target cluster must also have completed control plane deployment and certificate generation. You cannot obtain the kubeconfig for a cluster in the initial state.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

