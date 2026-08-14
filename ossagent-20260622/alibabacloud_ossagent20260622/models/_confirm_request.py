# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ossagent20260622 import models as main_models
from darabonba.model import DaraModel

class ConfirmRequest(DaraModel):
    def __init__(
        self,
        confirmed: bool = None,
        phase: str = None,
        reason: str = None,
        session_id: str = None,
        tool_calls: List[main_models.ConfirmRequestToolCalls] = None,
    ):
        # Specifies whether to approve the tool execution.
        self.confirmed = confirmed
        # The current execution phase.
        self.phase = phase
        # The reason for whether to call the tool.
        self.reason = reason
        # The Q&A session ID.
        self.session_id = session_id
        # The tool invocations.
        self.tool_calls = tool_calls

    def validate(self):
        if self.tool_calls:
            for v1 in self.tool_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirmed is not None:
            result['confirmed'] = self.confirmed

        if self.phase is not None:
            result['phase'] = self.phase

        if self.reason is not None:
            result['reason'] = self.reason

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        result['toolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['toolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confirmed') is not None:
            self.confirmed = m.get('confirmed')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        self.tool_calls = []
        if m.get('toolCalls') is not None:
            for k1 in m.get('toolCalls'):
                temp_model = main_models.ConfirmRequestToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class ConfirmRequestToolCalls(DaraModel):
    def __init__(
        self,
        id: str = None,
        modified_input: Dict[str, Any] = None,
        name: str = None,
    ):
        # The tool ID, returned by the Chat operation.
        self.id = id
        # The command to execute for the tool calling operation, returned by the Chat operation.
        self.modified_input = modified_input
        # The consumer name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.modified_input is not None:
            result['modifiedInput'] = self.modified_input

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedInput') is not None:
            self.modified_input = m.get('modifiedInput')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

