# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class ResetApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: main_models.ApiKey = None,
        code: str = None,
        ip_blacklist: List[main_models.IPConfig] = None,
        ip_whitelist: List[main_models.IPConfig] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The API key information.
        self.api_key = api_key
        # The error code.
        self.code = code
        self.ip_blacklist = ip_blacklist
        self.ip_whitelist = ip_whitelist
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.api_key:
            self.api_key.validate()
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
        if self.api_key is not None:
            result['apiKey'] = self.api_key.to_map()

        if self.code is not None:
            result['code'] = self.code

        result['ipBlacklist'] = []
        if self.ip_blacklist is not None:
            for k1 in self.ip_blacklist:
                result['ipBlacklist'].append(k1.to_map() if k1 else None)

        result['ipWhitelist'] = []
        if self.ip_whitelist is not None:
            for k1 in self.ip_whitelist:
                result['ipWhitelist'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            temp_model = main_models.ApiKey()
            self.api_key = temp_model.from_map(m.get('apiKey'))

        if m.get('code') is not None:
            self.code = m.get('code')

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

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

