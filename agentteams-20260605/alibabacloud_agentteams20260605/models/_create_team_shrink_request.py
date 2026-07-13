# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTeamShrinkRequest(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        team_members_shrink: str = None,
    ):
        self.admin_name = admin_name
        self.client_token = client_token
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.team_members_shrink = team_members_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_name is not None:
            result['AdminName'] = self.admin_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.team_members_shrink is not None:
            result['TeamMembers'] = self.team_members_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TeamMembers') is not None:
            self.team_members_shrink = m.get('TeamMembers')

        return self

