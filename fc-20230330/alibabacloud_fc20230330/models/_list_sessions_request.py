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
        # The maximum number of sessions to return. Default value: 20.
        self.limit = limit
        # The pagination token.
        self.next_token = next_token
        # The alias or version of the function.
        self.qualifier = qualifier
        # The ID of the session used for filtering. If you specify this parameter, all active or expired status information associated with the session is returned.
        self.session_id = session_id
        # The session status to filter. By default, all session information in the Active or Expired state is returned. You can specify Active to retrieve only active session information, or specify Expired to retrieve only expired session information.
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

