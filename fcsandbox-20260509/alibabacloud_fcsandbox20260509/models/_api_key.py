# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
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
        ip_blacklist: List[main_models.IPConfig] = None,
        ip_whitelist: List[main_models.IPConfig] = None,
        last_used_time: str = None,
        resource_group_id: str = None,
        source: str = None,
        status: str = None,
        team_id: str = None,
        team_name: str = None,
        team_plan: str = None,
        user_id: str = None,
        username: str = None,
    ):
        # The unique identifier of the API key.
        self.api_key_id = api_key_id
        # The masked display value of the API key.
        self.api_key_mask = api_key_mask
        # The name of the API key.
        self.api_key_name = api_key_name
        # The value of the API key.
        self.api_key_value = api_key_value
        # The time when the API key was created.
        self.created_time = created_time
        # The expiration time.
        self.expire_time = expire_time
        self.ip_blacklist = ip_blacklist
        self.ip_whitelist = ip_whitelist
        # The time when the API key was last used.
        self.last_used_time = last_used_time
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.source = source
        # The status. Valid values:
        # - active
        # - inactive
        self.status = status
        # The unique identifier of the team.
        self.team_id = team_id
        # The name of the team.
        self.team_name = team_name
        self.team_plan = team_plan
        # The UID of the creator.
        self.user_id = user_id
        # The creator.
        self.username = username

    def validate(self):
        if self.ip_blacklist:
            for v1 in self.ip_blacklist:
                 if v1:
                    v1.validate()
        if self.ip_whitelist:
            for v1 in self.ip_whitelist:
                 if v1:
                    v1.validate()

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

        result['ipBlacklist'] = []
        if self.ip_blacklist is not None:
            for k1 in self.ip_blacklist:
                result['ipBlacklist'].append(k1.to_map() if k1 else None)

        result['ipWhitelist'] = []
        if self.ip_whitelist is not None:
            for k1 in self.ip_whitelist:
                result['ipWhitelist'].append(k1.to_map() if k1 else None)

        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.team_plan is not None:
            result['teamPlan'] = self.team_plan

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

        self.ip_blacklist = []
        if m.get('ipBlacklist') is not None:
            for k1 in m.get('ipBlacklist'):
                temp_model = main_models.IPConfig()
                self.ip_blacklist.append(temp_model.from_map(k1))

        self.ip_whitelist = []
        if m.get('ipWhitelist') is not None:
            for k1 in m.get('ipWhitelist'):
                temp_model = main_models.IPConfig()
                self.ip_whitelist.append(temp_model.from_map(k1))

        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('teamPlan') is not None:
            self.team_plan = m.get('teamPlan')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

