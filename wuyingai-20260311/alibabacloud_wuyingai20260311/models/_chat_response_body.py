# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_wuyingai20260311 import models as main_models
from darabonba.model import DaraModel

class ChatResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: List[main_models.ChatResponseBodyContent] = None,
        created: str = None,
        created_at: str = None,
        http_status_code: int = None,
        id: str = None,
        message: str = None,
        object: str = None,
        request_id: str = None,
        role: str = None,
        sequence_number: str = None,
        session_id: str = None,
        status: str = None,
        success: bool = None,
        text: str = None,
        trace_id: str = None,
        type: str = None,
    ):
        # The business status code.
        self.code = code
        # The content block list (included only when Status is completed).
        self.content = content
        # （已废弃）创建时间戳
        self.created = created
        # The creation timestamp (Unix seconds).
        self.created_at = created_at
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The unique message identifier.
        self.id = id
        # The error details (returned on failure).
        self.message = message
        # The event object type.
        self.object = object
        # The request ID.
        self.request_id = request_id
        # The role (user / assistant / system / tool).
        self.role = role
        # The event sequence number (an incrementing integer in string format, used to guarantee ordering). Note: When StreamOptions filters out certain event types, the filtered events still consume sequence numbers. Therefore, the sequence numbers received by the client may not be contiguous.
        self.sequence_number = sequence_number
        # The session ID.
        self.session_id = session_id
        # The reply status (created / in_progress / completed).
        self.status = status
        # Indicates whether the request is successful.
        self.success = success
        # The incremental text content (included in Object=content events).
        # [_single.resp.200.props.Created.desc](Deprecated) The creation timestamp.
        self.text = text
        self.trace_id = trace_id
        # The message type (reasoning (model thinking process) / message (formal reply)).
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
        if self.code is not None:
            result['Code'] = self.code

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.created is not None:
            result['Created'] = self.created

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.object is not None:
            result['Object'] = self.object

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

        if self.success is not None:
            result['Success'] = self.success

        if self.text is not None:
            result['Text'] = self.text

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ChatResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Object') is not None:
            self.object = m.get('Object')

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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ChatResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        object: str = None,
        text: str = None,
        type: str = None,
    ):
        # The structured data (such as tool invocation). Example: {"call_id":"call_xxx","name":"get_weather", "output":"Tool output details in text format"}.
        self.data = data
        # The object type.
        self.object = object
        # The text content.
        self.text = text
        # The content type ("text" / "data").
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.object is not None:
            result['Object'] = self.object

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

