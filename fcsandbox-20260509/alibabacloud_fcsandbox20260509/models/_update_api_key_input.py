# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class UpdateApiKeyInput(DaraModel):
    def __init__(
        self,
        api_key_name: str = None,
        expire_time: str = None,
        ip_blacklist: List[main_models.IPConfig] = None,
        ip_whitelist: List[main_models.IPConfig] = None,
        status: str = None,
    ):
        # The API key name.
        self.api_key_name = api_key_name
        # The expiration time.
        self.expire_time = expire_time
        self.ip_blacklist = ip_blacklist
        self.ip_whitelist = ip_whitelist
        # The status. Valid values:
        # - active
        # - inactive
        self.status = status

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

        result['ipBlacklist'] = []
        if self.ip_blacklist is not None:
            for k1 in self.ip_blacklist:
                result['ipBlacklist'].append(k1.to_map() if k1 else None)

        result['ipWhitelist'] = []
        if self.ip_whitelist is not None:
            for k1 in self.ip_whitelist:
                result['ipWhitelist'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

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

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

