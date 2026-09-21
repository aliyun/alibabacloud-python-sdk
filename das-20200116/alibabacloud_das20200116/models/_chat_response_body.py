# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ChatResponseBody(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        agent_id: str = None,
        content: str = None,
        delta: str = None,
        kind: str = None,
        label: str = None,
        message_id: str = None,
        name: str = None,
        originating_tool_call_id: str = None,
        parent_agent_id: str = None,
        parent_message_id: str = None,
        role: str = None,
        run_id: str = None,
        step_name: str = None,
        step_status: str = None,
        task_tracker_id: str = None,
        thread_id: str = None,
        timestamp: int = None,
        tool_call_error: str = None,
        tool_call_id: str = None,
        tool_call_name: str = None,
        type: str = None,
        value: Any = None,
    ):
        # The heartbeat.
        self.activity_type = activity_type
        # The agent ID.
        self.agent_id = agent_id
        # The response content.
        self.content = content
        # Indicates whether the content is incremental.
        self.delta = delta
        # The step type of STEP_STARTED, such as task.
        self.kind = kind
        # The display name of the sub-agent for STEP_STARTED.
        self.label = label
        # The message ID.
        self.message_id = message_id
        # The extension key.
        self.name = name
        # The original ID of the tool call.
        self.originating_tool_call_id = originating_tool_call_id
        # The parent agent ID.
        self.parent_agent_id = parent_agent_id
        # The parent message ID.
        self.parent_message_id = parent_message_id
        # The conversation role ID.
        self.role = role
        # The run ID.
        self.run_id = run_id
        # The execution step name.
        self.step_name = step_name
        # The step status of STEP_FINISHED, such as completed.
        self.step_status = step_status
        # The callback utility class.
        self.task_tracker_id = task_tracker_id
        # The thread ID.
        self.thread_id = thread_id
        # The event timestamp.
        self.timestamp = timestamp
        # The error that occurred during tool invocation.
        self.tool_call_error = tool_call_error
        # The tool invocation ID.
        self.tool_call_id = tool_call_id
        # The tool name.
        self.tool_call_name = tool_call_name
        # The event type.
        self.type = type
        # The extension value.
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

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.content is not None:
            result['Content'] = self.content

        if self.delta is not None:
            result['Delta'] = self.delta

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.label is not None:
            result['Label'] = self.label

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.name is not None:
            result['Name'] = self.name

        if self.originating_tool_call_id is not None:
            result['OriginatingToolCallId'] = self.originating_tool_call_id

        if self.parent_agent_id is not None:
            result['ParentAgentId'] = self.parent_agent_id

        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id

        if self.role is not None:
            result['Role'] = self.role

        if self.run_id is not None:
            result['RunId'] = self.run_id

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.step_status is not None:
            result['StepStatus'] = self.step_status

        if self.task_tracker_id is not None:
            result['TaskTrackerId'] = self.task_tracker_id

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.tool_call_error is not None:
            result['ToolCallError'] = self.tool_call_error

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

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Delta') is not None:
            self.delta = m.get('Delta')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginatingToolCallId') is not None:
            self.originating_tool_call_id = m.get('OriginatingToolCallId')

        if m.get('ParentAgentId') is not None:
            self.parent_agent_id = m.get('ParentAgentId')

        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')

        if m.get('TaskTrackerId') is not None:
            self.task_tracker_id = m.get('TaskTrackerId')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ToolCallError') is not None:
            self.tool_call_error = m.get('ToolCallError')

        if m.get('ToolCallId') is not None:
            self.tool_call_id = m.get('ToolCallId')

        if m.get('ToolCallName') is not None:
            self.tool_call_name = m.get('ToolCallName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

