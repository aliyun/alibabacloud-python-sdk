# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_tags_shrink: str = None,
        team_id: str = None,
    ):
        # The maximum number of entries to return per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token. Use the nextToken value returned in the previous response.
        self.next_token = next_token
        # The resource tags.
        self.resource_tags_shrink = resource_tags_shrink
        # The team ID.
        self.team_id = team_id

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

        if self.resource_tags_shrink is not None:
            result['resourceTags'] = self.resource_tags_shrink

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceTags') is not None:
            self.resource_tags_shrink = m.get('resourceTags')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

