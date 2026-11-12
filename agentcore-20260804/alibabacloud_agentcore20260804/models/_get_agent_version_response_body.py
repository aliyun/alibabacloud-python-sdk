# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentVersionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value is SUCCESS if the request is successful, or an error code if the request fails.
        self.code = code
        # The details of the fixed agent version. The configuration field contains the agent configuration at the time the version was saved.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message. The value is success if the request is successful, or an error message if the request fails.
        self.message = message
        # The request ID, which is used to locate and troubleshoot the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.GetAgentVersionResponseBodyData()
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

class GetAgentVersionResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        artifact_status: str = None,
        configuration: Dict[str, Any] = None,
        created_at: str = None,
        created_by: str = None,
        description: str = None,
        target_spec_version: int = None,
        version_name: str = None,
        workspace_id: str = None,
    ):
        # The ID of the managed or custom agent to which the version belongs.
        self.agent_id = agent_id
        # The system-generated version number that increments for the agent, such as v1 and v2. This is used when querying or deleting versions, and when server endpoints reference the version.
        self.agent_version = agent_version
        # Indicates only whether the version template and artifact archive are complete, and does not represent the deployment or running status. Valid values: READY indicates that the archive is complete. INVALID indicates that the archive is missing or inconsistent.
        self.artifact_status = artifact_status
        # For managed agents, the structure is consistent with the data structure of GetManagedAgent. For custom agents, the structure is consistent with the data structure of GetCustomAgent. The data masking rules are the same.
        self.configuration = configuration
        # The time when the version was saved, in ISO 8601 UTC format.
        self.created_at = created_at
        # The UID of the Alibaba Cloud account of the caller who saved the version. If the API is called by a RAM user, this is the UID of the Alibaba Cloud account to which the RAM user belongs.
        self.created_by = created_by
        # The version description provided when the version was saved. It can be up to 1,024 characters in length. If no description was provided when the version was saved, this field is empty.
        self.description = description
        # The effective release sequence number of the agent when the version was saved, which is the effectiveSpecVersion at that time. This value does not change after the version is saved.
        self.target_spec_version = target_spec_version
        # The display name specified by the user when the version was saved. For earlier saved versions where no name was recorded, the agentVersion is returned.
        self.version_name = version_name
        # The ID of the AgentCore workspace where the agent that owns this version resides.
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

        if self.agent_version is not None:
            result['agentVersion'] = self.agent_version

        if self.artifact_status is not None:
            result['artifactStatus'] = self.artifact_status

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.target_spec_version is not None:
            result['targetSpecVersion'] = self.target_spec_version

        if self.version_name is not None:
            result['versionName'] = self.version_name

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentVersion') is not None:
            self.agent_version = m.get('agentVersion')

        if m.get('artifactStatus') is not None:
            self.artifact_status = m.get('artifactStatus')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('targetSpecVersion') is not None:
            self.target_spec_version = m.get('targetSpecVersion')

        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

