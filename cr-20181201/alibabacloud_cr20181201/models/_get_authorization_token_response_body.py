# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuthorizationTokenResponseBody(DaraModel):
    def __init__(
        self,
        authorization_token: str = None,
        code: str = None,
        expire_time: int = None,
        is_success: bool = None,
        request_id: str = None,
        temp_username: str = None,
    ):
        # The password that you use to log on to the registry.
        self.authorization_token = authorization_token
        # The HTTP status code.
        self.code = code
        # The timestamp when the temporary token expired. Unit: milliseconds.
        self.expire_time = expire_time
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID
        self.request_id = request_id
        # The username that you use to log on to the registry.
        self.temp_username = temp_username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_token is not None:
            result['AuthorizationToken'] = self.authorization_token

        if self.code is not None:
            result['Code'] = self.code

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.temp_username is not None:
            result['TempUsername'] = self.temp_username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationToken') is not None:
            self.authorization_token = m.get('AuthorizationToken')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TempUsername') is not None:
            self.temp_username = m.get('TempUsername')

        return self

