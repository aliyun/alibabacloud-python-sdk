# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
    ):
        # The number of nodes to add. For example, if the node pool currently has 2 nodes and you add 2 more, the total number of nodes becomes 4. Subject to the node quota limit of the current cluster, you can add a maximum of 500 nodes in a single operation.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        return self

