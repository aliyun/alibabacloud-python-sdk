# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The binding information of the external identity provider.
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
            temp_model = main_models.CreateIdentityProviderResponseBodyData()
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

class CreateIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.CreateIdentityProviderResponseBodyDataConfiguration = None,
        identity_provider_type: str = None,
        login_enabled: bool = None,
        oidc: main_models.CreateIdentityProviderResponseBodyDataOidc = None,
        protocol: str = None,
        saml: main_models.CreateIdentityProviderResponseBodyDataSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.CreateIdentityProviderResponseBodyDataSyncScope = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration is read back on demand only in GetIdentityProvider. SCIM queries and preparations return the actual receiving status and URL.
        self.configuration = configuration
        # The type of the external identity provider. Valid values: DingTalk and Feishu.
        self.identity_provider_type = identity_provider_type
        # Specifies whether to allow workspace users to log on through the external identity provider.
        self.login_enabled = login_enabled
        # The security summary of the expected configuration. It does not contain credentials. The original SAML fields and meanings are retained.
        self.oidc = oidc
        # Currently, only SAML is supported. This field may not be returned if no valid configuration is saved. Initialization with an OIDC placeholder is not supported.
        self.protocol = protocol
        # The input supports either XML or full manual entry. Queries return the standardized configuration and do not echo the original XML. This field can be omitted if it is not configured.
        self.saml = saml
        # The binding status. Valid values:
        # - CONFIGURED: configuration accepted and waiting for user pool activation
        # - SYNCING: synchronizing organization members
        # - SYNCED: organization member synchronization completed
        # - READY: binding in effect
        # - SYNC_FAILED: organization member synchronization failed
        # - UPDATING: updating configuration
        # - UPDATE_FAILED: configuration update failed
        # - DISCONNECTING: disconnecting the binding
        # - DISCONNECT_FAILED: disconnection failed
        self.status = status
        # Specifies whether to enable organization member synchronization. When enabled, organization members are synchronized as workspace users by the external identity provider.
        self.sync_enabled = sync_enabled
        # Uses the department-based synchronization scope definition. If omitted during creation, the default value is AllAuthorized, and the initial vendor synchronization is determined by syncOnBind. If omitted or set to null during an update, the original value is retained. Updating and saving the scope does not automatically trigger full synchronization.
        self.sync_scope = sync_scope
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration:
            self.configuration.validate()
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

        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

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

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.CreateIdentityProviderResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('oidc') is not None:
            temp_model = main_models.CreateIdentityProviderResponseBodyDataOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.CreateIdentityProviderResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.CreateIdentityProviderResponseBodyDataSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateIdentityProviderResponseBodyDataSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # When the mode is SelectedDepartments, this parameter must contain at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When the mode is AllAuthorized, pass an empty array or omit this parameter.
        self.department_ids = department_ids
        # Valid values:
        # - AllAuthorized: the entire authorized scope, which is limited by the application address book authorization.
        # - SelectedDepartments: the selected departments and all their sub-departments.
        # When explicitly submitting syncScope, you must provide a valid mode, which is verified by the backend.
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

class CreateIdentityProviderResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain a maximum of 2,048 characters. It cannot be changed after configuration. It is different from the local entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # Required for manual entry. It must be a non-empty array that uses PEM X.509 certificate text. The current validity period is verified. A maximum of two certificates are allowed after deduplication.
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

class CreateIdentityProviderResponseBodyDataOidc(DaraModel):
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
        # The absolute HTTPS URL required in manual entry mode. Do not specify this field in discovery mode.
        self.authorization_endpoint = authorization_endpoint
        # The default value is client_secret_post. If the value is none, PKCE must be enabled.
        self.client_auth_method = client_auth_method
        # The client ID registered in the external IdP, which is different from the Matrix client. It cannot be replaced in place after configuration.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint. It is mutually exclusive with manually entered endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer of the external IdP. It cannot be replaced in place after configuration.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual entry mode. Do not specify this field in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. This parameter must be set to true when client authentication is not used.
        self.pkce_required = pkce_required
        # An array of strings that must include openid. Default values: openid, profile, and email.
        self.scopes = scopes
        # The name of the claim in the ID token that is used to match the SCIM externalId. If omitted during creation, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can specify oid. The value must be non-empty and contain no whitespace characters. When you query oidc, the saved value is returned. When you query oidcConfiguration, the actual upstream value is returned, which may be empty.
        self.sso_mapping_claim = sso_mapping_claim
        # The absolute HTTPS URL required in manual entry mode. Do not specify this field in discovery mode.
        self.token_endpoint = token_endpoint
        # The optional absolute HTTPS URL for manual mode. Leave this field empty in Discovery mode.
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

class CreateIdentityProviderResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain a maximum of 2,048 characters. It cannot be changed after configuration. It is different from the local entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The actual switch value, which is Enabled or Disabled. It is not equivalent to the expected loginEnabled value saved in the access configuration.
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

