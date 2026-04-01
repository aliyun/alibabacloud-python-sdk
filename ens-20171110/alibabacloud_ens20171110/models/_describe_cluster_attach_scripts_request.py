# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterAttachScriptsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        nodepool_id: str = None,
        options: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.nodepool_id = nodepool_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        if self.options is not None:
            result['Options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        return self

