# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateApiKeyInput(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        expire_time: str = None,
        ip_blacklist: List[main_models.IPConfig] = None,
        ip_whitelist: List[main_models.IPConfig] = None,
        team_id: str = None,
        vpc_bindings: List[str] = None,
    ):
        # The name of the API key. The name can be up to 128 characters in length and can contain only letters, digits, spaces, hyphens (-), underscores (_), and half-width periods (.).
        self.api_key_name = api_key_name
        # The expiration time of the API key in UTC. The time must be in RFC 3339 format. If this parameter is left empty, the API key never expires.
        self.expire_time = expire_time
        # The IP address blacklist. After you configure this parameter, the IP addresses in the list cannot use the API key. This parameter is mutually exclusive with ipWhitelist.
        self.ip_blacklist = ip_blacklist
        # The IP address whitelist. After you configure this parameter, only the IP addresses in the list can use the API key. This parameter is mutually exclusive with ipBlacklist.
        self.ip_whitelist = ip_whitelist
        # The ID of the team to which the API key belongs. The ID must be in UUID format. If this parameter is not specified, the default team of the current account is used.
        self.team_id = team_id
        # The list of source VPC IDs that are allowed to use this API key to initiate management requests. The list is matched as a set. If this parameter is omitted, set to null, or set to an empty array, no restrictions are applied to source VPCs. If this parameter is not empty, only requests from trusted source VPCs that match the list are allowed. Requests from the Internet or from unverified source VPCs are rejected. You can configure this parameter together with an IP address whitelist or blacklist. Requests must meet both restrictions. This field does not create VPC bindings for underlying functions.
        self.vpc_bindings = vpc_bindings

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
        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.ip_blacklist is not None:
            result['ipBlacklist'] = []
            for k1 in self.ip_blacklist:
                result['ipBlacklist'].append(k1.to_map() if k1 else None)

        if self.ip_whitelist is not None:
            result['ipWhitelist'] = []
            for k1 in self.ip_whitelist:
                result['ipWhitelist'].append(k1.to_map() if k1 else None)

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.vpc_bindings is not None:
            result['vpcBindings'] = self.vpc_bindings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('ipBlacklist') is not None:
            self.ip_blacklist = []
            for k1 in m.get('ipBlacklist'):
                temp_model = main_models.IPConfig()
                self.ip_blacklist.append(temp_model.from_map(k1))

        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = []
            for k1 in m.get('ipWhitelist'):
                temp_model = main_models.IPConfig()
                self.ip_whitelist.append(temp_model.from_map(k1))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('vpcBindings') is not None:
            self.vpc_bindings = m.get('vpcBindings')

        return self

