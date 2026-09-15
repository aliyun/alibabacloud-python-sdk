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
        # The business status code.
        self.code = code
        # The credential details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message. An error description is returned if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        resource_refs: List[main_models.GetCredentialResponseBodyDataResourceRefs] = None,
        resource_scope: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The list of agents bound to the credential.
        self.bound_agents = bound_agents
        # The creation time in UTC, formatted according to RFC 3339.
        self.created_at = created_at
        # The credential ID.
        self.credential_id = credential_id
        # The masked content of the credential. When credentialType is apiKey, the value of apiKey is returned as asterisks (*) of equal length.
        self.credential_metadata = credential_metadata
        # The credential type. Currently, only apiKey is supported.
        self.credential_type = credential_type
        # The credential description, up to 256 characters in length.
        self.description = description
        # The credential name. The name must be unique within the workspace and can contain only letters, digits, periods (.), underscores (_), and hyphens (-). The name must be 3 to 128 characters in length and cannot use runtime reserved names.
        self.name = name
        # The region ID where the resource resides.
        self.region_id = region_id
        # Each item contains resourceType, resourceId, and resourceName. If the resource has been deleted, resourceName is empty.
        self.resource_refs = resource_refs
        # The scope of resources to which the credential applies.
        self.resource_scope = resource_scope
        # The time of the last modification in UTC, formatted according to RFC 3339.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.bound_agents:
            for v1 in self.bound_agents:
                 if v1:
                    v1.validate()
        if self.resource_refs:
            for v1 in self.resource_refs:
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

        result['resourceRefs'] = []
        if self.resource_refs is not None:
            for k1 in self.resource_refs:
                result['resourceRefs'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope

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

        self.resource_refs = []
        if m.get('resourceRefs') is not None:
            for k1 in m.get('resourceRefs'):
                temp_model = main_models.GetCredentialResponseBodyDataResourceRefs()
                self.resource_refs.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            self.resource_scope = m.get('resourceScope')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetCredentialResponseBodyDataResourceRefs(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The unique identifier of the resource.
        self.resource_id = resource_id
        # The resource name. This value is empty if the resource has been deleted.
        self.resource_name = resource_name
        # The resource type, such as agent.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class GetCredentialResponseBodyDataBoundAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The agent name.
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

