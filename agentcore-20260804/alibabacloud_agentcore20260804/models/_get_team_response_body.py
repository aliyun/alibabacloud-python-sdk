# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetTeamResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTeamResponseBodyData = None,
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
            temp_model = main_models.GetTeamResponseBodyData()
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

class GetTeamResponseBodyData(DaraModel):
    def __init__(
        self,
        agents: List[main_models.GetTeamResponseBodyDataAgents] = None,
        created_at: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        team_id: str = None,
        updated_at: str = None,
        users: List[main_models.GetTeamResponseBodyDataUsers] = None,
        workspace_id: str = None,
    ):
        self.agents = agents
        self.created_at = created_at
        self.description = description
        self.name = name
        self.region_id = region_id
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

        if self.region_id is not None:
            result['regionId'] = self.region_id

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
                temp_model = main_models.GetTeamResponseBodyDataAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.GetTeamResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetTeamResponseBodyDataUsers(DaraModel):
    def __init__(
        self,
        auth_method: str = None,
        created_at: str = None,
        display_name: str = None,
        email: str = None,
        initial_password: str = None,
        name: str = None,
        note: str = None,
        status: str = None,
        team_role: str = None,
        updated_at: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.auth_method = auth_method
        self.created_at = created_at
        self.display_name = display_name
        self.email = email
        self.initial_password = initial_password
        self.name = name
        self.note = note
        self.status = status
        self.team_role = team_role
        self.updated_at = updated_at
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_method is not None:
            result['authMethod'] = self.auth_method

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.email is not None:
            result['email'] = self.email

        if self.initial_password is not None:
            result['initialPassword'] = self.initial_password

        if self.name is not None:
            result['name'] = self.name

        if self.note is not None:
            result['note'] = self.note

        if self.status is not None:
            result['status'] = self.status

        if self.team_role is not None:
            result['teamRole'] = self.team_role

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMethod') is not None:
            self.auth_method = m.get('authMethod')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('initialPassword') is not None:
            self.initial_password = m.get('initialPassword')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamRole') is not None:
            self.team_role = m.get('teamRole')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetTeamResponseBodyDataAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        effective_spec_version: int = None,
        latest_spec_version: int = None,
        name: str = None,
        runtime: str = None,
        status: str = None,
        team_role: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        self.agent_id = agent_id
        self.create_mode = create_mode
        self.created_at = created_at
        self.deploy_type = deploy_type
        self.description = description
        self.effective_spec_version = effective_spec_version
        self.latest_spec_version = latest_spec_version
        self.name = name
        self.runtime = runtime
        self.status = status
        self.team_role = team_role
        self.updated_at = updated_at
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.effective_spec_version is not None:
            result['effectiveSpecVersion'] = self.effective_spec_version

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.name is not None:
            result['name'] = self.name

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.status is not None:
            result['status'] = self.status

        if self.team_role is not None:
            result['teamRole'] = self.team_role

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectiveSpecVersion') is not None:
            self.effective_spec_version = m.get('effectiveSpecVersion')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('teamRole') is not None:
            self.team_role = m.get('teamRole')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

