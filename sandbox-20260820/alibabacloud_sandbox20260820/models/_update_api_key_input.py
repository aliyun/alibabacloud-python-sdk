# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class UpdateApiKeyInput(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        expire_time: str = None,
        ip_blacklist: List[main_models.IPConfig] = None,
        ip_whitelist: List[main_models.IPConfig] = None,
        status: str = None,
        vpc_bindings: List[str] = None,
    ):
        # The new name of the API key. The name can be up to 128 characters in length and can contain only letters, digits, spaces, hyphens (-), underscores (_), and periods (.).
        self.api_key_name = api_key_name
        # The expiration time of the API key in UTC. The time must be in RFC 3339 format. An empty value indicates that the API key never expires.
        self.expire_time = expire_time
        # The IP address blacklist. If you specify this parameter, the existing blacklist is completely overwritten. This parameter is mutually exclusive with ipWhitelist.
        self.ip_blacklist = ip_blacklist
        # The IP address whitelist. If you specify this parameter, the existing whitelist is completely overwritten. This parameter is mutually exclusive with ipBlacklist.
        self.ip_whitelist = ip_whitelist
        # The new status of the API key. Valid values:
        # - active: Enabled.
        # - inactive: Disabled.
        self.status = status
        # The set of allowed source VPC IDs. This set is updated independently of the IP blacklists and whitelists. If you omit this parameter or set it to null, the original set is retained. A non-empty array completely replaces the original set. An explicit empty array [] purges the VPC restrictions. Updating only this parameter does not affect the IP address lists, and updating the IP address lists does not affect the VPC restrictions. An empty request body {} purges all IP address and VPC source restrictions. You can update this parameter along with other parameters such as the name.
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

        if self.status is not None:
            result['status'] = self.status

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

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('vpcBindings') is not None:
            self.vpc_bindings = m.get('vpcBindings')

        return self

