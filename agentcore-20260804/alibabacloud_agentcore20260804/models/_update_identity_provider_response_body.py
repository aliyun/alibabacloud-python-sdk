# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code. If the request fails, use this code along with the HTTP status code and message for troubleshooting.
        self.code = code
        # The business result. For the result structure, refer to the response fields of this operation. For asynchronous write operations, the response indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The processing status of the current request. This does not indicate the final result of the background task.
        self.http_status_code = http_status_code
        # The request acceptance or error message. For asynchronous tasks, verify the task result by calling the corresponding query operation.
        self.message = message
        # The request ID. Retain this ID to correlate the current call and troubleshoot failures.
        self.request_id = request_id
        # Indicates whether the current request is processed successfully. A value of true indicates success. For asynchronous write operations, you must still query the task result.
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
            temp_model = main_models.UpdateIdentityProviderResponseBodyData()
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

class UpdateIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateIdentityProviderResponseBodyDataConfiguration = None,
        identity_provider_type: str = None,
        login_enabled: bool = None,
        oidc: main_models.UpdateIdentityProviderResponseBodyDataOidc = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderResponseBodyDataSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.UpdateIdentityProviderResponseBodyDataSyncScope = None,
        workspace_id: str = None,
    ):
        # The actual upstream configuration. The actual SAML configuration is read on demand only in GetIdentityProvider. SCIM queries and preparations return the actual reception status and URL.
        self.configuration = configuration
        # General CRUD operations support DingTalk, Feishu, and CustomSSO. SP queries support only CustomSSO. The SCIM path uses the CustomSSO shared pool.
        self.identity_provider_type = identity_provider_type
        # Do not pass true during CustomSSO initialization. A valid SAML configuration must be saved before enabling. Disabling does not delete the configuration. If an asynchronous failure occurs, this expected value does not indicate that it has taken effect upstream.
        self.login_enabled = login_enabled
        # The expected security summary of the configuration. This does not include credentials. The original SAML fields and meanings are retained.
        self.oidc = oidc
        # The login protocol for CustomSSO. Currently, only SAML is supported. You can pass SAML when saving the SAML configuration. You can omit this parameter if you only modify loginEnabled. DingTalk and Feishu do not accept this field.
        self.protocol = protocol
        # The SAML configuration for CustomSSO. Choose either metadataXml or the four manually entered fields: entityId, loginUrl, bindingType, and x509Certificates. If not submitted, the existing configuration is retained. DingTalk and Feishu do not accept this field.
        self.saml = saml
        # The status of the identity source resource and logon configuration. A READY status in the CustomSSO shared pool does not mean that SAML is configured. Query operationStatus independently for SCIM operation results.
        self.status = status
        # Specifies whether synchronization is enabled. Do not set this parameter to true during CustomSSO initialization. You can only update this parameter later by calling UpdateIdentityProviderSCIM. Evaluate the result in combination with operationStatus.
        self.sync_enabled = sync_enabled
        # Follows the definition of the department-based synchronization scope. If omitted during creation, the default value is AllAuthorized. The initial provider synchronization is determined by syncOnBind. If omitted or set to null during an update, the original value is retained. Saving the scope during an update does not automatically trigger a full synchronization.
        self.sync_scope = sync_scope
        # Required. The ID of the destination workspace. The region of the request must be the same as the region of the destination workspace.
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
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('oidc') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateIdentityProviderResponseBodyDataSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # When set to SelectedDepartments, it must contain at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When set to AllAuthorized, pass an empty array or omit this parameter.
        self.department_ids = department_ids
        # AllAuthorized: the full authorization scope, subject to the application address book authorization limits. SelectedDepartments: the selected departments and all their sub-departments. When explicitly submitting syncScope, a valid mode must be provided and verified by the backend.
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

class UpdateIdentityProviderResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. The query returns the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain up to 2,048 characters. The existing configuration does not support replacement. It is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url
        # Required for manual entry. It must be a non-empty array using PEM X.509 certificate text. The current validity period is verified. Up to two certificates are allowed after deduplication.
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

class UpdateIdentityProviderResponseBodyDataOidc(DaraModel):
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
        # The client identifier registered in the external IdP, which is different from the Matrix client. This value cannot be changed in place after it is configured.
        self.client_id = client_id
        # The absolute HTTPS discovery endpoint URL. This parameter is mutually exclusive with manually specified endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer URL of the external IdP. This value cannot be changed in place after it is configured.
        self.issuer = issuer
        # The absolute HTTPS URL required in manual mode. Do not specify this parameter in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. This parameter must be set to true when no client authentication is used.
        self.pkce_required = pkce_required
        # The array of scope strings. It must include openid. Default values: openid, profile, and email.
        self.scopes = scopes
        # The name of the claim in the ID token used to match the SCIM externalId. If omitted during the initial configuration, the default value is sub. If omitted during an update, the saved value is retained. For Azure, you can specify oid. The value must be non-empty and cannot contain whitespace characters. When queried, oidc returns the saved value, while oidcConfiguration returns the actual upstream value, which may be empty.
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

class UpdateIdentityProviderResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. The query returns the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain up to 2,048 characters. The existing configuration does not support replacement. It is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url
        # The actual switch value, which is Enabled or Disabled. This is not equivalent to the expected loginEnabled value saved in AC.
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

