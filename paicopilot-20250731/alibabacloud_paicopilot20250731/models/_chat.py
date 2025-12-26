# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class Chat(DaraModel):
    def __init__(
        self,
        answer: main_models.ChatDetail = None,
        chat_id: str = None,
        extra_data: str = None,
        gmt_create_time: str = None,
        gmt_modified: str = None,
        message: str = None,
        owner_id: str = None,
        question: main_models.ChatDetail = None,
        session_id: str = None,
        status: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.answer = answer
        self.chat_id = chat_id
        self.extra_data = extra_data
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified = gmt_modified
        self.message = message
        self.owner_id = owner_id
        self.question = question
        self.session_id = session_id
        self.status = status
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.answer:
            self.answer.validate()
        if self.question:
            self.question.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.question is not None:
            result['Question'] = self.question.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = main_models.ChatDetail()
            self.answer = temp_model.from_map(m.get('Answer'))

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Question') is not None:
            temp_model = main_models.ChatDetail()
            self.question = temp_model.from_map(m.get('Question'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

