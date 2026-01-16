# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTransferableNodesRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        node_type: str = None,
    ):
        # The number of nodes to be migrated.
        # 
        # This parameter is required.
        self.count = count
        # The type of nodes.**WORKER**represents a hot node,**WORKER_WARM** represents a warm node.
        # 
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        return self

