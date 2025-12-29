# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterNodePoolsRequest(DaraModel):
    def __init__(
        self,
        nodepool_name: str = None,
    ):
        # Node pool name.
        self.nodepool_name = nodepool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nodepool_name is not None:
            result['NodepoolName'] = self.nodepool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodepoolName') is not None:
            self.nodepool_name = m.get('NodepoolName')

        return self

