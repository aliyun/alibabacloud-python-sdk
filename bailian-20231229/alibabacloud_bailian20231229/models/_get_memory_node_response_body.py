# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMemoryNodeResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        memory_id: str = None,
        memory_node_id: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The content of the memory fragment.
        self.content = content
        # The long-term memory ID.
        self.memory_id = memory_id
        # The memory fragment ID.
        self.memory_node_id = memory_node_id
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

