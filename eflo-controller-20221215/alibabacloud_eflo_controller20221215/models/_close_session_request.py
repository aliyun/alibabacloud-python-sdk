# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloseSessionRequest(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        session_token: str = None,
    ):
        # The session ID.
        self.session_id = session_id
        # Session token.
        self.session_token = session_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_token is not None:
            result['SessionToken'] = self.session_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')

        return self

