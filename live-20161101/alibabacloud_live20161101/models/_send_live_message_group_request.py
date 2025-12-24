# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendLiveMessageGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        data_center: str = None,
        group_id: str = None,
        msg_tid: str = None,
        msg_type: int = None,
        no_cache: bool = None,
        no_storage: bool = None,
        sender_id: str = None,
        sender_meta_info: str = None,
        statics_increase: int = None,
        weight: int = None,
    ):
        # The ID of the interactive messaging application in which the message is received.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The message body. The body can be up to 15 KB in length.
        self.body = body
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The ID of the group that receives the message.
        # 
        # >  Make sure that the specified group ID exists. Otherwise, a ResourceNotExist error is returned.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the message, which is a unique identifier that can be used to delete the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        self.msg_tid = msg_tid
        # The message type.
        self.msg_type = msg_type
        # Specifies whether to disable message caching. Valid values: true and false. Default value: false, which specifies that the message is cached to the recent message list of the group.
        self.no_cache = no_cache
        # Specifies whether to disable message storage. Valid values: true and false. Default value: false, which specifies that the message is stored for a validity period of 30 days. You can find the message in the response of the ListLiveMessageGroupMessages operation. If you do not want to store the message, set this parameter to true.
        self.no_storage = no_storage
        # The ID of the user who sends the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        # 
        # This parameter is required.
        self.sender_id = sender_id
        # The additional information about the user who sends the message. The value can be up to 512 bytes in length.
        self.sender_meta_info = sender_meta_info
        # The contribution of the message to the increase in the number of messages of this type. Default value: 1.
        self.statics_increase = statics_increase
        # The weight of the message. Default value: 1. A greater value indicates a higher priority. For a message of the highest priority, you can set the weight to 1000000.
        self.weight = weight

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.msg_tid is not None:
            result['MsgTid'] = self.msg_tid

        if self.msg_type is not None:
            result['MsgType'] = self.msg_type

        if self.no_cache is not None:
            result['NoCache'] = self.no_cache

        if self.no_storage is not None:
            result['NoStorage'] = self.no_storage

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_meta_info is not None:
            result['SenderMetaInfo'] = self.sender_meta_info

        if self.statics_increase is not None:
            result['StaticsIncrease'] = self.statics_increase

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MsgTid') is not None:
            self.msg_tid = m.get('MsgTid')

        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')

        if m.get('NoCache') is not None:
            self.no_cache = m.get('NoCache')

        if m.get('NoStorage') is not None:
            self.no_storage = m.get('NoStorage')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderMetaInfo') is not None:
            self.sender_meta_info = m.get('SenderMetaInfo')

        if m.get('StaticsIncrease') is not None:
            self.statics_increase = m.get('StaticsIncrease')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

