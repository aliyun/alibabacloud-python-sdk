# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AddMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        async_mode: bool = None,
        custom_instructions: str = None,
        infer: bool = None,
        messages: List[main_models.AddMemoriesRequestMessages] = None,
        metadata: Dict[str, Any] = None,
        run_id: str = None,
        timestamp: int = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.async_mode = async_mode
        self.custom_instructions = custom_instructions
        self.infer = infer
        self.messages = messages
        self.metadata = metadata
        self.run_id = run_id
        self.timestamp = timestamp
        self.user_id = user_id

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.async_mode is not None:
            result['asyncMode'] = self.async_mode

        if self.custom_instructions is not None:
            result['customInstructions'] = self.custom_instructions

        if self.infer is not None:
            result['infer'] = self.infer

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('asyncMode') is not None:
            self.async_mode = m.get('asyncMode')

        if m.get('customInstructions') is not None:
            self.custom_instructions = m.get('customInstructions')

        if m.get('infer') is not None:
            self.infer = m.get('infer')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.AddMemoriesRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class AddMemoriesRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
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

