# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateChatRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        digital_employee_name: str = None,
        messages: List[main_models.CreateChatRequestMessages] = None,
        thread_id: str = None,
        variables: Dict[str, Any] = None,
    ):
        self.action = action
        self.digital_employee_name = digital_employee_name
        self.messages = messages
        self.thread_id = thread_id
        self.variables = variables

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
        if self.action is not None:
            result['action'] = self.action

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.variables is not None:
            result['variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.CreateChatRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        return self

class CreateChatRequestMessages(DaraModel):
    def __init__(
        self,
        contents: List[main_models.CreateChatRequestMessagesContents] = None,
        message_id: str = None,
        role: str = None,
        tools: List[Dict[str, Any]] = None,
    ):
        self.contents = contents
        self.message_id = message_id
        self.role = role
        self.tools = tools

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['contents'].append(k1.to_map() if k1 else None)

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.role is not None:
            result['role'] = self.role

        if self.tools is not None:
            result['tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('contents') is not None:
            for k1 in m.get('contents'):
                temp_model = main_models.CreateChatRequestMessagesContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('tools') is not None:
            self.tools = m.get('tools')

        return self

class CreateChatRequestMessagesContents(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

