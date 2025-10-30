# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAINodeRequest(DaraModel):
    def __init__(
        self,
        ainode_num: int = None,
        ainode_pool_id: str = None,
        dbinstance_id: str = None,
        node_names: List[str] = None,
    ):
        # This parameter is required.
        self.ainode_num = ainode_num
        self.ainode_pool_id = ainode_pool_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ainode_num is not None:
            result['AINodeNum'] = self.ainode_num

        if self.ainode_pool_id is not None:
            result['AINodePoolId'] = self.ainode_pool_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AINodeNum') is not None:
            self.ainode_num = m.get('AINodeNum')

        if m.get('AINodePoolId') is not None:
            self.ainode_pool_id = m.get('AINodePoolId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        return self

