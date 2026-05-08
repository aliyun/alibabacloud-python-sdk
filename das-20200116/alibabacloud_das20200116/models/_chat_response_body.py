# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ChatResponseBody(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        content: str = None,
        delta: str = None,
        message_id: str = None,
        name: str = None,
        parent_message_id: str = None,
        role: str = None,
        run_id: str = None,
        step_name: str = None,
        task_tracker_id: str = None,
        thread_id: str = None,
        tool_call_id: str = None,
        tool_call_name: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.activity_type = activity_type
        self.content = content
        self.delta = delta
        self.message_id = message_id
        self.name = name
        self.parent_message_id = parent_message_id
        self.role = role
        self.run_id = run_id
        self.step_name = step_name
        self.task_tracker_id = task_tracker_id
        self.thread_id = thread_id
        self.tool_call_id = tool_call_id
        self.tool_call_name = tool_call_name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.content is not None:
            result['Content'] = self.content

        if self.delta is not None:
            result['Delta'] = self.delta

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id

        if self.role is not None:
            result['Role'] = self.role

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.task_tracker_id is not None:
            result['TaskTrackerId'] = self.task_tracker_id

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.tool_call_id is not None:
            result['ToolCallId'] = self.tool_call_id

        if self.tool_call_name is not None:
            result['ToolCallName'] = self.tool_call_name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Delta') is not None:
            self.delta = m.get('Delta')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TaskTrackerId') is not None:
            self.task_tracker_id = m.get('TaskTrackerId')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('ToolCallId') is not None:
            self.tool_call_id = m.get('ToolCallId')

        if m.get('ToolCallName') is not None:
            self.tool_call_name = m.get('ToolCallName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

