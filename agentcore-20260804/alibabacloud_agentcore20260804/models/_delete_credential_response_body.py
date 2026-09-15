# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DeleteCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteCredentialResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The information about the deleted credential.
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
            temp_model = main_models.DeleteCredentialResponseBodyData()
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

class DeleteCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        name: str = None,
        workspace_id: str = None,
    ):
        # The credential ID.
        self.credential_id = credential_id
        # The credential name. The name must be unique within the workspace and can contain only letters, digits, periods (.), underscores (_), and hyphens (-). The name must be 3 to 128 characters in length and cannot use runtime reserved names.
        self.name = name
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.name is not None:
            result['name'] = self.name

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

