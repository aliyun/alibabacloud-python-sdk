# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateIdentityProviderRequestBody = None,
    ):
        # Submit business parameters as described in this operation. The body parameters of public APIs are mapped to backend wrappers by the gateway. Do not mix them with backend direct connection body wrappers.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateIdentityProviderRequestBody(DaraModel):
    def __init__(
        self,
        login_enabled: bool = None,
        metadata: main_models.UpdateIdentityProviderRequestBodyMetadata = None,
        oidc: main_models.UpdateIdentityProviderRequestBodyOidc = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderRequestBodySaml = None,
        sync_enabled: bool = None,
        sync_scope: main_models.UpdateIdentityProviderRequestBodySyncScope = None,
    ):
        # Do not pass true during CustomSSO initialization. A valid SAML configuration must be saved before enabling. Disabling does not delete the configuration. If an asynchronous failure occurs, this expected value does not indicate that it has taken effect upstream.
        self.login_enabled = login_enabled
        # The provider configurations for DingTalk and Feishu support partial updates. Omitted fields retain their saved values. Submitted values must not be null, empty strings, or blank strings. The complete configuration is verified after merging. CustomSSO updates use protocol and saml, and do not accept this field. The returned value does not contain provider keys.
        self.metadata = metadata
        # Accepted only for CustomSSO and mutually exclusive with SAML. Submit the complete public configuration. Omitting credentials retains the existing values, while new values replace them. Blank and masked values are not accepted as credentials.
        self.oidc = oidc
        # The login protocol for CustomSSO. Currently, only SAML is supported. You can pass SAML when saving the SAML configuration. You can omit this parameter if you only modify loginEnabled. DingTalk and Feishu do not accept this field.
        self.protocol = protocol
        # The SAML configuration for CustomSSO. Choose either metadataXml or the four manually entered fields: entityId, loginUrl, bindingType, and x509Certificates. If not submitted, the existing configuration is retained. DingTalk and Feishu do not accept this field.
        self.saml = saml
        # Specifies whether to enable incremental synchronization for subsequent address book change events of DingTalk or Feishu. If not passed, the original value is retained. It does not control the initial synchronization or manual synchronization. CustomSSO does not accept this field. You must use UpdateIdentityProviderSCIM.
        self.sync_enabled = sync_enabled
        # Follows the definition of the department-based synchronization scope. If omitted during creation, the default value is AllAuthorized. The initial provider synchronization is determined by syncOnBind. If omitted or set to null during an update, the original value is retained. Saving the scope during an update does not automatically trigger a full synchronization.
        self.sync_scope = sync_scope

    def validate(self):
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

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.sync_scope is not None:
            result['syncScope'] = self.sync_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('metadata') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodyMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('oidc') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodyOidc()
            self.oidc = temp_model.from_map(m.get('oidc'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodySaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodySyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        return self

class UpdateIdentityProviderRequestBodySyncScope(DaraModel):
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

class UpdateIdentityProviderRequestBodySaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        metadata_xml: str = None,
        x_509certificates: List[str] = None,
    ):
        # HTTP-Redirect or HTTP-POST. Required for manual entry. The query returns the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain up to 2,048 characters. The existing configuration does not support replacement. It is different from the local entity ID returned by the SP query.
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url
        # The XML text of a single IdP EntityDescriptor, with a maximum size of 1 MiB. It must not be a URL or file path. It is mutually exclusive with the four manually entered fields. DTD and external entities are prohibited. If both SSO bindings are declared, HTTP-POST takes precedence.
        self.metadata_xml = metadata_xml
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

        if self.metadata_xml is not None:
            result['metadataXml'] = self.metadata_xml

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

        if m.get('metadataXml') is not None:
            self.metadata_xml = m.get('metadataXml')

        if m.get('x509Certificates') is not None:
            self.x_509certificates = m.get('x509Certificates')

        return self

class UpdateIdentityProviderRequestBodyOidc(DaraModel):
    def __init__(
        self,
        authorization_endpoint: str = None,
        client_auth_method: str = None,
        client_id: str = None,
        client_private_key: str = None,
        client_secret: str = None,
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
        # The private key required for private_key_jwt authentication. If omitted during an update, the original value is retained. The value is not echoed in the response.
        self.client_private_key = client_private_key
        # Required for post or basic authentication. If omitted during an update, the original value is retained. Blank or fully masked values with asterisks are not accepted. The value is not echoed in the response.
        self.client_secret = client_secret
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

        if self.client_private_key is not None:
            result['clientPrivateKey'] = self.client_private_key

        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret

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

        if m.get('clientPrivateKey') is not None:
            self.client_private_key = m.get('clientPrivateKey')

        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')

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

class UpdateIdentityProviderRequestBodyMetadata(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # The Feishu App ID. It can be omitted during an update to retain the saved value. The merged Feishu configuration of the old and new values must contain this item.
        self.app_id = app_id
        # The DingTalk AppKey. It can be omitted during an update to retain the saved value. The merged DingTalk configuration of the old and new values must contain this item.
        self.app_key = app_key
        # The provider application secret. If omitted during an update, the saved value is retained. You can submit this field separately to update the secret. The explicit value must not be empty. This is sensitive input and is not echoed in the response.
        self.app_secret = app_secret
        # The DingTalk enterprise CorpId. It can be omitted during an update to retain the saved value. The merged DingTalk configuration of the old and new values must contain this item.
        self.corp_id = corp_id
        # Required when synchronization is enabled for DingTalk and Feishu. This is sensitive input and is unrelated to the SCIM token.
        self.encrypt_key = encrypt_key
        # Required when synchronization is enabled for DingTalk and Feishu. This is sensitive input and is unrelated to the SCIM token.
        self.verification_token = verification_token

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

        if self.app_secret is not None:
            result['appSecret'] = self.app_secret

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key

        if self.verification_token is not None:
            result['verificationToken'] = self.verification_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('appSecret') is not None:
            self.app_secret = m.get('appSecret')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')

        if m.get('verificationToken') is not None:
            self.verification_token = m.get('verificationToken')

        return self

