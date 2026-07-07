# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class RefreshAuthTokensResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.RefreshAuthTokensResponseBodyData = None,
        request_id: str = None,
    ):
        # The token data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.RefreshAuthTokensResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RefreshAuthTokensResponseBodyData(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        tokens: List[main_models.RefreshAuthTokensResponseBodyDataTokens] = None,
    ):
        # The model gateway access URL.
        self.base_url = base_url
        # The list of tokens.
        self.tokens = tokens

    def validate(self):
        if self.tokens:
            for v1 in self.tokens:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        result['Tokens'] = []
        if self.tokens is not None:
            for k1 in self.tokens:
                result['Tokens'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        self.tokens = []
        if m.get('Tokens') is not None:
            for k1 in m.get('Tokens'):
                temp_model = main_models.RefreshAuthTokensResponseBodyDataTokens()
                self.tokens.append(temp_model.from_map(k1))

        return self

class RefreshAuthTokensResponseBodyDataTokens(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        expire_at: int = None,
        expire_seconds: int = None,
        instance_id: str = None,
        issued_at: int = None,
        license_key: str = None,
    ):
        # The authorization token value.
        self.auth_token = auth_token
        # The expiration timestamp.
        self.expire_at = expire_at
        # The validity period in seconds.
        self.expire_seconds = expire_seconds
        # The instance ID.
        self.instance_id = instance_id
        # The issuance timestamp.
        self.issued_at = issued_at
        # The license key.
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issued_at is not None:
            result['IssuedAt'] = self.issued_at

        if self.license_key is not None:
            result['LicenseKey'] = self.license_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IssuedAt') is not None:
            self.issued_at = m.get('IssuedAt')

        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')

        return self

