# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListMemoriesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        memories: List[main_models.ListMemoriesResponseBodyMemories] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.memories = memories
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.workspace_id = workspace_id

    def validate(self):
        if self.memories:
            for v1 in self.memories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['memories'] = []
        if self.memories is not None:
            for k1 in self.memories:
                result['memories'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.memories = []
        if m.get('memories') is not None:
            for k1 in m.get('memories'):
                temp_model = main_models.ListMemoriesResponseBodyMemories()
                self.memories.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListMemoriesResponseBodyMemories(DaraModel):
    def __init__(
        self,
        description: str = None,
        memory_id: str = None,
    ):
        self.description = description
        self.memory_id = memory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        return self

