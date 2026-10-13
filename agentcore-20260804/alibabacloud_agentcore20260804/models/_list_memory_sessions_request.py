# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMemorySessionsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        max_results: int = None,
        next_token: str = None,
        user_id: str = None,
    ):
        # The agent ID. If this parameter is not specified, all agents are matched. The length is limited to 1 to 128 UTF-8 bytes, and the value cannot contain / or *.
        self.agent_id = agent_id
        # The maximum number of records per page. Default value: 100. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The user ID. If this parameter is not specified, all users are matched. The length is limited to 1 to 128 UTF-8 bytes, and the value cannot contain / or *.
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

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

