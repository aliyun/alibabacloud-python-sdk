# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListModelConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListModelConnectionsResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code. A value of SUCCESS indicates success.
        self.code = code
        # The HTTP status code. A value of 200 indicates success.
        self.http_status_code = http_status_code
        # The list of model connections.
        self.items = items
        # The number of records per page. Valid values: 0 to 100. If this parameter is not set or is set to 0, the default value 10 is used.
        self.max_results = max_results
        # The request processing result message.
        self.message = message
        # The pagination token. Pass the token returned in the previous query. An empty response indicates that no more pages are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of resources that match the query conditions.
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
                temp_model = main_models.ListModelConnectionsResponseBodyItems()
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

class ListModelConnectionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        api_key_count: int = None,
        connection_id: str = None,
        created_at: str = None,
        credential_configured: bool = None,
        description: str = None,
        endpoint: str = None,
        models: List[main_models.ListModelConnectionsResponseBodyItemsModels] = None,
        name: str = None,
        protocol: str = None,
        provider_type: str = None,
        status: str = None,
        status_reason: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The number of API keys configured for the model connection.
        self.api_key_count = api_key_count
        # The model connection ID.
        self.connection_id = connection_id
        # The time when the resource was created, in RFC 3339 UTC format.
        self.created_at = created_at
        # Indicates whether access credentials have been configured for the model connection.
        self.credential_configured = credential_configured
        # The description of the model connection. Maximum length: 255 characters.
        self.description = description
        # The absolute HTTP or HTTPS address of the upstream model service. Maximum length: 1024 characters.
        self.endpoint = endpoint
        # The list of model summaries associated with the model connection.
        self.models = models
        # The model connection name. The name must be 1 to 128 non-whitespace characters in length.
        self.name = name
        # The model invocation protocol. Currently only OpenAI/v1 is supported. If not configured in Settings when the model connection is created, this default value is used.
        self.protocol = protocol
        # The model provider type.
        self.provider_type = provider_type
        # The resource status.
        self.status = status
        # The failure summary returned when the model connection fails to be published or fails to be deleted but remains in the Deleting state. This value is empty for other states.
        self.status_reason = status_reason
        # The time when the resource was last updated, in RFC 3339 UTC format.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_count is not None:
            result['apiKeyCount'] = self.api_key_count

        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.credential_configured is not None:
            result['credentialConfigured'] = self.credential_configured

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.provider_type is not None:
            result['providerType'] = self.provider_type

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyCount') is not None:
            self.api_key_count = m.get('apiKeyCount')

        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('credentialConfigured') is not None:
            self.credential_configured = m.get('credentialConfigured')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.ListModelConnectionsResponseBodyItemsModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListModelConnectionsResponseBodyItemsModels(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
    ):
        # The model ID.
        self.model_id = model_id
        # The upstream model name.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        return self

