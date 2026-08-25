# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The binding details of the external identity provider.
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
            temp_model = main_models.GetIdentityProviderResponseBodyData()
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

class GetIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        metadata: main_models.GetIdentityProviderResponseBodyDataMetadata = None,
        status: str = None,
        sync_enabled: bool = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The creation time in UTC, formatted according to RFC 3339.
        self.created_at = created_at
        # The event subscription callback URL. Configure this URL in the application on the external identity provider side to receive organization change events. An empty string is returned if the user pool has not been provisioned.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The type of the external identity provider. Valid values: DingTalk, Feishu.
        self.identity_provider_type = identity_provider_type
        # The logon callback URL. Configure this URL in the application on the external identity provider side. An empty string is returned if the user pool has not been provisioned.
        self.login_callback_url = login_callback_url
        # Indicates whether workspace users are allowed to log on through this external identity provider.
        self.login_enabled = login_enabled
        # The application configuration of the external identity provider. Application secret configurations are not returned.
        self.metadata = metadata
        # The status. Valid values:
        # - CONFIGURED: The configuration has been accepted and is waiting for the user pool to be provisioned.
        # - SYNCING: Organization members are being synchronized.
        # - SYNCED: Organization member synchronization is complete.
        # - READY: The binding is active.
        # - SYNC_FAILED: Organization member synchronization failed.
        # - UPDATING: The configuration is being updated.
        # - UPDATE_FAILED: The configuration update failed.
        # - DISCONNECTING: The binding is being removed.
        # - DISCONNECT_FAILED: The unbinding failed.
        self.status = status
        # Indicates whether organization member synchronization is enabled. When enabled, the external identity provider synchronizes organization members as workspace users.
        self.sync_enabled = sync_enabled
        # The time of the last modification in UTC, formatted according to RFC 3339.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.event_subscription_callback_url is not None:
            result['eventSubscriptionCallbackUrl'] = self.event_subscription_callback_url

        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.login_callback_url is not None:
            result['loginCallbackUrl'] = self.login_callback_url

        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('eventSubscriptionCallbackUrl') is not None:
            self.event_subscription_callback_url = m.get('eventSubscriptionCallbackUrl')

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('loginCallbackUrl') is not None:
            self.login_callback_url = m.get('loginCallbackUrl')

        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('metadata') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetIdentityProviderResponseBodyDataMetadata(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        corp_id: str = None,
    ):
        # The App ID of the Lark application. Required when the binding type is Feishu.
        self.app_id = app_id
        # The AppKey of the DingTalk application. Required when the binding type is DingTalk.
        self.app_key = app_key
        # The CorpId of the DingTalk enterprise. Required when the binding type is DingTalk.
        self.corp_id = corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        return self

