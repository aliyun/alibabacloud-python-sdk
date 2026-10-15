# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class E2BTeam(DaraModel):
    def __init__(
        self,
        allow_update_team_name: bool = None,
        created_time: str = None,
        description: str = None,
        plan: str = None,
        read_only: bool = None,
        resource_group_id: str = None,
        status: str = None,
        team_id: str = None,
        team_name: str = None,
        user_id: str = None,
    ):
        # Specifies whether the team name can be modified. The default team does not allow modification.
        self.allow_update_team_name = allow_update_team_name
        # The creation time of the team in UTC, in RFC 3339 format.
        self.created_time = created_time
        # The team description.
        self.description = description
        # The team plan specification. Valid values:
        # - eco: economy.
        # - std: standard.
        # - pro: professional.
        # - ent: enterprise.
        self.plan = plan
        # Indicates whether the current caller has read-only access to the team. If the value is true, the team configuration cannot be modified.
        self.read_only = read_only
        # The ID of the Alibaba Cloud resource group to which the team belongs.
        self.resource_group_id = resource_group_id
        # The team status. Valid values:
        # - active: Normal.
        # - deleting: Being deleted.
        # - delete_failed: Failed to delete.
        self.status = status
        # The ID of the team to which the resource belongs, in UUID format.
        self.team_id = team_id
        # The team name.
        self.team_name = team_name
        # The user ID of the team creator, in UUID format.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_update_team_name is not None:
            result['allowUpdateTeamName'] = self.allow_update_team_name

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.plan is not None:
            result['plan'] = self.plan

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowUpdateTeamName') is not None:
            self.allow_update_team_name = m.get('allowUpdateTeamName')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

