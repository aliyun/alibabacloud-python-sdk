# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleClusterNodePoolShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        cluster_id: str = None,
        nodepool_id: str = None,
    ):
        self.body_shrink = body_shrink
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.nodepool_id = nodepool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        return self

