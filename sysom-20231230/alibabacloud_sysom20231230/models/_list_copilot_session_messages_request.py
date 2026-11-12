# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCopilotSessionMessagesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        limit: int = None,
        max_results: int = None,
        next_token: str = None,
        offset: int = None,
        session_id: str = None,
    ):
        # The agent ID retained for compatibility with historical calls. This parameter can be omitted. Currently, the entire session is queried by sessionId, and this parameter does not change the query scope of historical events.
        self.agent_id = agent_id
        # The page size retained for compatibility with historical calls. Default value: 50. Valid values: 1 to 200. For new integrations, we recommend using maxResults. If both parameters are specified, maxResults takes precedence.
        self.limit = limit
        # The page size. Default value: 50. Valid values: 1 to 1000.
        self.max_results = max_results
        # The token for the next page. Do not specify this parameter for the first request. For subsequent requests, use the nextToken value from the previous response. Clear this value when you change the filter conditions.
        self.next_token = next_token
        # The pagination offset retained for compatibility with historical calls. Default value: 0. For new integrations, we recommend using nextToken. Do not specify this parameter and nextToken at the same time.
        self.offset = offset
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.offset is not None:
            result['offset'] = self.offset

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

