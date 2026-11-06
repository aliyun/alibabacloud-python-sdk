# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCopilotSessionsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        max_results: int = None,
        next_token: str = None,
        scheduled_task_id: int = None,
        session_type: str = None,
    ):
        # The agent ID. If this parameter is not specified, all agent sessions of the current user are queried.
        self.agent_id = agent_id
        # The maximum number of records per page. Default value: 50. Valid values: 1 to 1000.
        self.max_results = max_results
        # The pagination token for the next page. Do not specify this parameter for the first query.
        self.next_token = next_token
        # The scheduled task ID, which must be a positive integer. If this parameter is specified, sessionType must be omitted or set to cron.
        self.scheduled_task_id = scheduled_task_id
        # The session source. If this parameter is not specified, sessions are not filtered by source.
        self.session_type = session_type

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

        if self.scheduled_task_id is not None:
            result['scheduledTaskId'] = self.scheduled_task_id

        if self.session_type is not None:
            result['sessionType'] = self.session_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('scheduledTaskId') is not None:
            self.scheduled_task_id = m.get('scheduledTaskId')

        if m.get('sessionType') is not None:
            self.session_type = m.get('sessionType')

        return self

