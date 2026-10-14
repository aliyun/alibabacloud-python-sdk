# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        cluster_id: str = None,
        release_node: bool = None,
    ):
        # The request body parameters.
        # 
        # This parameter is required.
        self.body_shrink = body_shrink
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to release the ENS instance where the node resides. Default value: true.
        self.release_node = release_node

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

        if self.release_node is not None:
            result['ReleaseNode'] = self.release_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ReleaseNode') is not None:
            self.release_node = m.get('ReleaseNode')

        return self

