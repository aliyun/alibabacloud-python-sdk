# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseUserResponse(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        created_at: str = None,
        creator: str = None,
        default_drive_id: str = None,
        default_location: str = None,
        deny_change_password_by_self: bool = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        expired_at: int = None,
        is_sync: bool = None,
        last_login_time: int = None,
        need_change_password_next_login: bool = None,
        nick_name: str = None,
        path_status: str = None,
        permission: Dict[str, main_models.IDPermission] = None,
        phone: str = None,
        phone_region: str = None,
        role: str = None,
        status: str = None,
        updated_at: str = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.avatar = avatar
        self.created_at = created_at
        self.creator = creator
        self.default_drive_id = default_drive_id
        self.default_location = default_location
        self.deny_change_password_by_self = deny_change_password_by_self
        self.description = description
        self.domain_id = domain_id
        self.email = email
        self.expired_at = expired_at
        self.is_sync = is_sync
        self.last_login_time = last_login_time
        self.need_change_password_next_login = need_change_password_next_login
        self.nick_name = nick_name
        self.path_status = path_status
        self.permission = permission
        self.phone = phone
        self.phone_region = phone_region
        self.role = role
        self.status = status
        self.updated_at = updated_at
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.permission:
            for v1 in self.permission.values():
                 if v1:
                    v1.validate()

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

        if self.default_location is not None:
            result['default_location'] = self.default_location

        if self.deny_change_password_by_self is not None:
            result['deny_change_password_by_self'] = self.deny_change_password_by_self

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.email is not None:
            result['email'] = self.email

        if self.expired_at is not None:
            result['expired_at'] = self.expired_at

        if self.is_sync is not None:
            result['is_sync'] = self.is_sync

        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time

        if self.need_change_password_next_login is not None:
            result['need_change_password_next_login'] = self.need_change_password_next_login

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.path_status is not None:
            result['path_status'] = self.path_status

        result['permission'] = {}
        if self.permission is not None:
            for k1, v1 in self.permission.items():
                result['permission'][k1] = v1.to_map() if v1 else None

        if self.phone is not None:
            result['phone'] = self.phone

        if self.phone_region is not None:
            result['phone_region'] = self.phone_region

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

        if m.get('default_location') is not None:
            self.default_location = m.get('default_location')

        if m.get('deny_change_password_by_self') is not None:
            self.deny_change_password_by_self = m.get('deny_change_password_by_self')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')

        if m.get('is_sync') is not None:
            self.is_sync = m.get('is_sync')

        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')

        if m.get('need_change_password_next_login') is not None:
            self.need_change_password_next_login = m.get('need_change_password_next_login')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')

        self.permission = {}
        if m.get('permission') is not None:
            for k1, v1 in m.get('permission').items():
                temp_model = main_models.IDPermission()
                self.permission[k1] = temp_model.from_map(v1)

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')

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

