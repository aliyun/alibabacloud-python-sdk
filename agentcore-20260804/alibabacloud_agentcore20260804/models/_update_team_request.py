# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateTeamRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateTeamRequestBody = None,
        client_token: str = None,
    ):
        self.body = body
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
            temp_model = main_models.UpdateTeamRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateTeamRequestBody(DaraModel):
    def __init__(
        self,
        agents: List[main_models.UpdateTeamRequestBodyAgents] = None,
        description: str = None,
        users: List[main_models.UpdateTeamRequestBodyUsers] = None,
    ):
        self.agents = agents
        self.description = description
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
                temp_model = main_models.UpdateTeamRequestBodyAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.UpdateTeamRequestBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class UpdateTeamRequestBodyUsers(DaraModel):
    def __init__(
        self,
        team_role: str = None,
        user_id: str = None,
    ):
        self.team_role = team_role
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

class UpdateTeamRequestBodyAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        team_role: str = None,
    ):
        self.agent_id = agent_id
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

