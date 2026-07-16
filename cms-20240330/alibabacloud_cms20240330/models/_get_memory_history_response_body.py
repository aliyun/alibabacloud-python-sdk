# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetMemoryHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.GetMemoryHistoryResponseBodyResults] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return value.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.GetMemoryHistoryResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class GetMemoryHistoryResponseBodyResults(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        event: str = None,
        id: str = None,
        input: List[main_models.GetMemoryHistoryResponseBodyResultsInput] = None,
        memory_id: str = None,
        metadata: Dict[str, Any] = None,
        new_memory: str = None,
        old_memory: str = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        # Creation time.
        self.created_at = created_at
        # Event type.
        self.event = event
        # Memory ID.
        self.id = id
        # Original message.
        self.input = input
        # Memory ID.
        self.memory_id = memory_id
        # Metadata.
        self.metadata = metadata
        # New memory.
        self.new_memory = new_memory
        # Old memory.
        self.old_memory = old_memory
        # Update time.
        self.updated_at = updated_at
        # User ID.
        self.user_id = user_id

    def validate(self):
        if self.input:
            for v1 in self.input:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.event is not None:
            result['event'] = self.event

        if self.id is not None:
            result['id'] = self.id

        result['input'] = []
        if self.input is not None:
            for k1 in self.input:
                result['input'].append(k1.to_map() if k1 else None)

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.new_memory is not None:
            result['newMemory'] = self.new_memory

        if self.old_memory is not None:
            result['oldMemory'] = self.old_memory

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.input = []
        if m.get('input') is not None:
            for k1 in m.get('input'):
                temp_model = main_models.GetMemoryHistoryResponseBodyResultsInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('newMemory') is not None:
            self.new_memory = m.get('newMemory')

        if m.get('oldMemory') is not None:
            self.old_memory = m.get('oldMemory')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetMemoryHistoryResponseBodyResultsInput(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # Message content.
        self.content = content
        # Message sender role.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

