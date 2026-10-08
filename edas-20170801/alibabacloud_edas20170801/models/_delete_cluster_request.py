# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        mode: int = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The type of the cluster ID. Valid values:
        # 
        # - 0: specifies the ID of the cluster in Enterprise Distributed Application Service (EDAS).
        # 
        # - 1: specifies the ID of the ACK cluster.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

