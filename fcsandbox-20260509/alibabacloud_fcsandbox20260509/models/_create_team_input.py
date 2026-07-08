# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTeamInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        resource_group_id: str = None,
        team_name: str = None,
    ):
        self.description = description
        self.resource_group_id = resource_group_id
        self.team_name = team_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        return self

