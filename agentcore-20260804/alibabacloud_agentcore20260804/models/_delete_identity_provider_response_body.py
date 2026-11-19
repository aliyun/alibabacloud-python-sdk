# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

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
        # The external identity provider binding information after the unbind operation is accepted.
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
        configuration: main_models.DeleteIdentityProviderResponseBodyDataConfiguration = None,
        identity_provider_type: str = None,
        oidc: main_models.DeleteIdentityProviderResponseBodyDataOidc = None,
        protocol: str = None,
        saml: main_models.DeleteIdentityProviderResponseBodyDataSaml = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration is read back on demand only in GetIdentityProvider. SCIM queries and preparations return the actual receiving status and URL.
        self.configuration = configuration
        # The type of the external identity provider. Valid values: DingTalk and Feishu.
        self.identity_provider_type = identity_provider_type
        # The security summary of the expected configuration. It does not contain credentials. The original SAML fields and meanings are retained.
        self.oidc = oidc
        # Currently, only SAML is supported. This field is not returned when no valid configuration is saved. Initialization with an OIDC placeholder is not supported.
        self.protocol = protocol
        # The input supports either XML or complete manual entry. Queries return the standardized configuration and do not echo the original XML. This field can be omitted when not configured.
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
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.oidc:
            self.oidc.validate()
        if self.saml:
            self.saml.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.oidc is not None:
            result['oidc'] = self.oidc.to_map()

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.DeleteIdentityProviderResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('oidc') is not None:
            temp_model = main_models.DeleteIdentityProviderResponseBodyDataOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.DeleteIdentityProviderResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class DeleteIdentityProviderResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain a maximum of 2,048 characters. Existing configurations cannot be replaced. This is different from the local entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # Required for manual entry as a non-empty array. Use PEM X.509 certificate text. The current validity period is verified. A maximum of two certificates are allowed after deduplication.
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

class DeleteIdentityProviderResponseBodyDataOidc(DaraModel):
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
        # The absolute HTTPS URL required in manual entry mode. Do not enter this in discovery mode.
        self.authorization_endpoint = authorization_endpoint
        # The default value is client_secret_post. If none is selected, PKCE must be enabled.
        self.client_auth_method = client_auth_method
        # The client ID registered in the external IdP, which is different from the Matrix client. In-place replacement is not supported after configuration.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint. It is mutually exclusive with manually entered endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer of the external IdP. In-place replacement is not supported after configuration.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual entry mode. Do not enter this in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. It must be true when client authentication is not used.
        self.pkce_required = pkce_required
        # The string array. It must contain openid. The default values are openid, profile, and email.
        self.scopes = scopes
        # The claim name in the ID token used to match the SCIM externalId. If omitted during the first creation, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can enter oid. It must be non-empty and contain no whitespace characters. When queried, oidc returns the saved value, and oidcConfiguration returns the actual upstream value, which may be empty.
        self.sso_mapping_claim = sso_mapping_claim
        # The absolute HTTPS URL required in manual entry mode. Do not enter this in discovery mode.
        self.token_endpoint = token_endpoint
        # The optional absolute HTTPS URL in manual entry mode. Do not enter this in discovery mode.
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

class DeleteIdentityProviderResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. Queries return the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain a maximum of 2,048 characters. Existing configurations cannot be replaced. This is different from the local entity ID queried by the service provider (SP).
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The actual switch value is Enabled or Disabled, which differs from the expected loginEnabled value saved in the AC.
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

