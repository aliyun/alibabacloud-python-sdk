# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateTeamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateTeamResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateTeamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateTeamResponseBodyData(DaraModel):
    def __init__(
        self,
        agents: List[main_models.CreateTeamResponseBodyDataAgents] = None,
        created_at: str = None,
        description: str = None,
        name: str = None,
        status: str = None,
        team_id: str = None,
        updated_at: str = None,
        users: List[main_models.CreateTeamResponseBodyDataUsers] = None,
        workspace_id: str = None,
    ):
        self.agents = agents
        self.created_at = created_at
        self.description = description
        self.name = name
        self.status = status
        self.team_id = team_id
        self.updated_at = updated_at
        self.users = users
        self.workspace_id = workspace_id

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

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        result['users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['users'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('agents') is not None:
            for k1 in m.get('agents'):
                temp_model = main_models.CreateTeamResponseBodyDataAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.CreateTeamResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateTeamResponseBodyDataUsers(DaraModel):
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

class CreateTeamResponseBodyDataAgents(DaraModel):
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

