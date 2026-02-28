# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListVisitorChatMessagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVisitorChatMessagesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListVisitorChatMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVisitorChatMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        messages: List[main_models.ListVisitorChatMessagesResponseBodyDataMessages] = None,
        next_page_token: str = None,
    ):
        self.messages = messages
        self.next_page_token = next_page_token

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
        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ListVisitorChatMessagesResponseBodyDataMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        return self

class ListVisitorChatMessagesResponseBodyDataMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        job_id: str = None,
        sender_avatar_url: str = None,
        sender_id: str = None,
        sender_name: str = None,
        sender_type: str = None,
        timestamp: int = None,
    ):
        self.content = content
        self.job_id = job_id
        self.sender_avatar_url = sender_avatar_url
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.sender_type = sender_type
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.sender_avatar_url is not None:
            result['SenderAvatarUrl'] = self.sender_avatar_url

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_name is not None:
            result['SenderName'] = self.sender_name

        if self.sender_type is not None:
            result['SenderType'] = self.sender_type

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SenderAvatarUrl') is not None:
            self.sender_avatar_url = m.get('SenderAvatarUrl')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')

        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

