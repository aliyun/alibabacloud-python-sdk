# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUserSessionTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_session_token: str = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Token.
        self.user_session_token = user_session_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_session_token is not None:
            result['UserSessionToken'] = self.user_session_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserSessionToken') is not None:
            self.user_session_token = m.get('UserSessionToken')

        return self

