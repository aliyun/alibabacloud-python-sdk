# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSessionsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        session_id: str = None,
        session_status: str = None,
    ):
        # The number of sessions to be returned. If this parameter is not specified, 20 sessions are returned by default.
        self.limit = limit
        # The token for the next page.
        self.next_token = next_token
        # The function alias or version.
        self.qualifier = qualifier
        # The SessionId value to filter. If specified, all session information associated with this session ID in Active or Expired states is returned.
        self.session_id = session_id
        # The session status to filter. By default, information for all sessions in the Active and Expired states is returned. You can specify Active to retrieve only active sessions, or Expired to retrieve only expired sessions.
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        return self

