# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AguiMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        metadata: main_models.AguiMessageMetadata = None,
        role: str = None,
        tool_call_id: str = None,
        tool_calls: List[main_models.AguiMessageToolCalls] = None,
    ):
        self.content = content
        self.id = id
        self.metadata = metadata
        self.role = role
        self.tool_call_id = tool_call_id
        self.tool_calls = tool_calls

    def validate(self):
        if self.metadata:
            self.metadata.validate()
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
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.role is not None:
            result['Role'] = self.role

        if self.tool_call_id is not None:
            result['ToolCallId'] = self.tool_call_id

        result['ToolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['ToolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metadata') is not None:
            temp_model = main_models.AguiMessageMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('ToolCallId') is not None:
            self.tool_call_id = m.get('ToolCallId')

        self.tool_calls = []
        if m.get('ToolCalls') is not None:
            for k1 in m.get('ToolCalls'):
                temp_model = main_models.AguiMessageToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class AguiMessageToolCalls(DaraModel):
    def __init__(
        self,
        function: main_models.AguiMessageToolCallsFunction = None,
        id: str = None,
        type: str = None,
    ):
        self.function = function
        self.id = id
        self.type = type

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = main_models.AguiMessageToolCallsFunction()
            self.function = temp_model.from_map(m.get('Function'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AguiMessageToolCallsFunction(DaraModel):
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
            result['Arguments'] = self.arguments

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class AguiMessageMetadata(DaraModel):
    def __init__(
        self,
        attachments: main_models.AguiMessageMetadataAttachments = None,
    ):
        self.attachments = attachments

    def validate(self):
        if self.attachments:
            self.attachments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachments is not None:
            result['Attachments'] = self.attachments.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attachments') is not None:
            temp_model = main_models.AguiMessageMetadataAttachments()
            self.attachments = temp_model.from_map(m.get('Attachments'))

        return self



class AguiMessageMetadataAttachments(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

