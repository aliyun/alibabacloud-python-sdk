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
        resource_group_id: str = None,
        status: str = None,
        team_id: str = None,
        team_name: str = None,
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
        self.resource_group_id = resource_group_id
        self.status = status
        self.team_id = team_id
        self.team_name = team_name
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

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

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

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

