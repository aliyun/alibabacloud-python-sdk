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
        # The URL of the agent\\"s profile picture.
        self.avatar_url = avatar_url
        # The agent\\"s ID number. Set this as needed.
        self.display_id = display_id
        # The display name of the agent. It must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address of the agent. After the agent is created, an email is sent to this address. The email contains the logon URL for Cloud Contact Center, and the username and password for the RAM account. Keep this information secure.
        # 
        # This parameter is required.
        self.email = email
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The logon name of the agent. It must be 4 to 64 characters in length and can contain uppercase letters, lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.login_name = login_name
        # The personal phone number of the agent. This number is used in OFF_SITE mode. The agent can use this number to answer calls in OFF_SITE mode.
        self.mobile = mobile
        # Specifies whether to send an email notification.
        # 
        # - true: Send
        # 
        # - false: Do not send
        self.need_email_notification = need_email_notification
        # The agent\\"s nickname.
        self.nickname = nickname
        # Specifies whether the agent must reset the password upon the first logon. If set to true, the agent is prompted to reset the password when they first log on to the RAM account. Otherwise, they are not prompted. The default value is false.
        self.reset_password = reset_password
        # The role ID. The format is Role\\@InstanceID. The following roles are supported: Admin (administrator), Manager (skill group leader), and Agent (agent).
        # 
        # This parameter is required.
        self.role_id = role_id
        # A list of skill levels for skill groups. This is a string in the format of a JSON array. The array can contain up to 100 elements. Each element is an object that contains two fields: skillGroupId and skillLevel. For skillGroupId, enter the ID of the skill group to add. For skillLevel, enter the skill level to add. The value can range from 1 to 10. A smaller value indicates a higher skill level, meaning the agent can handle more calls per unit of time.
        self.skill_level_list = skill_level_list
        # The work mode.
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

