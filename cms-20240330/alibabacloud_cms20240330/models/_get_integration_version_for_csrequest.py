# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIntegrationVersionForCSRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        return self

