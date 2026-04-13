# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class CreateChatResponseBody(DaraModel):
    def __init__(
        self,
        answer: main_models.ChatDetail = None,
        chat_id: str = None,
        error_code: str = None,
        error_message: str = None,
        gmt_create_time: str = None,
        request_id: str = None,
        session_id: str = None,
        status: str = None,
    ):
        self.answer = answer
        self.chat_id = chat_id
        self.error_code = error_code
        self.error_message = error_message
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.gmt_create_time = gmt_create_time
        self.request_id = request_id
        self.session_id = session_id
        self.status = status

    def validate(self):
        if self.answer:
            self.answer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = main_models.ChatDetail()
            self.answer = temp_model.from_map(m.get('Answer'))

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

