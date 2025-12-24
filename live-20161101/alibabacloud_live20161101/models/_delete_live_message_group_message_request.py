# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveMessageGroupMessageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_center: str = None,
        deleter_id: str = None,
        deleter_info: str = None,
        group_id: str = None,
        message_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The ID of the user who deletes the message. The ID must be up to 64 bytes in length and can contain letters and digits.
        self.deleter_id = deleter_id
        # The additional information about the user who performs the deletion operation. The value can be up to 512 bytes in length.
        self.deleter_info = deleter_info
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the message that you want to delete. Set this parameter to the value of MsgTid that you specified when you called the SendLiveMessageGroup operation. The ID must be up to 64 bytes in length and can contain letters and digits.
        # 
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.deleter_id is not None:
            result['DeleterId'] = self.deleter_id

        if self.deleter_info is not None:
            result['DeleterInfo'] = self.deleter_info

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DeleterId') is not None:
            self.deleter_id = m.get('DeleterId')

        if m.get('DeleterInfo') is not None:
            self.deleter_info = m.get('DeleterInfo')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

