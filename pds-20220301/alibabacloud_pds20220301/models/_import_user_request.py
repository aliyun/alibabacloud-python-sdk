# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportUserRequest(DaraModel):
    def __init__(
        self,
        authentication_display_name: str = None,
        authentication_type: str = None,
        auto_create_drive: bool = None,
        drive_total_size: int = None,
        extra: str = None,
        identity: str = None,
        nick_name: str = None,
        parent_group_id: str = None,
    ):
        # The display name of the authentication type.
        self.authentication_display_name = authentication_display_name
        # The authentication type. Valid values:
        # 
        # *   mobile: mobile number.
        # *   email: email address.
        # *   ding: DingTalk account.
        # *   ram: Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: WeCom account.
        # *   ldap: Lightweight Directory Access Protocol (LDAP) account.
        # *   custom: custom account.
        # 
        # This parameter is required.
        self.authentication_type = authentication_type
        # Specifies whether to automatically create a drive.
        self.auto_create_drive = auto_create_drive
        # The size of the drive. The value cannot be smaller than -1. A value of -1 specifies that the size is unlimited.
        self.drive_total_size = drive_total_size
        # The additional information.
        # 
        # If authentication_type is set to mobile, set this parameter to a country code. If you do not specify this parameter, 86 is used by default.
        self.extra = extra
        # The unique identifier.
        # 
        # This parameter is required.
        self.identity = identity
        # The nickname of the user.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The ID of the group to which the user is added.
        self.parent_group_id = parent_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_display_name is not None:
            result['authentication_display_name'] = self.authentication_display_name

        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type

        if self.auto_create_drive is not None:
            result['auto_create_drive'] = self.auto_create_drive

        if self.drive_total_size is not None:
            result['drive_total_size'] = self.drive_total_size

        if self.extra is not None:
            result['extra'] = self.extra

        if self.identity is not None:
            result['identity'] = self.identity

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_display_name') is not None:
            self.authentication_display_name = m.get('authentication_display_name')

        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')

        if m.get('auto_create_drive') is not None:
            self.auto_create_drive = m.get('auto_create_drive')

        if m.get('drive_total_size') is not None:
            self.drive_total_size = m.get('drive_total_size')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('identity') is not None:
            self.identity = m.get('identity')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')

        return self

