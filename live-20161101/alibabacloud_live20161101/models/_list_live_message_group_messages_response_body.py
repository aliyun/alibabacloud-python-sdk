# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveMessageGroupMessagesResponseBody(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        hasmore: bool = None,
        message_list: List[main_models.ListLiveMessageGroupMessagesResponseBodyMessageList] = None,
        next_page_token: int = None,
        request_id: str = None,
    ):
        # The ID of the group queried.
        self.group_id = group_id
        # Indicates whether the current page is followed by another page.
        self.hasmore = hasmore
        # Details about the messages.
        self.message_list = message_list
        # The starting page number for the next query. A value of 0 indicates that no further pages can be queried.
        self.next_page_token = next_page_token
        # The request ID.
        self.request_id = request_id

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
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hasmore is not None:
            result['Hasmore'] = self.hasmore

        result['MessageList'] = []
        if self.message_list is not None:
            for k1 in self.message_list:
                result['MessageList'].append(k1.to_map() if k1 else None)

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Hasmore') is not None:
            self.hasmore = m.get('Hasmore')

        self.message_list = []
        if m.get('MessageList') is not None:
            for k1 in m.get('MessageList'):
                temp_model = main_models.ListLiveMessageGroupMessagesResponseBodyMessageList()
                self.message_list.append(temp_model.from_map(k1))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLiveMessageGroupMessagesResponseBodyMessageList(DaraModel):
    def __init__(
        self,
        body: str = None,
        msg_tid: str = None,
        msg_type: int = None,
        sender: main_models.ListLiveMessageGroupMessagesResponseBodyMessageListSender = None,
        seq_number: int = None,
        timestamp: int = None,
        total_messages: int = None,
    ):
        # The message body.
        self.body = body
        # The ID of the message.
        self.msg_tid = msg_tid
        # The type of the message.
        self.msg_type = msg_type
        # The details about the user who sent the message.
        self.sender = sender
        # The sequence number of the message.
        self.seq_number = seq_number
        # The time when the message was sent. The value is a UNIX timestamp. Unit: seconds.
        self.timestamp = timestamp
        # The total number of messages.
        self.total_messages = total_messages

    def validate(self):
        if self.sender:
            self.sender.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.msg_tid is not None:
            result['MsgTid'] = self.msg_tid

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.sender is not None:
            result['Sender'] = self.sender.to_map()

        if self.seq_number is not None:
            result['SeqNumber'] = self.seq_number

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_messages is not None:
            result['TotalMessages'] = self.total_messages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('MsgTid') is not None:
            self.msg_tid = m.get('MsgTid')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('Sender') is not None:
            temp_model = main_models.ListLiveMessageGroupMessagesResponseBodyMessageListSender()
            self.sender = temp_model.from_map(m.get('Sender'))

        if m.get('SeqNumber') is not None:
            self.seq_number = m.get('SeqNumber')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalMessages') is not None:
            self.total_messages = m.get('TotalMessages')

        return self

class ListLiveMessageGroupMessagesResponseBodyMessageListSender(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_info: str = None,
    ):
        # The ID of the user who sent the message.
        self.user_id = user_id
        # The additional information about the user who sent the message.
        self.user_info = user_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')

        return self

