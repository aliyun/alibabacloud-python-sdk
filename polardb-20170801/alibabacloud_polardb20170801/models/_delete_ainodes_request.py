# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAINodesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnode_id: List[str] = None,
    ):
        # The cluster ID.
        # 
        # > Call the [DescribeAIDBClusters](https://api.aliyun.com/api/polardb/2017-08-01/DescribeAIDBClusters) operation to view the cluster ID.
        self.dbcluster_id = dbcluster_id
        # The IDs of the nodes to delete.
        self.dbnode_id = dbnode_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        return self

