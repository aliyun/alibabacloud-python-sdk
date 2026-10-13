# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetMemoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMemoryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The long-term memory details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetMemoryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMemoryResponseBodyData(DaraModel):
    def __init__(
        self,
        content: main_models.GetMemoryResponseBodyDataContent = None,
        created_at: str = None,
        memory_id: str = None,
        metadata: Dict[str, str] = None,
        scope: main_models.GetMemoryResponseBodyDataScope = None,
        updated_at: str = None,
    ):
        # The memory content.
        self.content = content
        # The creation time.
        self.created_at = created_at
        # The long-term memory ID.
        self.memory_id = memory_id
        # The memory metadata.
        self.metadata = metadata
        # The memory scope.
        self.scope = scope
        # The last update time.
        self.updated_at = updated_at

    def validate(self):
        if self.content:
            self.content.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = main_models.GetMemoryResponseBodyDataContent()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('scope') is not None:
            temp_model = main_models.GetMemoryResponseBodyDataScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetMemoryResponseBodyDataScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain / or *. This field is not returned if the memory is not associated with an agent ID.
        self.agent_id = agent_id
        # The session ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain / or *. This field is not returned if the memory is not associated with a session ID.
        self.session_id = session_id
        # The user ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain / or *. This field is not returned if the memory is not associated with a user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetMemoryResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        # The memory text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

