# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        display_id: str = None,
        display_name: str = None,
        email: str = None,
        instance_id: str = None,
        login_name: str = None,
        mobile: str = None,
        need_email_notification: str = None,
        nickname: str = None,
        reset_password: bool = None,
        role_id: str = None,
        skill_level_list: str = None,
        work_mode: str = None,
    ):
        self.avatar_url = avatar_url
        self.display_id = display_id
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.email = email
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.login_name = login_name
        self.mobile = mobile
        self.need_email_notification = need_email_notification
        self.nickname = nickname
        self.reset_password = reset_password
        # This parameter is required.
        self.role_id = role_id
        self.skill_level_list = skill_level_list
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

        if self.email is not None:
            result['Email'] = self.email

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.need_email_notification is not None:
            result['NeedEmailNotification'] = self.need_email_notification

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.reset_password is not None:
            result['ResetPassword'] = self.reset_password

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.skill_level_list is not None:
            result['SkillLevelList'] = self.skill_level_list

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

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('NeedEmailNotification') is not None:
            self.need_email_notification = m.get('NeedEmailNotification')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('ResetPassword') is not None:
            self.reset_password = m.get('ResetPassword')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('SkillLevelList') is not None:
            self.skill_level_list = m.get('SkillLevelList')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

