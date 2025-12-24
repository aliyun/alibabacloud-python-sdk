# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        admin_list_shrink: str = None,
        app_id: str = None,
        data_center: str = None,
        group_id: str = None,
        group_info: str = None,
        modify_admin: bool = None,
        modify_info: bool = None,
    ):
        # The list of administrators after your change.
        self.admin_list_shrink = admin_list_shrink
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application. Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The additional information about the group after the modification. The value can be up to 32 KB in length.
        self.group_info = group_info
        # Specifies whether to change the group administrators.
        self.modify_admin = modify_admin
        # Specifies whether to modify the additional information about the group.
        self.modify_info = modify_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_list_shrink is not None:
            result['AdminList'] = self.admin_list_shrink

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.modify_admin is not None:
            result['ModifyAdmin'] = self.modify_admin

        if self.modify_info is not None:
            result['ModifyInfo'] = self.modify_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminList') is not None:
            self.admin_list_shrink = m.get('AdminList')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('ModifyAdmin') is not None:
            self.modify_admin = m.get('ModifyAdmin')

        if m.get('ModifyInfo') is not None:
            self.modify_info = m.get('ModifyInfo')

        return self

