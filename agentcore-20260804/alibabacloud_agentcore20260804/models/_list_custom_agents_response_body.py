# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListCustomAgentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListCustomAgentsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The result code of the request. The value is SUCCESS if the request is successful.
        self.code = code
        # The HTTP status code of the request. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The list of custom agent summaries on the current page. To obtain the complete configuration and the execution results of the latest version, call GetCustomAgent.
        self.items = items
        # The maximum number of entries returned per page for this query.
        self.max_results = max_results
        # The description of the processing result for this request. The value is success if the request is successful.
        self.message = message
        # The opaque token used to query the next page. If this value is empty, no more pages are available. Pass this value as is in subsequent requests.
        self.next_token = next_token
        # The unique identifier of the request. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates that the request was processed successfully. A successful creation, update, or deletion does not indicate that the background operation is complete.
        self.success = success
        # The total number of custom agents that meet the query conditions in the specified workspace.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListCustomAgentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCustomAgentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        latest_spec_version: int = None,
        name: str = None,
        protocol: List[main_models.ListCustomAgentsResponseBodyItemsProtocol] = None,
        runtime: str = None,
        status: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The unique identifier of the custom agent. You can obtain this value from the response of CreateCustomAgent or ListCustomAgents.
        self.agent_id = agent_id
        # The creation method of the agent. The value is CUSTOM for custom agents.
        self.create_mode = create_mode
        # The time when the agent was created. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.created_at = created_at
        # The deployment method of the agent. Custom agents are deployed and managed by the platform. The value is MANAGED for custom agents.
        self.deploy_type = deploy_type
        # The description of the agent.
        self.description = description
        # The latest configuration version number. Updates with the same configuration may retain the original version number. This field does not indicate that the configuration has taken effect.
        self.latest_spec_version = latest_spec_version
        # The name of the custom agent.
        self.name = name
        # The list of invocation protocol configurations for the agent.
        self.protocol = protocol
        # The compute specifications of the agent. Valid values: INTERACTIVE, STANDARD, and HEAVY.
        self.runtime = runtime
        # The overall status of the agent. Valid values:
        # - Creating: The agent is being created.
        # - Running: The agent is running.
        # - Failed: The agent failed.
        # - Updating: The agent is being updated.
        # - Deleting: The agent is being deleted.
        # - Deleted: The agent is deleted.
        # To check the execution progress of the latest configuration, call GetCustomAgent.
        self.status = status
        # The time when the agent was last updated. The time is in ISO 8601 format. The trailing Z indicates the UTC time zone. Fractional seconds may be included.
        self.updated_at = updated_at
        # The ID of the workspace to which the custom agent belongs.
        self.workspace_id = workspace_id

    def validate(self):
        if self.protocol:
            for v1 in self.protocol:
                 if v1:
                    v1.validate()

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

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.name is not None:
            result['name'] = self.name

        result['protocol'] = []
        if self.protocol is not None:
            for k1 in self.protocol:
                result['protocol'].append(k1.to_map() if k1 else None)

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

        self.protocol = []
        if m.get('protocol') is not None:
            for k1 in m.get('protocol'):
                temp_model = main_models.ListCustomAgentsResponseBodyItemsProtocol()
                self.protocol.append(temp_model.from_map(k1))

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListCustomAgentsResponseBodyItemsProtocol(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        paths: List[main_models.ListCustomAgentsResponseBodyItemsProtocolPaths] = None,
        type: str = None,
    ):
        # The request header configuration of the current protocol. The key is the header name and the value is a string.
        self.headers = headers
        # The list of API paths corresponding to the current protocol.
        self.paths = paths
        # The invocation protocol type. Valid values:
        # - agui: AG-UI protocol.
        # - openai-chat-completion: OpenAI Chat Completions compatible protocol.
        # - custom: Custom protocol.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        result['paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['paths'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        self.paths = []
        if m.get('paths') is not None:
            for k1 in m.get('paths'):
                temp_model = main_models.ListCustomAgentsResponseBodyItemsProtocolPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListCustomAgentsResponseBodyItemsProtocolPaths(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the current API path.
        self.description = description
        # The API path corresponding to the current protocol.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

