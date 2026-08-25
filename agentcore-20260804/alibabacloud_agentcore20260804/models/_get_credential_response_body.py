# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCredentialResponseBodyData = None,
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
            temp_model = main_models.GetCredentialResponseBodyData()
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

class GetCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        bound_agents: List[main_models.GetCredentialResponseBodyDataBoundAgents] = None,
        created_at: str = None,
        credential_id: str = None,
        credential_metadata: str = None,
        credential_type: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        self.bound_agents = bound_agents
        self.created_at = created_at
        self.credential_id = credential_id
        self.credential_metadata = credential_metadata
        self.credential_type = credential_type
        self.description = description
        self.name = name
        self.region_id = region_id
        self.updated_at = updated_at
        self.workspace_id = workspace_id

    def validate(self):
        if self.bound_agents:
            for v1 in self.bound_agents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['boundAgents'] = []
        if self.bound_agents is not None:
            for k1 in self.bound_agents:
                result['boundAgents'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.credential_metadata is not None:
            result['credentialMetadata'] = self.credential_metadata

        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bound_agents = []
        if m.get('boundAgents') is not None:
            for k1 in m.get('boundAgents'):
                temp_model = main_models.GetCredentialResponseBodyDataBoundAgents()
                self.bound_agents.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('credentialMetadata') is not None:
            self.credential_metadata = m.get('credentialMetadata')

        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetCredentialResponseBodyDataBoundAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        return self

