# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetMemoryHistoryResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.GetMemoryHistoryResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GetMemoryHistoryResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GetMemoryHistoryResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        memory_id: str = None,
        input: List[main_models.GetMemoryHistoryResponseBodyInput] = None,
        new_memory: str = None,
        user_id: str = None,
        event: str = None,
        created_at: str = None,
        updated_at: str = None,
        old_memory: str = None,
        metadata: Dict[str, Any] = None,
    ):
        self.id = id
        self.memory_id = memory_id
        self.input = input
        self.new_memory = new_memory
        self.user_id = user_id
        self.event = event
        self.created_at = created_at
        self.updated_at = updated_at
        self.old_memory = old_memory
        self.metadata = metadata

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
        if self.id is not None:
            result['id'] = self.id

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        result['input'] = []
        if self.input is not None:
            for k1 in self.input:
                result['input'].append(k1.to_map() if k1 else None)

        if self.new_memory is not None:
            result['newMemory'] = self.new_memory

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.event is not None:
            result['event'] = self.event

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.old_memory is not None:
            result['oldMemory'] = self.old_memory

        if self.metadata is not None:
            result['metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        self.input = []
        if m.get('input') is not None:
            for k1 in m.get('input'):
                temp_model = main_models.GetMemoryHistoryResponseBodyInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('newMemory') is not None:
            self.new_memory = m.get('newMemory')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('oldMemory') is not None:
            self.old_memory = m.get('oldMemory')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        return self

class GetMemoryHistoryResponseBodyInput(DaraModel):
    def __init__(
        self,
        role: str = None,
        content: str = None,
    ):
        self.role = role
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['role'] = self.role

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

