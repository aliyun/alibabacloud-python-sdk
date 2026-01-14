# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListMemoryNodesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        memory_nodes: List[main_models.ListMemoryNodesResponseBodyMemoryNodes] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.memory_nodes = memory_nodes
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.memory_nodes:
            for v1 in self.memory_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['memoryNodes'] = []
        if self.memory_nodes is not None:
            for k1 in self.memory_nodes:
                result['memoryNodes'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.memory_nodes = []
        if m.get('memoryNodes') is not None:
            for k1 in m.get('memoryNodes'):
                temp_model = main_models.ListMemoryNodesResponseBodyMemoryNodes()
                self.memory_nodes.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMemoryNodesResponseBodyMemoryNodes(DaraModel):
    def __init__(
        self,
        content: str = None,
        memory_node_id: str = None,
    ):
        self.content = content
        self.memory_node_id = memory_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.memory_node_id is not None:
            result['memoryNodeId'] = self.memory_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('memoryNodeId') is not None:
            self.memory_node_id = m.get('memoryNodeId')

        return self

