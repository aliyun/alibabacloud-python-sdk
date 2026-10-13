# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class AddMemoriesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.AddMemoriesRequestBody = None,
    ):
        # The memory write request.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.AddMemoriesRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class AddMemoriesRequestBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AddMemoriesRequestBodyMessages] = None,
        metadata: Dict[str, str] = None,
        reference_time: str = None,
        scope: main_models.AddMemoriesRequestBodyScope = None,
        sync: bool = None,
        text: str = None,
    ):
        # The list of messages. You must provide either this parameter or Text, but not both. You can specify 1 to 20 messages, and the total size of Content must not exceed 32,000 UTF-8 bytes.
        self.messages = messages
        # The string key-value metadata. You can specify up to 16 keys. The maximum length of a key is 64 characters, and the maximum length of a value is 1,024 characters.
        self.metadata = metadata
        # The time reference point for this batch of messages or text. The time must be in RFC 3339 format with a time zone and support fractional seconds.
        self.reference_time = reference_time
        # The write scope. UserId, AgentId, and SessionId are all optional.
        self.scope = scope
        # Specifies whether to synchronously wait for memory extraction to complete. Default value: true.
        self.sync = sync
        # The text to be written directly. You must provide either this parameter or Messages, but not both. The text size must not exceed 32,000 UTF-8 bytes.
        self.text = text

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.reference_time is not None:
            result['referenceTime'] = self.reference_time

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.sync is not None:
            result['sync'] = self.sync

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.AddMemoriesRequestBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('referenceTime') is not None:
            self.reference_time = m.get('referenceTime')

        if m.get('scope') is not None:
            temp_model = main_models.AddMemoriesRequestBodyScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('sync') is not None:
            self.sync = m.get('sync')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class AddMemoriesRequestBodyScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The length is limited to 1 to 128 UTF-8 bytes. The ID cannot contain a forward slash (/) or an asterisk (*).
        self.agent_id = agent_id
        # The session ID. The length is limited to 1 to 128 UTF-8 bytes. The ID cannot contain a forward slash (/) or an asterisk (*).
        self.session_id = session_id
        # The user ID. The length is limited to 1 to 128 UTF-8 bytes. The ID cannot contain a forward slash (/) or an asterisk (*).
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



class AddMemoriesRequestBodyMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The message content.
        # 
        # This parameter is required.
        self.content = content
        # The message role.
        # 
        # This parameter is required.
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

