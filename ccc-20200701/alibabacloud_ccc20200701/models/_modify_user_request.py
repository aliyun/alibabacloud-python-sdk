# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserRequest(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        display_id: str = None,
        display_name: str = None,
        force: bool = None,
        instance_id: str = None,
        mobile: str = None,
        nickname: str = None,
        role_id: str = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        self.avatar_url = avatar_url
        self.display_id = display_id
        self.display_name = display_name
        self.force = force
        # This parameter is required.
        self.instance_id = instance_id
        self.mobile = mobile
        self.nickname = nickname
        self.role_id = role_id
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.display_id is not None:
            result['DisplayId'] = self.display_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('DisplayId') is not None:
            self.display_id = m.get('DisplayId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

