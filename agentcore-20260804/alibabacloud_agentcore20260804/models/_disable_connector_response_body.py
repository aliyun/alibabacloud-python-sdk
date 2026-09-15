# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DisableConnectorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DisableConnectorResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The Connector details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
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
            temp_model = main_models.DisableConnectorResponseBodyData()
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

class DisableConnectorResponseBodyData(DaraModel):
    def __init__(
        self,
        bound_agent_count: int = None,
        enabled_at: str = None,
        metadata: str = None,
        name: str = None,
        status: str = None,
    ):
        # The number of Agents bound to the Connector.
        self.bound_agent_count = bound_agent_count
        # The time when the Connector was enabled.
        self.enabled_at = enabled_at
        # A JSON string. For qodercli: {"site":"global|cn","organizationId":"...","apiKey":"...","serviceAccountKeys":[{"id":"ckey-xxx","name":"default","serviceAccountKey":"..."}]}. This field is empty when the Connector is not enabled.
        self.metadata = metadata
        # The Connector name.
        self.name = name
        # The Connector status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_agent_count is not None:
            result['boundAgentCount'] = self.bound_agent_count

        if self.enabled_at is not None:
            result['enabledAt'] = self.enabled_at

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boundAgentCount') is not None:
            self.bound_agent_count = m.get('boundAgentCount')

        if m.get('enabledAt') is not None:
            self.enabled_at = m.get('enabledAt')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

