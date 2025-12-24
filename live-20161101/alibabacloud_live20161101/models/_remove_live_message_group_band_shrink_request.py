# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveLiveMessageGroupBandShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_center: str = None,
        group_id: str = None,
        unbanned_users_shrink: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data center. It must be the same as the data center that was specified when you called the [CreateLiveMessageApp](https://help.aliyun.com/document_detail/2848162.html) operation to create the interactive messaging application.
        # 
        # >  Valid values: cn-shanghai and ap-southeast-1 (Singapore).
        self.data_center = data_center
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The users whom you want to unmute.
        # 
        # This parameter is required.
        self.unbanned_users_shrink = unbanned_users_shrink

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.unbanned_users_shrink is not None:
            result['UnbannedUsers'] = self.unbanned_users_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('UnbannedUsers') is not None:
            self.unbanned_users_shrink = m.get('UnbannedUsers')

        return self

