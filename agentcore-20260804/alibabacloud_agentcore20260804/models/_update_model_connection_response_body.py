# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateModelConnectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateModelConnectionResponseBodyData = None,
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
            temp_model = main_models.UpdateModelConnectionResponseBodyData()
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

class UpdateModelConnectionResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key_count: int = None,
        connection_id: str = None,
        created_at: str = None,
        credential_configured: bool = None,
        description: str = None,
        endpoint: str = None,
        name: str = None,
        protocol: str = None,
        provider_type: str = None,
        status: str = None,
        status_reason: str = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        self.api_key_count = api_key_count
        self.connection_id = connection_id
        self.created_at = created_at
        self.credential_configured = credential_configured
        self.description = description
        self.endpoint = endpoint
        self.name = name
        self.protocol = protocol
        self.provider_type = provider_type
        self.status = status
        self.status_reason = status_reason
        self.updated_at = updated_at
        self.workspace_id = workspace_id

    def validate(self):
        pass

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

