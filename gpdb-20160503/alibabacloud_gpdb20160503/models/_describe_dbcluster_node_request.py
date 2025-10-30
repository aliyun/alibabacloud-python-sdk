# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterNodeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_type: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The node type. Valid values:
        # 
        # *   **master**: coordinator node.
        # *   **segment**: compute node.
        # 
        # > If you do not specify this parameter, the information about all nodes is returned.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

