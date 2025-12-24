# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListMessageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListMessageResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListMessageResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListMessageResponseBodyResult(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        message_list: List[main_models.ListMessageResponseBodyResultMessageList] = None,
    ):
        # Indicates whether the current page is followed by another page. Valid values:
        # 
        # *   true: The current page is followed by another page.
        # *   false: The current page is not followed by another page.
        self.has_more = has_more
        # Details about the messages.
        self.message_list = message_list

    def validate(self):
        if self.message_list:
            for v1 in self.message_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['MessageList'] = []
        if self.message_list is not None:
            for k1 in self.message_list:
                result['MessageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.message_list = []
        if m.get('MessageList') is not None:
            for k1 in m.get('MessageList'):
                temp_model = main_models.ListMessageResponseBodyResultMessageList()
                self.message_list.append(temp_model.from_map(k1))

        return self

class ListMessageResponseBodyResultMessageList(DaraModel):
    def __init__(
        self,
        data: str = None,
        group_id: str = None,
        message_id: str = None,
        sender_id: str = None,
        type: int = None,
    ):
        # The message body. The value is a JSON string.
        self.data = data
        # The ID of the message group.
        self.group_id = group_id
        # The ID of the message.
        self.message_id = message_id
        # The ID of the user who sent the message.
        self.sender_id = sender_id
        # The type of the message.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

