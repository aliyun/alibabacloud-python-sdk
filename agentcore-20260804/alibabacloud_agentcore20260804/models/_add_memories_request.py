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
        # The write memory request.
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
        extract: bool = None,
        memories: List[main_models.AddMemoriesRequestBodyMemories] = None,
        messages: List[main_models.AddMemoriesRequestBodyMessages] = None,
        metadata: Dict[str, str] = None,
        reference_time: str = None,
        scope: main_models.AddMemoriesRequestBodyScope = None,
        sync: bool = None,
        text: str = None,
    ):
        # Specifies whether to extract memories. If omitted or set to true, memories are extracted from text or messages. If set to false, memories are directly written.
        self.extract = extract
        # The list of memories to be directly written when extract is set to false. The list can contain 1 to 100 memories. You cannot provide text, messages, referenceTime, or request-level metadata at the same time.
        self.memories = memories
        # The list of messages. You must provide either text or messages, but not both. The list can contain 1 to 20 messages, and the total length of the content cannot exceed 32,000 UTF-8 bytes.
        self.messages = messages
        # The string key-value metadata. A maximum of 16 keys are supported. A key can be up to 64 characters in length, and a value can be up to 1,024 characters in length.
        self.metadata = metadata
        # The time reference point for the batch of messages or text. It uses the RFC 3339 format with a time zone and supports fractional seconds.
        self.reference_time = reference_time
        # The write scope. UserId, AgentId, and SessionId are all optional.
        self.scope = scope
        # Specifies whether to synchronously wait for the memory extraction to complete. Default value: true.
        self.sync = sync
        # The text to be directly written. You must provide either text or messages, but not both. The text cannot exceed 32,000 UTF-8 bytes.
        self.text = text

    def validate(self):
        if self.memories:
            for v1 in self.memories:
                 if v1:
                    v1.validate()
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
        if self.extract is not None:
            result['extract'] = self.extract

        result['memories'] = []
        if self.memories is not None:
            for k1 in self.memories:
                result['memories'].append(k1.to_map() if k1 else None)

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
        if m.get('extract') is not None:
            self.extract = m.get('extract')

        self.memories = []
        if m.get('memories') is not None:
            for k1 in m.get('memories'):
                temp_model = main_models.AddMemoriesRequestBodyMemories()
                self.memories.append(temp_model.from_map(k1))

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
        team_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain a forward slash (/) or an asterisk (*).
        self.agent_id = agent_id
        # The session ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain a forward slash (/) or an asterisk (*).
        self.session_id = session_id
        # The business team ID defined by the caller. It cannot be empty when provided and can be up to 128 UTF-8 bytes in length.
        self.team_id = team_id
        # The user ID. The length is limited to 1 to 128 UTF-8 bytes. It cannot contain a forward slash (/) or an asterisk (*).
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

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class AddMemoriesRequestBodyMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        reference_time: str = None,
        role: str = None,
    ):
        # The content of the message.
        # 
        # This parameter is required.
        self.content = content
        # The reference time of the message in RFC 3339 format with a time zone. If omitted, the request-level referenceTime is used. If both are omitted, the time of the current request is used.
        self.reference_time = reference_time
        # The role of the message.
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

        if self.reference_time is not None:
            result['referenceTime'] = self.reference_time

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('referenceTime') is not None:
            self.reference_time = m.get('referenceTime')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self



class AddMemoriesRequestBodyMemories(DaraModel):
    def __init__(
        self,
        metadata: Dict[str, str] = None,
        text: str = None,
        type: str = None,
    ):
        # The string key-value tags set by the caller. A maximum of 16 tags are supported. A key can be up to 64 Unicode characters in length, and a value can be up to 1,024 Unicode characters in length. Empty strings are allowed. Nested objects or arrays are not supported.
        self.metadata = metadata
        # The content of the memory to be directly written. It cannot be empty and can be up to 32,000 UTF-8 bytes in length.
        self.text = text
        # The content type of the memory. Valid values: semantic for semantic memory, skill for skill, user_profile for user preference, and session_summary for session summary.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

