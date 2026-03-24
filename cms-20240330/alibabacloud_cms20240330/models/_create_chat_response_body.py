# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateChatResponseBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.CreateChatResponseBodyMessages] = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        # Messages list
        self.messages = messages
        # Unique identifier for the request
        self.request_id = request_id
        # Global identifier for the request trace
        self.trace_id = trace_id

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
        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.CreateChatResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CreateChatResponseBodyMessages(DaraModel):
    def __init__(
        self,
        agents: List[Dict[str, Any]] = None,
        artifacts: List[Dict[str, Any]] = None,
        call_id: str = None,
        contents: List[Dict[str, Any]] = None,
        detail: str = None,
        events: List[Dict[str, Any]] = None,
        parent_call_id: str = None,
        role: str = None,
        seq: int = None,
        timestamp: str = None,
        tools: List[Dict[str, Any]] = None,
        type: str = None,
        version: str = None,
    ):
        # Agents list
        self.agents = agents
        # Artifacts information
        self.artifacts = artifacts
        # Call ID of the current node
        self.call_id = call_id
        # Messages contents array
        self.contents = contents
        # Detailed information, such as tool progress description
        self.detail = detail
        # Events list
        self.events = events
        # Call ID of the parent node
        self.parent_call_id = parent_call_id
        # Message role
        self.role = role
        # Event sequence number. This number increments to preserve event order.
        self.seq = seq
        # UNIX timestamp (seconds)
        self.timestamp = timestamp
        # Tools calls array
        self.tools = tools
        # Special event type, such as done, error, or heartbeat
        self.type = type
        # Message version number
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agents is not None:
            result['agents'] = self.agents

        if self.artifacts is not None:
            result['artifacts'] = self.artifacts

        if self.call_id is not None:
            result['callId'] = self.call_id

        if self.contents is not None:
            result['contents'] = self.contents

        if self.detail is not None:
            result['detail'] = self.detail

        if self.events is not None:
            result['events'] = self.events

        if self.parent_call_id is not None:
            result['parentCallId'] = self.parent_call_id

        if self.role is not None:
            result['role'] = self.role

        if self.seq is not None:
            result['seq'] = self.seq

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.tools is not None:
            result['tools'] = self.tools

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agents') is not None:
            self.agents = m.get('agents')

        if m.get('artifacts') is not None:
            self.artifacts = m.get('artifacts')

        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        if m.get('contents') is not None:
            self.contents = m.get('contents')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('events') is not None:
            self.events = m.get('events')

        if m.get('parentCallId') is not None:
            self.parent_call_id = m.get('parentCallId')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('seq') is not None:
            self.seq = m.get('seq')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('tools') is not None:
            self.tools = m.get('tools')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

