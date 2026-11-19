# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

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
        # The response message. Returns an error description when the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
        configuration: main_models.GetIdentityProviderResponseBodyDataConfiguration = None,
        created_at: str = None,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        metadata: main_models.GetIdentityProviderResponseBodyDataMetadata = None,
        oidc: main_models.GetIdentityProviderResponseBodyDataOidc = None,
        oidc_configuration: main_models.GetIdentityProviderResponseBodyDataOidcConfiguration = None,
        protocol: str = None,
        saml: main_models.GetIdentityProviderResponseBodyDataSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.GetIdentityProviderResponseBodyDataSyncScope = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration is read back on demand only in GetIdentityProvider. SCIM queries and preparations return the actual received status and URLs.
        self.configuration = configuration
        # The creation time in UTC format based on RFC 3339.
        self.created_at = created_at
        # The event subscription callback URL. You must configure this URL in the application of the external identity provider to receive organization change events. An empty string is returned when the user pool is not yet activated.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The type of the external identity provider. Valid values: DingTalk and Feishu.
        self.identity_provider_type = identity_provider_type
        # The logon callback URL. You must configure this URL in the application of the external identity provider. An empty string is returned when the user pool is not yet activated.
        self.login_callback_url = login_callback_url
        # Indicates whether workspace users are allowed to log on through this external identity provider.
        self.login_enabled = login_enabled
        # The application configuration of the external identity provider. Application secret configurations are not returned.
        self.metadata = metadata
        # The security summary of the expected configuration. It does not contain credentials. The original SAML fields and meanings are retained.
        self.oidc = oidc
        # The security summary queried in real time from AgentIdentity. It does not contain secrets, private keys, or JIT fields. It can be empty when it is not configured or during unbinding.
        self.oidc_configuration = oidc_configuration
        # Currently, only SAML is supported. This parameter may not be returned when no valid configuration is saved. Placeholder initialization with OIDC is not supported.
        self.protocol = protocol
        # The input supports either XML or complete manual entry. Queries return standardized configurations and do not echo the original XML. This parameter can be omitted when not configured.
        self.saml = saml
        # The status. Valid values:
        # - CONFIGURED: The configuration is accepted and waiting for the user pool to be activated.
        # - SYNCING: Organization members are being synchronized.
        # - SYNCED: The synchronization of organization members is complete.
        # - READY: The binding is in effect.
        # - SYNC_FAILED: The synchronization of organization members failed.
        # - UPDATING: The configuration is being updated.
        # - UPDATE_FAILED: The configuration update failed.
        # - DISCONNECTING: The binding is being disconnected.
        # - DISCONNECT_FAILED: The disconnection failed.
        self.status = status
        # Indicates whether organization member synchronization is enabled. When enabled, organization members are synchronized as workspace users by this external identity provider.
        self.sync_enabled = sync_enabled
        # The synchronization scope defined by department. If omitted during creation, the default value is AllAuthorized, and the first vendor synchronization is determined by syncOnBind. If omitted or set to null during an update, the original value is retained. Updating and saving the scope does not automatically trigger a full synchronization.
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
        if self.oidc_configuration:
            self.oidc_configuration.validate()
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

        if self.oidc_configuration is not None:
            result['oidcConfiguration'] = self.oidc_configuration.to_map()

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
            temp_model = main_models.GetIdentityProviderResponseBodyDataConfiguration()
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
            temp_model = main_models.GetIdentityProviderResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('oidc') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyDataOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('oidcConfiguration') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyDataOidcConfiguration()
            self.oidc_configuration = temp_model.from_map(m.get('oidcConfiguration'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyDataSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetIdentityProviderResponseBodyDataSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # When the mode is SelectedDepartments, this list must contain at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When the mode is AllAuthorized, pass an empty array or omit this parameter.
        self.department_ids = department_ids
        # The scope mode. Valid values: AllAuthorized (all authorized scopes, limited by application address book authorization) and SelectedDepartments (selected departments and all their sub-departments). A valid mode must be provided when explicitly submitting syncScope and is verified by the backend.
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

class GetIdentityProviderResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. This parameter is required when manually filled in. Queries return short names.
        self.binding_type = binding_type
        # This parameter is required when manually filled in. It must be non-empty and contain a maximum of 2,048 characters. Existing configurations do not support replacement. It is different from the Entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # This parameter is required when manually filled in. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # When manually filled in, a non-empty array is required, using PEM X.509 certificate text. The current validity period is verified, and a maximum of two certificates are allowed after deduplication.
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

class GetIdentityProviderResponseBodyDataOidcConfiguration(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_auth_method: str = None,
        client_id: str = None,
        discovery_endpoint: str = None,
        has_client_private_key: bool = None,
        has_client_secret: bool = None,
        issuer: str = None,
        jwks_uri: str = None,
        pkce_required: bool = None,
        scopes: List[str] = None,
        sso_mapping_claim: str = None,
        sso_status: str = None,
        token_endpoint: str = None,
        userinfo_endpoint: str = None,
    ):
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.authorization_endpoint = authorization_endpoint
        # The default value is client_secret_post. If the value is none, PKCE must be enabled.
        self.client_auth_method = client_auth_method
        # The client identifier registered in the external IdP, which is different from the Matrix client. In-place replacement is not supported after configuration.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint. It is mutually exclusive with manually entered endpoints.
        self.discovery_endpoint = discovery_endpoint
        # Indicates whether the client secret is saved. Only the existence status is returned, not the plaintext.
        self.has_client_private_key = has_client_private_key
        # Indicates whether the client secret is saved. Only the existence status is returned, not the plaintext.
        self.has_client_secret = has_client_secret
        # The absolute HTTPS issuer of the external IdP. In-place replacement is not supported after configuration.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. It must be set to true when no client authentication is used.
        self.pkce_required = pkce_required
        # An array of strings that must contain openid. The default values are openid, profile, and email.
        self.scopes = scopes
        # The claim name in the ID token used to match the SCIM externalId. If omitted during initial creation, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can enter oid. The value must be non-empty and cannot contain whitespace characters. When you query oidc, the saved value is returned. When you query oidcConfiguration, the actual upstream value is returned, which may be empty.
        self.sso_mapping_claim = sso_mapping_claim
        # The current upstream logon switch, which is Enabled or Disabled.
        self.sso_status = sso_status
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

        if self.has_client_private_key is not None:
            result['hasClientPrivateKey'] = self.has_client_private_key

        if self.has_client_secret is not None:
            result['hasClientSecret'] = self.has_client_secret

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

        if self.sso_status is not None:
            result['ssoStatus'] = self.sso_status

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

        if m.get('hasClientPrivateKey') is not None:
            self.has_client_private_key = m.get('hasClientPrivateKey')

        if m.get('hasClientSecret') is not None:
            self.has_client_secret = m.get('hasClientSecret')

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

        if m.get('ssoStatus') is not None:
            self.sso_status = m.get('ssoStatus')

        if m.get('tokenEndpoint') is not None:
            self.token_endpoint = m.get('tokenEndpoint')

        if m.get('userinfoEndpoint') is not None:
            self.userinfo_endpoint = m.get('userinfoEndpoint')

        return self

class GetIdentityProviderResponseBodyDataOidc(DaraModel):
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
        # The default value is client_secret_post. If the value is none, PKCE must be enabled.
        self.client_auth_method = client_auth_method
        # The client identifier registered in the external IdP, which is different from the Matrix client. In-place replacement is not supported after configuration.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint. It is mutually exclusive with manually entered endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer of the external IdP. In-place replacement is not supported after configuration.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. It must be set to true when no client authentication is used.
        self.pkce_required = pkce_required
        # An array of strings that must contain openid. The default values are openid, profile, and email.
        self.scopes = scopes
        # The claim name in the ID token used to match the SCIM externalId. If omitted during initial creation, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can enter oid. The value must be non-empty and cannot contain whitespace characters. When you query oidc, the saved value is returned. When you query oidcConfiguration, the actual upstream value is returned, which may be empty.
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

class GetIdentityProviderResponseBodyDataMetadata(DaraModel):
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
        # The App ID of the Lark application. This parameter is required when the binding type is Feishu.
        self.app_id = app_id
        # The AppKey of the DingTalk application. This parameter is required when the binding type is DingTalk.
        self.app_key = app_key
        # The SAML Binding URI in the historical metadata snapshot. For CustomSSO updates, use saml.bindingType.
        self.binding = binding
        # The certificate string in the historical metadata snapshot. To edit the configuration, use saml.x509Certificates and do not submit the old metadata.
        self.certificates = certificates
        # The CorpId of the DingTalk enterprise. This parameter is required when the binding type is DingTalk.
        self.corp_id = corp_id
        # This parameter is required when manually filled in. It must be non-empty and contain a maximum of 2,048 characters. Existing configurations do not support replacement. It is different from the Entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # This parameter is required when manually filled in. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
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

class GetIdentityProviderResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. This parameter is required when manually filled in. Queries return short names.
        self.binding_type = binding_type
        # This parameter is required when manually filled in. It must be non-empty and contain a maximum of 2,048 characters. Existing configurations do not support replacement. It is different from the Entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # This parameter is required when manually filled in. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The actual switch value is Enabled or Disabled, which is not equivalent to the expected loginEnabled value saved in AC.
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

