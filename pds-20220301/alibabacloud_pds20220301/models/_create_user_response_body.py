# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateUserResponseBody(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        creator: str = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The URL of the profile picture.
        self.avatar = avatar
        # The time when the user was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The user who created the user.
        self.creator = creator
        # The ID of the default drive.
        self.default_drive_id = default_drive_id
        # The description of the user.
        self.description = description
        # The domain ID.
        self.domain_id = domain_id
        # The email address.
        self.email = email
        # The nickname of the user.
        self.nick_name = nick_name
        # The phone number.
        self.phone = phone
        # The role of the user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        self.role = role
        # The state of the user. Valid values:
        # 
        # *   disabled: The user is prohibited from logon.
        # *   enabled: The user is in a normal state.
        self.status = status
        # The time when the user was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_at = updated_at
        # The custom data.
        self.user_data = user_data
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.email is not None:
            result['email'] = self.email

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.role is not None:
            result['role'] = self.role

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.user_data is not None:
            result['user_data'] = self.user_data

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

