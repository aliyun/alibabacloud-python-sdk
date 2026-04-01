# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachInstancesToNodePoolShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instances_shrink: str = None,
        nodepool_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.instances_shrink = instances_shrink
        # This parameter is required.
        self.nodepool_id = nodepool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        return self

