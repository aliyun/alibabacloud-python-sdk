# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class DeleteIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DeleteIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The binding information of the external identity provider after the unbinding operation is accepted.
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
            temp_model = main_models.DeleteIdentityProviderResponseBodyData()
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

class DeleteIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        identity_provider_type: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The type of the external identity provider. Valid values: DingTalk, Feishu.
        self.identity_provider_type = identity_provider_type
        # The status. Valid values:
        # - CONFIGURED: The configuration has been accepted and is waiting for the user pool to be provisioned.
        # - SYNCING: Organization members are being synchronized.
        # - SYNCED: Organization member synchronization is complete.
        # - READY: The binding is in effect.
        # - SYNC_FAILED: Organization member synchronization failed.
        # - UPDATING: The configuration is being updated.
        # - UPDATE_FAILED: Configuration update failed.
        # - DISCONNECTING: The unbinding is in progress.
        # - DISCONNECT_FAILED: The unbinding failed.
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.status is not None:
            result['status'] = self.status

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

