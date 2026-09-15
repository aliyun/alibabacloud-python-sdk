# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateTeamRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateTeamRequestBody = None,
        client_token: str = None,
    ):
        # The request body for creating a team.
        self.body = body
        # Not supported.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateTeamRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateTeamRequestBody(DaraModel):
    def __init__(
        self,
        agents: List[main_models.CreateTeamRequestBodyAgents] = None,
        description: str = None,
        name: str = None,
        users: List[main_models.CreateTeamRequestBodyUsers] = None,
    ):
        # The list of agent members in the team.
        self.agents = agents
        # The team description.
        self.description = description
        # The team name. The name can contain only lowercase letters, digits, and hyphens (-). It must start and end with a lowercase letter or digit. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The list of user members in the team. The list must include exactly one member with the ADMIN role.
        self.users = users

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['agents'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('agents') is not None:
            for k1 in m.get('agents'):
                temp_model = main_models.CreateTeamRequestBodyAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.CreateTeamRequestBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class CreateTeamRequestBodyUsers(DaraModel):
    def __init__(
        self,
        team_role: str = None,
        user_id: str = None,
    ):
        # The role of the user in the team. Valid values: ADMIN, MEMBER. Each team must include exactly one ADMIN.
        self.team_role = team_role
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.team_role is not None:
            result['teamRole'] = self.team_role

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('teamRole') is not None:
            self.team_role = m.get('teamRole')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class CreateTeamRequestBodyAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        team_role: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The role of the agent in the team. Valid values: LEADER, WORKER.
        self.team_role = team_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.team_role is not None:
            result['teamRole'] = self.team_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('teamRole') is not None:
            self.team_role = m.get('teamRole')

        return self

