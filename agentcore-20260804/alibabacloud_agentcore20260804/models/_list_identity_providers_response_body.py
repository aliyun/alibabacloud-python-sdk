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
        # The maximum number of records per page for this query.
        self.max_results = max_results
        # The response message. Returns an error description when the request fails.
        self.message = message
        # The token for the next page. Empty if there is no next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of external identity providers that meet the query conditions.
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
        oidc: main_models.ListIdentityProvidersResponseBodyItemsOidc = None,
        protocol: str = None,
        saml: main_models.ListIdentityProvidersResponseBodyItemsSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.ListIdentityProvidersResponseBodyItemsSyncScope = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The actual upstream configuration. The actual SAML configuration is read on demand only in GetIdentityProvider. SCIM queries and preparations return the actual receiving status and URL.
        self.configuration = configuration
        # The creation time in UTC format based on RFC 3339.
        self.created_at = created_at
        # The event subscription callback URL. You must configure this URL in the application of the external identity provider to receive organization change events. An empty string is returned when the user pool is not activated.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The type of the external identity provider. Valid values: DingTalk and Feishu.
        self.identity_provider_type = identity_provider_type
        # The logon callback URL. You must configure this URL in the application of the external identity provider. An empty string is returned when the user pool is not activated.
        self.login_callback_url = login_callback_url
        # Specifies whether workspace users are allowed to log on through this external identity provider.
        self.login_enabled = login_enabled
        # The application configuration of the external identity provider. Application secret configurations are not returned.
        self.metadata = metadata
        # The security summary of the expected configuration. It does not contain credentials. The original SAML fields and meanings are retained.
        self.oidc = oidc
        # Currently, only SAML is supported. It may not be returned when no valid configuration is saved. OIDC placeholder initialization is not supported.
        self.protocol = protocol
        # The input supports either XML or complete manual entry. The query returns the standardized configuration and does not echo the original XML. It can be omitted when not configured.
        self.saml = saml
        # The binding status. Valid values: CONFIGURED (the configuration is accepted, waiting for the user pool to be activated), SYNCING (synchronizing organization members), SYNCED (organization member synchronization is completed), READY (the binding is in effect), SYNC_FAILED (organization member synchronization failed), UPDATING (updating the configuration), UPDATE_FAILED (configuration update failed), DISCONNECTING (disconnecting), and DISCONNECT_FAILED (disconnection failed).
        self.status = status
        # Specifies whether organization member synchronization is enabled. When enabled, organization members are synchronized as workspace users from this external identity provider.
        self.sync_enabled = sync_enabled
        # Follows the department-based sync scope definition. If omitted during creation, it defaults to AllAuthorized, and the first vendor sync is determined by syncOnBind. If omitted or null during an update, the original value is retained. Updating and saving the scope does not automatically trigger a full sync.
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
        if self.oidc:
            self.oidc.validate()
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

        if self.oidc is not None:
            result['oidc'] = self.oidc.to_map()

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

        if m.get('oidc') is not None:
            temp_model = main_models.ListIdentityProvidersResponseBodyItemsOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

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
        # When set to SelectedDepartments, it must contain at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When set to AllAuthorized, pass an empty array or omit this field.
        self.department_ids = department_ids
        # AllAuthorized: the full authorized scope, limited by the application address book authorization. SelectedDepartments: the selected departments and all their sub-departments. A valid mode must be provided and verified by the backend when explicitly submitting syncScope.
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
        # The SAML binding type, such as HTTP-Redirect or HTTP-POST. This parameter is required for manual configuration. The query returns the short name.
        self.binding_type = binding_type
        # Required when manually filled in. It must be non-empty and no more than 2048 characters. Existing configurations do not support replacement. It is different from our Entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually filled in. It must be an absolute HTTPS URL without user credentials and fragments.
        self.login_url = login_url
        # The list of IdP signing certificates. A non-empty array is required for manual configuration. Use PEM X.509 certificate text. The system validates the current validity period. A maximum of two unique certificates are allowed.
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

class ListIdentityProvidersResponseBodyItemsOidc(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_auth_method: str = None,
        client_id: str = None,
        discovery_endpoint: str = None,
        issuer: str = None,
        jwks_uri: str = None,
        pkce_required: bool = None,
        scopes: List[str] = None,
        sso_mapping_claim: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.authorization_endpoint = authorization_endpoint
        # The client authentication method. Default value: client_secret_post. If the value is none, PKCE must be enabled.
        self.client_auth_method = client_auth_method
        # The client identifier registered in the external IdP, which is different from the Matrix client. In-place replacement is not supported after configuration.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint. This parameter is mutually exclusive with manually specified endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer of the external IdP. In-place replacement is not supported after configuration.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. This parameter must be set to true when no client authentication is used.
        self.pkce_required = pkce_required
        # The array of scopes. The array must contain openid. Default values: openid, profile, and email.
        self.scopes = scopes
        # The claim name in the ID token used to match the SCIM externalId. If omitted during initial configuration, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can enter oid. The value must be non-empty and cannot contain whitespace characters. In query results, oidc returns the saved value, and oidcConfiguration returns the actual upstream value, which may be empty.
        self.sso_mapping_claim = sso_mapping_claim
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.token_endpoint = token_endpoint
        # The optional absolute HTTPS URL in manual mode. Do not specify this parameter in discovery mode.
        self.userinfo_endpoint = userinfo_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_endpoint is not None:
            result['authorizationEndpoint'] = self.authorization_endpoint

        if self.client_auth_method is not None:
            result['clientAuthMethod'] = self.client_auth_method

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.discovery_endpoint is not None:
            result['discoveryEndpoint'] = self.discovery_endpoint

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.jwks_uri is not None:
            result['jwksUri'] = self.jwks_uri

        if self.pkce_required is not None:
            result['pkceRequired'] = self.pkce_required

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.sso_mapping_claim is not None:
            result['ssoMappingClaim'] = self.sso_mapping_claim

        if self.token_endpoint is not None:
            result['tokenEndpoint'] = self.token_endpoint

        if self.userinfo_endpoint is not None:
            result['userinfoEndpoint'] = self.userinfo_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationEndpoint') is not None:
            self.authorization_endpoint = m.get('authorizationEndpoint')

        if m.get('clientAuthMethod') is not None:
            self.client_auth_method = m.get('clientAuthMethod')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('discoveryEndpoint') is not None:
            self.discovery_endpoint = m.get('discoveryEndpoint')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('jwksUri') is not None:
            self.jwks_uri = m.get('jwksUri')

        if m.get('pkceRequired') is not None:
            self.pkce_required = m.get('pkceRequired')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('ssoMappingClaim') is not None:
            self.sso_mapping_claim = m.get('ssoMappingClaim')

        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')

        if m.get('userinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('userinfoEndpoint')

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
        # The SAML Binding URI in the historical metadata snapshot. Use saml.bindingType for CustomSSO updates.
        self.binding = binding
        # The certificate string in the historical metadata snapshot. Use saml.x509Certificates to edit the configuration, and do not submit the old metadata.
        self.certificates = certificates
        # The CorpId of the DingTalk enterprise. Required when the binding type is DingTalk.
        self.corp_id = corp_id
        # Required when manually filled in. It must be non-empty and no more than 2048 characters. Existing configurations do not support replacement. It is different from our Entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually filled in. It must be an absolute HTTPS URL without user credentials and fragments.
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
        # The SAML binding type, such as HTTP-Redirect or HTTP-POST. This parameter is required for manual configuration. The query returns the short name.
        self.binding_type = binding_type
        # Required when manually filled in. It must be non-empty and no more than 2048 characters. Existing configurations do not support replacement. It is different from our Entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually filled in. It must be an absolute HTTPS URL without user credentials and fragments.
        self.login_url = login_url
        # The actual SSO logon status of AgentIdentity. The actual switch value is Enabled or Disabled, which is not equivalent to the expected loginEnabled value saved in AC.
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

