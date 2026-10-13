# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        max_results: int = None,
        next_token: str = None,
        session_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. If you do not specify this parameter, all agents are matched. The value must be 1 to 128 bytes in length and encoded in UTF-8. The value cannot contain a forward slash (/) or an asterisk (*).
        self.agent_id = agent_id
        # The maximum number of records per page. Default value: 50. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The session ID. If you do not specify this parameter, all sessions are matched. The value must be 1 to 128 bytes in length and encoded in UTF-8. The value cannot contain a forward slash (/) or an asterisk (*).
        self.session_id = session_id
        # The user ID. If you do not specify this parameter, all users are matched. The value must be 1 to 128 bytes in length and encoded in UTF-8. The value cannot contain a forward slash (/) or an asterisk (*).
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

