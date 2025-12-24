# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveMessageGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        administrators_shrink: str = None,
        app_id: str = None,
        creator_id: str = None,
        data_center: str = None,
        group_id: str = None,
        group_info: str = None,
        group_name: str = None,
    ):
        # The list of administrators.
        self.administrators_shrink = administrators_shrink
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the group creator. The ID can be up to 64 bytes in length and can contain letters and digits.
        self.creator_id = creator_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2593195.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The ID of the group that you want to create. The group ID must be unique within your business. The ID can be up to 64 bytes in length and can contain letters and digits.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The additional information about the group. The value can be up to 32 KB in length.
        self.group_info = group_info
        # The name of the group. The name can be up to 128 bytes in length.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrators_shrink is not None:
            result['Administrators'] = self.administrators_shrink

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Administrators') is not None:
            self.administrators_shrink = m.get('Administrators')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

