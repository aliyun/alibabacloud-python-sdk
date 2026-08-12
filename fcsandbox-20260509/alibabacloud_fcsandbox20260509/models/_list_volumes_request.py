# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVolumesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        status: str = None,
        team_id: str = None,
        user_id: str = None,
        volume_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id
        self.status = status
        self.team_id = team_id
        self.user_id = user_id
        self.volume_name = volume_name

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

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.user_id is not None:
            result['userID'] = self.user_id

        if self.volume_name is not None:
            result['volumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')

        return self

