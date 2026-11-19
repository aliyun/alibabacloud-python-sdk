# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        max_results: int = None,
        next_token: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The exact filter for the business agent.
        self.agent_id = agent_id
        # The maximum number of entries per page. Default value: 200. Valid values: 1 to 500.
        self.max_results = max_results
        # The pagination token used to continue reading the same query.
        self.next_token = next_token
        # The ID of the session.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The exact filter for the business team.
        self.team_id = team_id
        # The exact filter for the business user. This is not the platform tenant identity.
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

        if self.team_id is not None:
            result['teamId'] = self.team_id

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

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

