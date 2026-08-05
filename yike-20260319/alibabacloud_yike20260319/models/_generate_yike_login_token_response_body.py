# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateYikeLoginTokenResponseBody(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        request_id: str = None,
        token: str = None,
        user_id: str = None,
    ):
        self.expires_at = expires_at
        self.request_id = request_id
        self.token = token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

