# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class InvokeAgentRequest(DaraModel):
    def __init__(
        self,
        context: List[main_models.InvokeAgentRequestContext] = None,
        forwarded_props: main_models.InvokeAgentRequestForwardedProps = None,
        messages: List[main_models.InvokeAgentRequestMessages] = None,
        parent_run_id: str = None,
        resume: List[main_models.InvokeAgentRequestResume] = None,
        run_id: str = None,
        state: Any = None,
        thread_id: str = None,
        tools: List[main_models.InvokeAgentRequestTools] = None,
    ):
        self.context = context
        self.forwarded_props = forwarded_props
        self.messages = messages
        self.parent_run_id = parent_run_id
        self.resume = resume
        self.run_id = run_id
        self.state = state
        self.thread_id = thread_id
        self.tools = tools

    def validate(self):
        if self.context:
            for v1 in self.context:
                 if v1:
                    v1.validate()
        if self.forwarded_props:
            self.forwarded_props.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.resume:
            for v1 in self.resume:
                 if v1:
                    v1.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['context'] = []
        if self.context is not None:
            for k1 in self.context:
                result['context'].append(k1.to_map() if k1 else None)

        if self.forwarded_props is not None:
            result['forwardedProps'] = self.forwarded_props.to_map()

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.parent_run_id is not None:
            result['parentRunId'] = self.parent_run_id

        result['resume'] = []
        if self.resume is not None:
            for k1 in self.resume:
                result['resume'].append(k1.to_map() if k1 else None)

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.state is not None:
            result['state'] = self.state

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.context = []
        if m.get('context') is not None:
            for k1 in m.get('context'):
                temp_model = main_models.InvokeAgentRequestContext()
                self.context.append(temp_model.from_map(k1))

        if m.get('forwardedProps') is not None:
            temp_model = main_models.InvokeAgentRequestForwardedProps()
            self.forwarded_props = temp_model.from_map(m.get('forwardedProps'))

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.InvokeAgentRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('parentRunId') is not None:
            self.parent_run_id = m.get('parentRunId')

        self.resume = []
        if m.get('resume') is not None:
            for k1 in m.get('resume'):
                temp_model = main_models.InvokeAgentRequestResume()
                self.resume.append(temp_model.from_map(k1))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.InvokeAgentRequestTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class InvokeAgentRequestTools(DaraModel):
    def __init__(
        self,
        description: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        parameters: Any = None,
    ):
        # This parameter is required.
        self.description = description
        self.metadata = metadata
        # This parameter is required.
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

class InvokeAgentRequestResume(DaraModel):
    def __init__(
        self,
        interrupt_id: str = None,
        payload: Any = None,
        status: str = None,
    ):
        self.interrupt_id = interrupt_id
        self.payload = payload
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

class InvokeAgentRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        encrypted_value: str = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        role: str = None,
        subagent_run_id: str = None,
        tool_call_id: str = None,
        tool_calls: List[main_models.InvokeAgentRequestMessagesToolCalls] = None,
    ):
        self.content = content
        self.encrypted_value = encrypted_value
        self.id = id
        self.metadata = metadata
        self.name = name
        self.role = role
        self.subagent_run_id = subagent_run_id
        self.tool_call_id = tool_call_id
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
        if self.content is not None:
            result['content'] = self.content

        if self.encrypted_value is not None:
            result['encryptedValue'] = self.encrypted_value

        if self.id is not None:
            result['id'] = self.id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.role is not None:
            result['role'] = self.role

        if self.subagent_run_id is not None:
            result['subagentRunId'] = self.subagent_run_id

        if self.tool_call_id is not None:
            result['toolCallId'] = self.tool_call_id

        result['toolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['toolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('encryptedValue') is not None:
            self.encrypted_value = m.get('encryptedValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('subagentRunId') is not None:
            self.subagent_run_id = m.get('subagentRunId')

        if m.get('toolCallId') is not None:
            self.tool_call_id = m.get('toolCallId')

        self.tool_calls = []
        if m.get('toolCalls') is not None:
            for k1 in m.get('toolCalls'):
                temp_model = main_models.InvokeAgentRequestMessagesToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class InvokeAgentRequestMessagesToolCalls(DaraModel):
    def __init__(
        self,
        encrypted_value: str = None,
        function: main_models.InvokeAgentRequestMessagesToolCallsFunction = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
        type: str = None,
    ):
        self.encrypted_value = encrypted_value
        self.function = function
        self.id = id
        self.metadata = metadata
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
            temp_model = main_models.InvokeAgentRequestMessagesToolCallsFunction()
            self.function = temp_model.from_map(m.get('function'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class InvokeAgentRequestMessagesToolCallsFunction(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        name: str = None,
    ):
        self.arguments = arguments
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

class InvokeAgentRequestForwardedProps(DaraModel):
    def __init__(
        self,
        enable_thinking: bool = None,
        language: str = None,
        source: str = None,
    ):
        self.enable_thinking = enable_thinking
        self.language = language
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_thinking is not None:
            result['enableThinking'] = self.enable_thinking

        if self.language is not None:
            result['language'] = self.language

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableThinking') is not None:
            self.enable_thinking = m.get('enableThinking')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class InvokeAgentRequestContext(DaraModel):
    def __init__(
        self,
        description: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

