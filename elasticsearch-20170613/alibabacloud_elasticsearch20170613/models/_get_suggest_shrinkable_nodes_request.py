# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSuggestShrinkableNodesRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        ignore_status: bool = None,
        node_type: str = None,
    ):
        # The number of nodes that you want to remove.
        # 
        # This parameter is required.
        self.count = count
        # Specifies whether to ignore the instance status. Default value: false.
        self.ignore_status = ignore_status
        # The type of removing nodes. WORKER indicates hot node and WORKER_WARM indicates warm node.
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

        if self.ignore_status is not None:
            result['ignoreStatus'] = self.ignore_status

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('ignoreStatus') is not None:
            self.ignore_status = m.get('ignoreStatus')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        return self

