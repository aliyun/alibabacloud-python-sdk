# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DeleteCustomAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteCustomAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code of the request. The value is SUCCESS if the request is successful.
        self.code = code
        # The summary of the custom code or image agent whose deletion has been accepted. Runtime resources are subsequently cleaned up in the background.
        self.data = data
        # The HTTP status code of the request. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The processing result description of the request. The value is success if the request is successful.
        self.message = message
        # The unique identifier of the request. It is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of true indicates that the request was successful. A successful creation, update, or deletion does not mean that the background operations are complete.
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
            temp_model = main_models.DeleteCustomAgentResponseBodyData()
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

class DeleteCustomAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
        access_scope: str = None,
        agent_id: str = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        latest_spec_version: int = None,
        name: str = None,
        runtime: str = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The inbound access mode.
        self.access_mode = access_mode
        # The user access scope.
        self.access_scope = access_scope
        # The unique identifier of the custom code or image agent. You can obtain this value from the response of CreateCustomAgent or ListCustomAgents.
        self.agent_id = agent_id
        # The creation method of the agent. The value is CUSTOM for custom code or image agents.
        self.create_mode = create_mode
        # The time when the agent was created. The time is in ISO 8601 format. A trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.created_at = created_at
        # The deployment method of the agent. Custom code or image agents are deployed and managed by the platform, and the value is MANAGED.
        self.deploy_type = deploy_type
        # The description of the agent.
        self.description = description
        # The current latest configuration version number. Updates with the same configuration may retain the original version number. This field does not indicate that the configuration has taken effect.
        self.latest_spec_version = latest_spec_version
        # The name of the custom code or image agent.
        self.name = name
        # The compute specifications of the agent. Valid values: INTERACTIVE, STANDARD, and HEAVY.
        self.runtime = runtime
        # The overall status of the agent. Valid values: Creating (the agent is being created), Running (the agent is running), Failed (the agent failed), Updating (the agent is being updated), Deleting (the agent is being deleted), and Deleted (the agent is deleted). Call GetCustomAgent to query the execution progress of the latest configuration.
        self.status = status
        # The time when the agent was last updated. The time is in ISO 8601 format. A trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.updated_at = updated_at
        # The ID of the workspace to which the custom code or image agent belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['accessMode'] = self.access_mode

        if self.access_scope is not None:
            result['accessScope'] = self.access_scope

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

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.name is not None:
            result['name'] = self.name

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessMode') is not None:
            self.access_mode = m.get('accessMode')

        if m.get('accessScope') is not None:
            self.access_scope = m.get('accessScope')

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

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

