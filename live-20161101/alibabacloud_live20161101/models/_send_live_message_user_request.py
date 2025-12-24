# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendLiveMessageUserRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        data_center: str = None,
        high_reliability: bool = None,
        msg_tid: str = None,
        msg_type: int = None,
        receiver_id: str = None,
        sender_id: str = None,
        sender_info: str = None,
        storage: bool = None,
    ):
        # The ID of the interactive messaging application in which the message is sent.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The message body. It can be up to 15 KB in length.
        self.body = body
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # Specifies whether to set the message as a highly reliable message. A highly reliable message ensures that success is returned only after the receiver has received the message and responded. If the receiver does not respond within 3 seconds, failure is returned.
        # 
        # *   true: sets the message as a highly reliable message.
        # *   false (default): does not set the message as a highly reliable message.
        # 
        # >  This parameter is supported only by the client SDK V1.5.1 and later. When you send a message to a client with an earlier SDK version, the message can be successfully sent without waiting for an acknowledgement (ACK) response.
        self.high_reliability = high_reliability
        # The ID of the message, which is a unique identifier that can be used to delete the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        self.msg_tid = msg_tid
        # The message type.
        self.msg_type = msg_type
        # The ID of the user who receives the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        # 
        # >  Make sure that the user who receives the message is online. You can call the CheckLiveMessageUsersOnline operation to query whether the user is online.
        # 
        # This parameter is required.
        self.receiver_id = receiver_id
        # The ID of the user who sends the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        # 
        # This parameter is required.
        self.sender_id = sender_id
        # The additional information about the user who sends the message. It can be up to 512 bytes in length.
        self.sender_info = sender_info
        # Specifies whether to store the message.
        # 
        # *   true: stores the message.
        # *   false (default): does not store the message.
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.body is not None:
            result['Body'] = self.body

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.high_reliability is not None:
            result['HighReliability'] = self.high_reliability

        if self.msg_tid is not None:
            result['MsgTid'] = self.msg_tid

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_info is not None:
            result['SenderInfo'] = self.sender_info

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('HighReliability') is not None:
            self.high_reliability = m.get('HighReliability')

        if m.get('MsgTid') is not None:
            self.msg_tid = m.get('MsgTid')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderInfo') is not None:
            self.sender_info = m.get('SenderInfo')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

