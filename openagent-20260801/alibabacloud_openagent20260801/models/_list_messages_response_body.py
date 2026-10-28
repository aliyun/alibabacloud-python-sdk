# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_openagent20260801 import models as main_models
from darabonba.model import DaraModel

class ListMessagesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMessagesResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The message history and pagination information.
        self.data = data
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates success.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        session_id: str = None,
        timeline: List[main_models.ListMessagesResponseBodyDataTimeline] = None,
        total: int = None,
    ):
        # The pagination token for the next page. A value of null indicates that no more data is available.
        self.next_token = next_token
        # The ID of the session to which the messages belong.
        self.session_id = session_id
        # The message records returned in a timeline.
        self.timeline = timeline
        # The number of timeline records on the current page, which is equal to the length of the timeline array.
        self.total = total

    def validate(self):
        if self.timeline:
            for v1 in self.timeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        result['timeline'] = []
        if self.timeline is not None:
            for k1 in self.timeline:
                result['timeline'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        self.timeline = []
        if m.get('timeline') is not None:
            for k1 in m.get('timeline'):
                temp_model = main_models.ListMessagesResponseBodyDataTimeline()
                self.timeline.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMessagesResponseBodyDataTimeline(DaraModel):
    def __init__(
        self,
        message: main_models.ListMessagesResponseBodyDataTimelineMessage = None,
        run_id: str = None,
    ):
        # The message object. Different message types are distinguished by role, and each type uses the corresponding fields.
        self.message = message
        # The ID of the run to which the message belongs.
        self.run_id = run_id

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message.to_map()

        if self.run_id is not None:
            result['runId'] = self.run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            temp_model = main_models.ListMessagesResponseBodyDataTimelineMessage()
            self.message = temp_model.from_map(m.get('message'))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        return self

class ListMessagesResponseBodyDataTimelineMessage(DaraModel):
    def __init__(
        self,
        activity_type: str = None,
        content: Any = None,
        encrypted_value: str = None,
        error: str = None,
        id: str = None,
        interrupt_outcome: main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcome = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        resume_input: main_models.ListMessagesResponseBodyDataTimelineMessageResumeInput = None,
        role: str = None,
        tool_call_id: str = None,
        tool_calls: List[main_models.ListMessagesResponseBodyDataTimelineMessageToolCalls] = None,
    ):
        # The type identifier of the activity message.
        self.activity_type = activity_type
        # The message content. The structure is determined by the message type.
        self.content = content
        # The encrypted content. The example is an invalid placeholder value and does not contain real ciphertext.
        self.encrypted_value = encrypted_value
        # The error description when tool execution fails.
        self.error = error
        # The message ID.
        self.id = id
        # The result information of historical interrupts.
        self.interrupt_outcome = interrupt_outcome
        # The extended metadata of the message.
        self.metadata = metadata
        # The name of the message sender.
        self.name = name
        # The resume input corresponding to the historical interrupt.
        self.resume_input = resume_input
        # The role of the message. Valid values: `user` (user message), `assistant` (assistant message), `tool` (tool result), `activity` (activity message), `reasoning` (reasoning message), and `interrupt` (interrupt record).
        self.role = role
        # The ID of the tool invocation associated with the tool result.
        self.tool_call_id = tool_call_id
        # The list of tool invocations initiated by the agent.
        self.tool_calls = tool_calls

    def validate(self):
        if self.interrupt_outcome:
            self.interrupt_outcome.validate()
        if self.resume_input:
            self.resume_input.validate()
        if self.tool_calls:
            for v1 in self.tool_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_type is not None:
            result['activityType'] = self.activity_type

        if self.content is not None:
            result['content'] = self.content

        if self.encrypted_value is not None:
            result['encryptedValue'] = self.encrypted_value

        if self.error is not None:
            result['error'] = self.error

        if self.id is not None:
            result['id'] = self.id

        if self.interrupt_outcome is not None:
            result['interruptOutcome'] = self.interrupt_outcome.to_map()

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.resume_input is not None:
            result['resumeInput'] = self.resume_input.to_map()

        if self.role is not None:
            result['role'] = self.role

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        result['toolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['toolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityType') is not None:
            self.activity_type = m.get('activityType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('encryptedValue') is not None:
            self.encrypted_value = m.get('encryptedValue')

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('interruptOutcome') is not None:
            temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcome()
            self.interrupt_outcome = temp_model.from_map(m.get('interruptOutcome'))

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resumeInput') is not None:
            temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageResumeInput()
            self.resume_input = temp_model.from_map(m.get('resumeInput'))

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        self.tool_calls = []
        if m.get('toolCalls') is not None:
            for k1 in m.get('toolCalls'):
                temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class ListMessagesResponseBodyDataTimelineMessageToolCalls(DaraModel):
    def __init__(
        self,
        encrypted_value: str = None,
        function: main_models.ListMessagesResponseBodyDataTimelineMessageToolCallsFunction = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
        type: str = None,
    ):
        # The encrypted content of the tool invocation. The example is only a placeholder value.
        self.encrypted_value = encrypted_value
        # The information about the function to be executed.
        self.function = function
        # The tool invocation ID.
        self.id = id
        # The extended metadata of the tool invocation.
        self.metadata = metadata
        # The type of the tool invocation. The value is fixed to `function`.
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_value is not None:
            result['encryptedValue'] = self.encrypted_value

        if self.function is not None:
            result['function'] = self.function.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encryptedValue') is not None:
            self.encrypted_value = m.get('encryptedValue')

        if m.get('function') is not None:
            temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageToolCallsFunction()
            self.function = temp_model.from_map(m.get('function'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListMessagesResponseBodyDataTimelineMessageToolCallsFunction(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        name: str = None,
    ):
        # The tool parameters in the form of a JSON string.
        self.arguments = arguments
        # The name of the function or tool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['arguments'] = self.arguments

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListMessagesResponseBodyDataTimelineMessageResumeInput(DaraModel):
    def __init__(
        self,
        resolved_at: str = None,
        resume: List[main_models.ListMessagesResponseBodyDataTimelineMessageResumeInputResume] = None,
        run_id: str = None,
        source: str = None,
    ):
        # The time when the interrupt processing was completed, in RFC 3339 format.
        self.resolved_at = resolved_at
        # The submitted processing results for each interrupt.
        self.resume = resume
        # The ID of the original run that was resumed.
        self.run_id = run_id
        # The source of the resume request. Valid values: `USER` (submitted by a user) and `INTERNAL` (submitted by an internal process).
        self.source = source

    def validate(self):
        if self.resume:
            for v1 in self.resume:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resolved_at is not None:
            result['resolvedAt'] = self.resolved_at

        result['resume'] = []
        if self.resume is not None:
            for k1 in self.resume:
                result['resume'].append(k1.to_map() if k1 else None)

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resolvedAt') is not None:
            self.resolved_at = m.get('resolvedAt')

        self.resume = []
        if m.get('resume') is not None:
            for k1 in m.get('resume'):
                temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageResumeInputResume()
                self.resume.append(temp_model.from_map(k1))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class ListMessagesResponseBodyDataTimelineMessageResumeInputResume(DaraModel):
    def __init__(
        self,
        interrupt_id: str = None,
        payload: Any = None,
        status: str = None,
    ):
        # The ID of the processed interrupt.
        self.interrupt_id = interrupt_id
        # The processing result for the corresponding interrupt, which must comply with the responseSchema of the interrupt.
        self.payload = payload
        # The response method for the current interrupt. Valid values: `resolved` (the answer, confirmation, or tool result required by the interrupt has been submitted, including the `payload`) and `cancelled` (the interrupt has been canceled, excluding the `payload`).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interrupt_id is not None:
            result['interruptId'] = self.interrupt_id

        if self.payload is not None:
            result['payload'] = self.payload

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interruptId') is not None:
            self.interrupt_id = m.get('interruptId')

        if m.get('payload') is not None:
            self.payload = m.get('payload')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListMessagesResponseBodyDataTimelineMessageInterruptOutcome(DaraModel):
    def __init__(
        self,
        interrupts: List[main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterrupts] = None,
        type: str = None,
    ):
        # The list of historical interrupts.
        self.interrupts = interrupts
        # The type of the interrupt result. The value is fixed to `interrupt`.
        self.type = type

    def validate(self):
        if self.interrupts:
            for v1 in self.interrupts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['interrupts'] = []
        if self.interrupts is not None:
            for k1 in self.interrupts:
                result['interrupts'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interrupts = []
        if m.get('interrupts') is not None:
            for k1 in m.get('interrupts'):
                temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterrupts()
                self.interrupts.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterrupts(DaraModel):
    def __init__(
        self,
        data: main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsData = None,
        expires_at: str = None,
        id: str = None,
        message: str = None,
        metadata: Dict[str, Any] = None,
        reason: str = None,
        response_schema: Dict[str, Any] = None,
        tool_call_id: str = None,
    ):
        # The supplementary business data for the interrupt.
        self.data = data
        # The expiration time of the interrupt, in RFC 3339 format.
        self.expires_at = expires_at
        # The interrupt ID.
        self.id = id
        # The interrupt prompt displayed to the user.
        self.message = message
        # The extended metadata of the interrupt.
        self.metadata = metadata
        # The reason for the interrupt. Valid values: `tool_call` (tool invocation requires processing), `input_required` (user input is required), `confirmation` (confirmation is required), and `out_of_band_approval` (waiting for out-of-band approval).
        self.reason = reason
        # The JSON schema that the resume result payload must follow.
        self.response_schema = response_schema
        # The ID of the tool invocation associated with the interrupt.
        self.tool_call_id = tool_call_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.id is not None:
            result['id'] = self.id

        if self.message is not None:
            result['message'] = self.message

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.reason is not None:
            result['reason'] = self.reason

        if self.response_schema is not None:
            result['responseSchema'] = self.response_schema

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('responseSchema') is not None:
            self.response_schema = m.get('responseSchema')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        return self

class ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsData(DaraModel):
    def __init__(
        self,
        api_calls: List[main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsDataApiCalls] = None,
        approval_id: str = None,
        approval_url: str = None,
        cancellable: bool = None,
        change_digest: str = None,
        title: str = None,
    ):
        # The list of API operations that require approval.
        self.api_calls = api_calls
        # The associated approval ID.
        self.approval_id = approval_id
        # The URL of the approval page. The example URL cannot be used for actual approval.
        self.approval_url = approval_url
        # Specifies whether the approval can be canceled.
        self.cancellable = cancellable
        # The digest identifier of the change pending approval.
        self.change_digest = change_digest
        # The title of the approval item.
        self.title = title

    def validate(self):
        if self.api_calls:
            for v1 in self.api_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiCalls'] = []
        if self.api_calls is not None:
            for k1 in self.api_calls:
                result['apiCalls'].append(k1.to_map() if k1 else None)

        if self.approval_id is not None:
            result['approvalId'] = self.approval_id

        if self.approval_url is not None:
            result['approvalUrl'] = self.approval_url

        if self.cancellable is not None:
            result['cancellable'] = self.cancellable

        if self.change_digest is not None:
            result['changeDigest'] = self.change_digest

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_calls = []
        if m.get('apiCalls') is not None:
            for k1 in m.get('apiCalls'):
                temp_model = main_models.ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsDataApiCalls()
                self.api_calls.append(temp_model.from_map(k1))

        if m.get('approvalId') is not None:
            self.approval_id = m.get('approvalId')

        if m.get('approvalUrl') is not None:
            self.approval_url = m.get('approvalUrl')

        if m.get('cancellable') is not None:
            self.cancellable = m.get('cancellable')

        if m.get('changeDigest') is not None:
            self.change_digest = m.get('changeDigest')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class ListMessagesResponseBodyDataTimelineMessageInterruptOutcomeInterruptsDataApiCalls(DaraModel):
    def __init__(
        self,
        action: str = None,
        description: str = None,
    ):
        # The name of the API action.
        self.action = action
        # The description of the operation pending approval.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

