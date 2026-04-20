# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class DescribeChatMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_at: str = None,
        content: List[main_models.DescribeChatMessageResponseBodyContent] = None,
        created_at: str = None,
        data: main_models.DescribeChatMessageResponseBodyData = None,
        delta: bool = None,
        error: str = None,
        id: str = None,
        index: int = None,
        message: str = None,
        msg_id: str = None,
        object: str = None,
        output: str = None,
        request_id: str = None,
        role: str = None,
        sequence_number: int = None,
        session_id: str = None,
        status: str = None,
        text: str = None,
        type: str = None,
    ):
        self.code = code
        self.completed_at = completed_at
        self.content = content
        self.created_at = created_at
        self.data = data
        self.delta = delta
        self.error = error
        self.id = id
        self.index = index
        self.message = message
        self.msg_id = msg_id
        self.object = object
        self.output = output
        self.request_id = request_id
        self.role = role
        self.sequence_number = sequence_number
        self.session_id = session_id
        self.status = status
        self.text = text
        self.type = type

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.completed_at is not None:
            result['CompletedAt'] = self.completed_at

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.delta is not None:
            result['Delta'] = self.delta

        if self.error is not None:
            result['Error'] = self.error

        if self.id is not None:
            result['Id'] = self.id

        if self.index is not None:
            result['Index'] = self.index

        if self.message is not None:
            result['Message'] = self.message

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.object is not None:
            result['Object'] = self.object

        if self.output is not None:
            result['Output'] = self.output

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role

        if self.sequence_number is not None:
            result['SequenceNumber'] = self.sequence_number

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompletedAt') is not None:
            self.completed_at = m.get('CompletedAt')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeChatMessageResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeChatMessageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Delta') is not None:
            self.delta = m.get('Delta')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SequenceNumber') is not None:
            self.sequence_number = m.get('SequenceNumber')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeChatMessageResponseBodyData(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        call_id: str = None,
        name: str = None,
        output: str = None,
    ):
        self.arguments = arguments
        self.call_id = call_id
        self.name = name
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['Arguments'] = self.arguments

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

class DescribeChatMessageResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeChatMessageResponseBodyContentData = None,
        delta: bool = None,
        error: str = None,
        index: int = None,
        msg_id: str = None,
        object: str = None,
        sequence_number: int = None,
        status: str = None,
        text: str = None,
        type: str = None,
    ):
        self.data = data
        self.delta = delta
        self.error = error
        self.index = index
        self.msg_id = msg_id
        self.object = object
        self.sequence_number = sequence_number
        self.status = status
        self.text = text
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.delta is not None:
            result['Delta'] = self.delta

        if self.error is not None:
            result['Error'] = self.error

        if self.index is not None:
            result['Index'] = self.index

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.object is not None:
            result['Object'] = self.object

        if self.sequence_number is not None:
            result['SequenceNumber'] = self.sequence_number

        if self.status is not None:
            result['Status'] = self.status

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeChatMessageResponseBodyContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Delta') is not None:
            self.delta = m.get('Delta')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('SequenceNumber') is not None:
            self.sequence_number = m.get('SequenceNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeChatMessageResponseBodyContentData(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        name: str = None,
        output: str = None,
    ):
        self.call_id = call_id
        self.name = name
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

