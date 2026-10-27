# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListIdentityProvidersResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of external identity providers.
        self.items = items
        # The maximum number of records per page that takes effect in this query.
        self.max_results = max_results
        # The response message. Returns an error description if the request fails.
        self.message = message
        # The cursor for the next page. Empty if there is no next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of external identity providers that match the query conditions.
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
                temp_model = main_models.ListIdentityProvidersResponseBodyItems()
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

class ListIdentityProvidersResponseBodyItems(DaraModel):
    def __init__(
        self,
        configuration: main_models.ListIdentityProvidersResponseBodyItemsConfiguration = None,
        created_at: str = None,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        metadata: main_models.ListIdentityProvidersResponseBodyItemsMetadata = None,
        protocol: str = None,
        saml: main_models.ListIdentityProvidersResponseBodyItemsSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.ListIdentityProvidersResponseBodyItemsSyncScope = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration is retrieved on demand only through GetIdentityProvider. SCIM queries and provisioning return the actual receiving status and URL.
        self.configuration = configuration
        # The creation time in UTC format based on RFC 3339.
        self.created_at = created_at
        # The event subscription callback URL. Configure this URL in the external identity provider application to receive organization change events. Returns an empty string if the user pool is not activated.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The type of the external identity provider. Valid values: DingTalk, Feishu.
        self.identity_provider_type = identity_provider_type
        # The logon callback URL. Configure this URL in the external identity provider application. Returns an empty string if the user pool is not activated.
        self.login_callback_url = login_callback_url
        # Specifies whether workspace users are allowed to log on through this external identity provider.
        self.login_enabled = login_enabled
        # The application configuration of the external identity provider. Application secret configurations are not returned.
        self.metadata = metadata
        # Only SAML is currently supported. May not be returned if no valid configuration is saved. OIDC placeholder initialization is not supported.
        self.protocol = protocol
        # Input supports either XML or full manual entry. Queries return the standardized configuration and do not echo the original XML. Can be omitted if not configured.
        self.saml = saml
        # The binding status. Valid values: CONFIGURED (the configuration is accepted and waiting for user pool activation), SYNCING (synchronizing organization members), SYNCED (organization member synchronization is completed), READY (the binding is effective), SYNC_FAILED (organization member synchronization failed), UPDATING (updating the configuration), UPDATE_FAILED (configuration update failed), DISCONNECTING (disconnecting), DISCONNECT_FAILED (disconnection failed).
        self.status = status
        # Specifies whether to enable organization member synchronization. If enabled, the external identity provider synchronizes organization members as workspace users.
        self.sync_enabled = sync_enabled
        # Follows the department-based synchronization scope definition. If omitted during creation, the default is AllAuthorized. The first vendor synchronization is determined by syncOnBind. If omitted or null during an update, the original value is retained. Updating the saved scope does not automatically trigger full synchronization.
        self.sync_scope = sync_scope
        # The time of the last modification in UTC format based on RFC 3339.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.metadata:
            self.metadata.validate()
        if self.saml:
            self.saml.validate()
        if self.sync_scope:
            self.sync_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

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

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.sync_scope is not None:
            result['syncScope'] = self.sync_scope.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.ListIdentityProvidersResponseBodyItemsConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

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
            temp_model = main_models.ListIdentityProvidersResponseBodyItemsMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.ListIdentityProvidersResponseBodyItemsSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.ListIdentityProvidersResponseBodyItemsSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListIdentityProvidersResponseBodyItemsSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # Must contain at least one non-empty department ID when set to SelectedDepartments. The IDs should be obtained from ListIdentityProviderDepartments. Pass an empty array or omit this parameter when set to AllAuthorized.
        self.department_ids = department_ids
        # AllAuthorized: the full authorization scope, limited by the application address book authorization. SelectedDepartments: the selected departments and all their sub-departments. A valid mode must be provided and verified by the backend when syncScope is explicitly submitted.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_ids is not None:
            result['departmentIds'] = self.department_ids

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIds') is not None:
            self.department_ids = m.get('departmentIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

class ListIdentityProvidersResponseBodyItemsSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. Must be non-empty and up to 2048 characters. Existing configurations cannot be changed. This is different from the local entity ID returned by SP queries.
        self.entity_id = entity_id
        # Required for manual entry. Must be an absolute HTTPS URL without user credentials or fragments.
        self.login_url = login_url
        # Required as a non-empty array for manual entry. Uses PEM X.509 certificate text. Validates the current validity period. A maximum of two certificates are allowed after deduplication.
        self.x_509certificates = x_509certificates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['bindingType'] = self.binding_type

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        if self.x_509certificates is not None:
            result['x509Certificates'] = self.x_509certificates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingType') is not None:
            self.binding_type = m.get('bindingType')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        if m.get('x509Certificates') is not None:
            self.x_509certificates = m.get('x509Certificates')

        return self

class ListIdentityProvidersResponseBodyItemsMetadata(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        binding: str = None,
        certificates: str = None,
        corp_id: str = None,
        entity_id: str = None,
        login_url: str = None,
    ):
        # The App ID of the Lark application. Required when the binding type is Feishu.
        self.app_id = app_id
        # The AppKey of the DingTalk application. Required when the binding type is DingTalk.
        self.app_key = app_key
        # The SAML binding URI in the historical metadata snapshot. Use saml.bindingType for CustomSSO updates.
        self.binding = binding
        # The certificate string in the historical metadata snapshot. Use saml.x509Certificates to edit the configuration. Do not submit the old metadata.
        self.certificates = certificates
        # The CorpId of the DingTalk enterprise. Required when the binding type is DingTalk.
        self.corp_id = corp_id
        # Required for manual entry. Must be non-empty and up to 2048 characters. Existing configurations cannot be changed. This is different from the local entity ID returned by SP queries.
        self.entity_id = entity_id
        # Required for manual entry. Must be an absolute HTTPS URL without user credentials or fragments.
        self.login_url = login_url

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

        if self.binding is not None:
            result['binding'] = self.binding

        if self.certificates is not None:
            result['certificates'] = self.certificates

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('binding') is not None:
            self.binding = m.get('binding')

        if m.get('certificates') is not None:
            self.certificates = m.get('certificates')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        return self

class ListIdentityProvidersResponseBodyItemsConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. Must be non-empty and up to 2048 characters. Existing configurations cannot be changed. This is different from the local entity ID returned by SP queries.
        self.entity_id = entity_id
        # Required for manual entry. Must be an absolute HTTPS URL without user credentials or fragments.
        self.login_url = login_url
        # The actual switch value is Enabled or Disabled. This is not equivalent to the expected loginEnabled value saved in AC.
        self.sso_status = sso_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['bindingType'] = self.binding_type

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        if self.sso_status is not None:
            result['ssoStatus'] = self.sso_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingType') is not None:
            self.binding_type = m.get('bindingType')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        if m.get('ssoStatus') is not None:
            self.sso_status = m.get('ssoStatus')

        return self

