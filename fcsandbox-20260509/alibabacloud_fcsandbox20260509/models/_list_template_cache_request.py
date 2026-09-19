# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplateCacheRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        team_id: str = None,
        template_id: str = None,
    ):
        # The maximum number of entries per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token returned from the previous response.
        self.next_token = next_token
        # Filters by cache status. Valid values:
        # 
        # - InProgress
        # - Success
        # - Failed
        # - Deleting
        # - Evicted
        self.status = status
        # The team ID.
        self.team_id = team_id
        # The unique identifier of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

