# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class AccountAccessTokenResponse(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        avatar: str = None,
        default_drive_id: str = None,
        default_sbox_drive_id: str = None,
        device_id: str = None,
        device_name: str = None,
        domain_id: str = None,
        exist_link: List[main_models.LinkInfo] = None,
        expire_time: str = None,
        expires_in: int = None,
        is_first_login: bool = None,
        need_link: bool = None,
        need_rp_verify: bool = None,
        nick_name: str = None,
        path_status: str = None,
        pin_setup: bool = None,
        refresh_token: str = None,
        role: str = None,
        state: str = None,
        status: str = None,
        token_type: str = None,
        user_data: Dict[str, str] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.access_token = access_token
        self.avatar = avatar
        self.default_drive_id = default_drive_id
        self.default_sbox_drive_id = default_sbox_drive_id
        self.device_id = device_id
        self.device_name = device_name
        self.domain_id = domain_id
        self.exist_link = exist_link
        self.expire_time = expire_time
        self.expires_in = expires_in
        self.is_first_login = is_first_login
        self.need_link = need_link
        self.need_rp_verify = need_rp_verify
        self.nick_name = nick_name
        self.path_status = path_status
        self.pin_setup = pin_setup
        self.refresh_token = refresh_token
        self.role = role
        self.state = state
        self.status = status
        self.token_type = token_type
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.exist_link:
            for v1 in self.exist_link:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['access_token'] = self.access_token

        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id

        if self.default_sbox_drive_id is not None:
            result['default_sbox_drive_id'] = self.default_sbox_drive_id

        if self.device_id is not None:
            result['device_id'] = self.device_id

        if self.device_name is not None:
            result['device_name'] = self.device_name

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        result['exist_link'] = []
        if self.exist_link is not None:
            for k1 in self.exist_link:
                result['exist_link'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.expires_in is not None:
            result['expires_in'] = self.expires_in

        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login

        if self.need_link is not None:
            result['need_link'] = self.need_link

        if self.need_rp_verify is not None:
            result['need_rp_verify'] = self.need_rp_verify

        if self.nick_name is not None:
            result['nick_name'] = self.nick_name

        if self.path_status is not None:
            result['path_status'] = self.path_status

        if self.pin_setup is not None:
            result['pin_setup'] = self.pin_setup

        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token

        if self.role is not None:
            result['role'] = self.role

        if self.state is not None:
            result['state'] = self.state

        if self.status is not None:
            result['status'] = self.status

        if self.token_type is not None:
            result['token_type'] = self.token_type

        if self.user_data is not None:
            result['user_data'] = self.user_data

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')

        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')

        if m.get('default_sbox_drive_id') is not None:
            self.default_sbox_drive_id = m.get('default_sbox_drive_id')

        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')

        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        self.exist_link = []
        if m.get('exist_link') is not None:
            for k1 in m.get('exist_link'):
                temp_model = main_models.LinkInfo()
                self.exist_link.append(temp_model.from_map(k1))

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')

        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')

        if m.get('need_link') is not None:
            self.need_link = m.get('need_link')

        if m.get('need_rp_verify') is not None:
            self.need_rp_verify = m.get('need_rp_verify')

        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')

        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')

        if m.get('pin_setup') is not None:
            self.pin_setup = m.get('pin_setup')

        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

