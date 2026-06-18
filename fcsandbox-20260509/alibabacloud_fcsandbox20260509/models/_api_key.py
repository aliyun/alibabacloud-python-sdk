# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class ApiKey(DaraModel):
    def __init__(
        self,
        api_key_id: str = None,
        api_key_mask: str = None,
        api_key_name: str = None,
        api_key_value: str = None,
        created_time: str = None,
        expire_time: str = None,
        last_used_time: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.api_key_id = api_key_id
        self.api_key_mask = api_key_mask
        self.api_key_name = api_key_name
        self.api_key_value = api_key_value
        self.created_time = created_time
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyID'] = self.api_key_id

        if self.api_key_mask is not None:
            result['apiKeyMask'] = self.api_key_mask

        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.api_key_value is not None:
            result['apiKeyValue'] = self.api_key_value

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time

        if self.user_id is not None:
            result['userID'] = self.user_id

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyID') is not None:
            self.api_key_id = m.get('apiKeyID')

        if m.get('apiKeyMask') is not None:
            self.api_key_mask = m.get('apiKeyMask')

        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('apiKeyValue') is not None:
            self.api_key_value = m.get('apiKeyValue')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

