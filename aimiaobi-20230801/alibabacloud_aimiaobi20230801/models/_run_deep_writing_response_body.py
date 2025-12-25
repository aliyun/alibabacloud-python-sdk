# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunDeepWritingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        header: main_models.RunDeepWritingResponseBodyHeader = None,
        http_status_code: str = None,
        message: str = None,
        payload: main_models.RunDeepWritingResponseBodyPayload = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.header = header
        self.http_status_code = http_status_code
        self.message = message
        self.payload = payload
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Header') is not None:
            temp_model = main_models.RunDeepWritingResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Payload') is not None:
            temp_model = main_models.RunDeepWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RunDeepWritingResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunDeepWritingResponseBodyPayloadOutput = None,
    ):
        self.output = output

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.RunDeepWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        return self

class RunDeepWritingResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        item: main_models.RunDeepWritingResponseBodyPayloadOutputItem = None,
        output_index: int = None,
        response: main_models.RunDeepWritingResponseBodyPayloadOutputResponse = None,
        sequence_number: str = None,
        type: str = None,
    ):
        self.item = item
        self.output_index = output_index
        self.response = response
        self.sequence_number = sequence_number
        self.type = type

    def validate(self):
        if self.item:
            self.item.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item.to_map()

        if self.output_index is not None:
            result['OutputIndex'] = self.output_index

        if self.response is not None:
            result['Response'] = self.response.to_map()

        if self.sequence_number is not None:
            result['SequenceNumber'] = self.sequence_number

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            temp_model = main_models.RunDeepWritingResponseBodyPayloadOutputItem()
            self.item = temp_model.from_map(m.get('Item'))

        if m.get('OutputIndex') is not None:
            self.output_index = m.get('OutputIndex')

        if m.get('Response') is not None:
            temp_model = main_models.RunDeepWritingResponseBodyPayloadOutputResponse()
            self.response = temp_model.from_map(m.get('Response'))

        if m.get('SequenceNumber') is not None:
            self.sequence_number = m.get('SequenceNumber')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunDeepWritingResponseBodyPayloadOutputResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        status: str = None,
    ):
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class RunDeepWritingResponseBodyPayloadOutputItem(DaraModel):
    def __init__(
        self,
        agent: str = None,
        arguments: str = None,
        content: List[main_models.RunDeepWritingResponseBodyPayloadOutputItemContent] = None,
        id: str = None,
        name: str = None,
        result: str = None,
        status: str = None,
        type: str = None,
    ):
        self.agent = agent
        self.arguments = arguments
        self.content = content
        self.id = id
        self.name = name
        self.result = result
        self.status = status
        self.type = type

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent

        if self.arguments is not None:
            result['Arguments'] = self.arguments

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            self.agent = m.get('Agent')

        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.RunDeepWritingResponseBodyPayloadOutputItemContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunDeepWritingResponseBodyPayloadOutputItemContent(DaraModel):
    def __init__(
        self,
        text: str = None,
        type: str = None,
    ):
        self.text = text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunDeepWritingResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.session_id = session_id
        self.status_code = status_code
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

