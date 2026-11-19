# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderSCIMResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIdentityProviderSCIMResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code. If the request fails, use this code in combination with the HTTP status code and the result message for troubleshooting.
        self.code = code
        # The data object. Retains the original fields and the meaning of the status field. The new scimStatus field corresponds to the data.status field in the query API operation, and the operationStatus field retains the status of the most recent SCIM task.
        self.data = data
        # The HTTP status code. Indicates the processing status of the current request, which does not necessarily reflect the final result of the background task.
        self.http_status_code = http_status_code
        # The result message. Indicates whether the request is accepted or returns an error message. For an asynchronous task, check the task result by calling the corresponding query API operation.
        self.message = message
        # The request ID. Retain this ID to correlate the current call and troubleshoot failures.
        self.request_id = request_id
        # Indicates whether the current request is successful. A value of true indicates that the request is processed successfully. For asynchronous write operations, you must continue to query the task result.
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
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyData()
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

class UpdateIdentityProviderSCIMResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateIdentityProviderSCIMResponseBodyDataConfiguration = None,
        created_at: str = None,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        metadata: main_models.UpdateIdentityProviderSCIMResponseBodyDataMetadata = None,
        oidc: main_models.UpdateIdentityProviderSCIMResponseBodyDataOidc = None,
        operation_status: str = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderSCIMResponseBodyDataSaml = None,
        scim_status: str = None,
        status: str = None,
        sync_enabled: bool = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The actual upstream configuration. The actual SAML configuration is read back on demand only by the GetIdentityProvider API operation. The SCIM query and preparation operations return the actual receiving status and URL.
        self.configuration = configuration
        # The time when the record was created on the server.
        self.created_at = created_at
        # The SAML vendor event callback URL. For CustomSSO, an empty string is returned. To obtain the SCIM receiving URL, call the SCIM query or preparation API operation. The example shows a JSON empty string "", but the actual value does not include double quotation marks.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The identity provider type. General CRUD operations support DingTalk, Feishu, and CustomSSO. SP queries support only CustomSSO. The SCIM path uses the CustomSSO shared pool.
        self.identity_provider_type = identity_provider_type
        # The SAML vendor callback URL. For CustomSSO, an empty string is returned. To obtain the Assertion Consumer Service (ACS) URL for SAML, call the SP query API operation. The example shows a JSON empty string "", but the actual value does not include double quotation marks.
        self.login_callback_url = login_callback_url
        # Specifies whether logon is enabled. Do not set this parameter to true during CustomSSO initialization. You must save a valid SAML configuration before enabling logon. Disabling logon does not delete the configuration. If an asynchronous task fails, this expected value does not indicate that the change has taken effect on the upstream server.
        self.login_enabled = login_enabled
        # The standard identity provider (IdP) metadata. Vendor parameters are used for DingTalk and Feishu. To update CustomSSO, use the protocol and saml fields. This field is not accepted for CustomSSO updates. The return value does not include vendor keys.
        self.metadata = metadata
        # The security summary of the expected OIDC configuration. This summary does not include credentials. The original SAML fields and their meanings are retained.
        self.oidc = oidc
        # The original status of the most recent independent SCIM operation task. If no historical tasks exist, an empty string ("") is returned.
        self.operation_status = operation_status
        # The logon protocol. Only SAML is supported. This field may not be returned if no valid configuration is saved. You cannot use OIDC as a placeholder for initialization.
        self.protocol = protocol
        # The SAML logon configuration. You can provide the input by using XML or by manually entering all fields. The query returns the standardized configuration and does not echo the original XML. This field can be omitted if it is not configured.
        self.saml = saml
        # The independent SCIM status. This field does not change the meaning of the original status field for shared resources and logon configurations. It corresponds to the data.status field in the query API operation.
        self.scim_status = scim_status
        # The operation status of the CustomSSO user pool lifecycle and logon configuration tasks. This status does not indicate the result of SCIM operations. To query the result of the SCIM switch, use the GetIdentityProviderSCIM.operationStatus field. You cannot use this field to determine whether all protocols are configured.
        self.status = status
        # Specifies whether to enable SCIM synchronization. Do not set this parameter to true during CustomSSO initialization. You can only update this parameter later by calling UpdateIdentityProviderSCIM. Determine the result based on the operationStatus field.
        self.sync_enabled = sync_enabled
        # The time when the record was last updated on the server.
        self.updated_at = updated_at
        # Required. The ID of the destination workspace. The region of the request must be the same as the region of the destination workspace.
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

        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.scim_status is not None:
            result['scimStatus'] = self.scim_status

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
        if m.get('configuration') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataConfiguration()
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
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('oidc') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('scimStatus') is not None:
            self.scim_status = m.get('scimStatus')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateIdentityProviderSCIMResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. This field is required when you manually enter the configuration. The query returns the short name.
        self.binding_type = binding_type
        # The IdP entity ID. This field is required when you manually enter the metadata. It must be a non-empty string of up to 2,048 characters. You cannot change the entity ID after it is configured. This ID is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # The IdP SSO logon URL. This field is required when you manually enter the metadata. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The list of IdP signing certificates. When you manually enter the configuration, this field is required and must be a non-empty array of PEM X.509 certificate texts. The system verifies the current validity period. A maximum of two certificates are retained after deduplication.
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

class UpdateIdentityProviderSCIMResponseBodyDataOidc(DaraModel):
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
        # The authorization endpoint. This field is required in manual mode and must be an absolute HTTPS URL. Do not specify this field in discovery mode.
        self.authorization_endpoint = authorization_endpoint
        # The client authentication method. Default value: client_secret_post. If the value is none, Proof Key for Code Exchange (PKCE) must be enabled.
        self.client_auth_method = client_auth_method
        # The client ID registered in the external IdP. This ID is different from the Matrix client ID. You cannot change the client ID in place after it is configured.
        self.client_id = client_id
        # The absolute HTTPS OIDC discovery endpoint. This field is mutually exclusive with manually entered endpoints.
        self.discovery_endpoint = discovery_endpoint
        # The absolute HTTPS issuer of the external IdP. You cannot change the issuer in place after it is configured.
        self.issuer = issuer
        # The authorization endpoint. This field is required in manual mode and must be an absolute HTTPS URL. Do not specify this field in discovery mode.
        self.jwks_uri = jwks_uri
        # Specifies whether PKCE is enabled. Default value: true. This parameter must be set to true when no client authentication is used.
        self.pkce_required = pkce_required
        # The array of strings that must contain openid. Default values: openid, profile, and email.
        self.scopes = scopes
        # The name of the claim in the ID token that is used to match the SCIM externalId. If omitted during creation, the default value sub is used. If omitted during an update, the saved value is retained. For Azure, you can specify oid. The value must be non-empty and cannot contain whitespace characters. When querying oidc, the saved value is returned. When querying oidcConfiguration, the actual upstream value is returned, which may be empty.
        self.sso_mapping_claim = sso_mapping_claim
        # The authorization endpoint. This field is required in manual mode and must be an absolute HTTPS URL. Do not specify this field in discovery mode.
        self.token_endpoint = token_endpoint
        # The optional absolute HTTPS URL for manual mode. Leave this field empty in discovery mode.
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

class UpdateIdentityProviderSCIMResponseBodyDataMetadata(DaraModel):
    def __init__(
        self,
        binding: str = None,
        certificates: str = None,
        entity_id: str = None,
        login_url: str = None,
    ):
        # The SAML binding URI in the historical metadata snapshot. To update CustomSSO, use the saml.bindingType field.
        self.binding = binding
        # The certificate string in the historical metadata snapshot. To edit the configuration, use the saml.x509Certificates field instead of submitting the old metadata.
        self.certificates = certificates
        # The IdP entity ID. This field is required when you manually enter the metadata. It must be a non-empty string of up to 2,048 characters. You cannot change the entity ID after it is configured. This ID is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # The IdP SSO logon URL. This field is required when you manually enter the metadata. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding is not None:
            result['binding'] = self.binding

        if self.certificates is not None:
            result['certificates'] = self.certificates

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('binding') is not None:
            self.binding = m.get('binding')

        if m.get('certificates') is not None:
            self.certificates = m.get('certificates')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        return self

class UpdateIdentityProviderSCIMResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. This field is required when you manually enter the configuration. The query returns the short name.
        self.binding_type = binding_type
        # The IdP entity ID. This field is required when you manually enter the metadata. It must be a non-empty string of up to 2,048 characters. You cannot change the entity ID after it is configured. This ID is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # The IdP SSO logon URL. This field is required when you manually enter the metadata. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The actual SSO logon status of AgentIdentity. The actual switch value is Enabled or Disabled, which is not equivalent to the expected value of loginEnabled saved in the access configuration.
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

