# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskContentV2Request(DaraModel):
    def __init__(
        self,
        node_content: str = None,
        node_id: str = None,
    ):
        # The node configurations after modification.
        # 
        # >  We recommend that you change the SQL type from SELECT to INSERT/CREATE.
        self.node_content = node_content
        # The ID of the task node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

