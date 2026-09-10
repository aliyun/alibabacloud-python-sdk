# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationSsoConfigResponseBody(DaraModel):
    def __init__(
        self,
        application_sso_config: main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfig = None,
        request_id: str = None,
    ):
        # The single sign-on (SSO) configuration information of the application.
        self.application_sso_config = application_sso_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_sso_config:
            self.application_sso_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_sso_config is not None:
            result['ApplicationSsoConfig'] = self.application_sso_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationSsoConfig') is not None:
            temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfig()
            self.application_sso_config = temp_model.from_map(m.get('ApplicationSsoConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfig(DaraModel):
    def __init__(
        self,
        init_login_type: str = None,
        init_login_url: str = None,
        oidc_sso_config: main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig = None,
        protocol_endpoint_domain: main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain = None,
        saml_sso_config: main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig = None,
        sso_status: str = None,
    ):
        # The initialization single sign-on (SSO) method. Valid values:
        # - only_app_init_sso: Only application-initiated SSO. This is the default value for OIDC protocol applications. When a SAML application specifies this method, InitLoginUrl must be specified.
        # - idaas_or_app_init_sso: IDaaS portal-initiated or application-initiated SSO. This is the default value for SAML protocol applications. When an OIDC application specifies this method, InitLoginUrl must be specified.
        self.init_login_type = init_login_type
        # The initialization single sign-on (SSO) trigger URL. This parameter is required when the InitLoginType of an OIDC protocol application is set to idaas_or_app_init_sso, or when the InitLoginType of a SAML protocol application is set to only_app_init_sso.
        self.init_login_url = init_login_url
        # The SSO configuration parameters for OIDC protocol applications. This parameter is returned only when the application SSO protocol is OIDC.
        self.oidc_sso_config = oidc_sso_config
        # The metadata endpoint configuration provided by the application.
        self.protocol_endpoint_domain = protocol_endpoint_domain
        # The SSO configuration parameters for SAML protocol applications. This parameter is returned only when the application SSO protocol is SAML 2.0.
        self.saml_sso_config = saml_sso_config
        # The SSO status of the application. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.sso_status = sso_status

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.protocol_endpoint_domain:
            self.protocol_endpoint_domain.validate()
        if self.saml_sso_config:
            self.saml_sso_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.init_login_type is not None:
            result['InitLoginType'] = self.init_login_type

        if self.init_login_url is not None:
            result['InitLoginUrl'] = self.init_login_url

        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()

        if self.protocol_endpoint_domain is not None:
            result['ProtocolEndpointDomain'] = self.protocol_endpoint_domain.to_map()

        if self.saml_sso_config is not None:
            result['SamlSsoConfig'] = self.saml_sso_config.to_map()

        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitLoginType') is not None:
            self.init_login_type = m.get('InitLoginType')

        if m.get('InitLoginUrl') is not None:
            self.init_login_url = m.get('InitLoginUrl')

        if m.get('OidcSsoConfig') is not None:
            temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m.get('OidcSsoConfig'))

        if m.get('ProtocolEndpointDomain') is not None:
            temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain()
            self.protocol_endpoint_domain = temp_model.from_map(m.get('ProtocolEndpointDomain'))

        if m.get('SamlSsoConfig') is not None:
            temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig()
            self.saml_sso_config = temp_model.from_map(m.get('SamlSsoConfig'))

        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfig(DaraModel):
    def __init__(
        self,
        assertion_signed: bool = None,
        attribute_statements: List[main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements] = None,
        default_relay_state: str = None,
        id_pentity_id: str = None,
        name_id_format: str = None,
        name_id_value_expression: str = None,
        optional_relay_states: List[main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigOptionalRelayStates] = None,
        require_authn_request_signed: bool = None,
        response_signed: bool = None,
        signature_algorithm: str = None,
        sp_entity_id: str = None,
        sp_signing_certificates: List[str] = None,
        sp_slo_response_url: str = None,
        sp_sso_acs_url: str = None,
    ):
        # Specifies whether the assertion needs to be signed. ResponseSigned and AssertionSigned cannot both be set to false.
        # - true: Signed.
        # - false: Not signed.
        self.assertion_signed = assertion_signed
        # The additional user attribute configuration included in the SAML assertion.
        self.attribute_statements = attribute_statements
        # The default RelayState value. When the single sign-on (SSO) request is initiated by EIAM, the SAML Response provided by EIAM specifies the RelayState as this value. This applies when the user logon request is initiated by EIAM.
        self.default_relay_state = default_relay_state
        # The Entity ID that represents the IdP identity in the SAML protocol.
        self.id_pentity_id = id_pentity_id
        # The NameID format defined by the SAML protocol standard. Valid values:
        # - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified: Unspecified. The application determines how to parse the NameID.
        # - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress: Email address format.
        # - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent: Persistent NameID.
        # - urn:oasis:names:tc:SAML:2.0:nameid-format:transient: Transient NameID.
        self.name_id_format = name_id_format
        # The expression used to generate the actual NameID value in the SAML protocol.
        self.name_id_value_expression = name_id_value_expression
        # The optional RelayState values. In the application portal, the application card displays multiple optional redirect addresses with display names. After a user clicks an address and completes SSO, the user is automatically redirected to the corresponding address. You can specify optional redirect addresses only after you specify a default redirect address.
        self.optional_relay_states = optional_relay_states
        # Indicates whether SSO AuthnRequest signature verification is enabled.
        self.require_authn_request_signed = require_authn_request_signed
        # Indicates whether the Response needs to be signed. ResponseSigned and AssertionSigned cannot both be set to false. Valid values:
        # - true: Signing is required.
        # - false: Signing is not required.
        self.response_signed = response_signed
        # The signature algorithm for the SAML assertion.
        self.signature_algorithm = signature_algorithm
        # The SAML EntityId of the application (SP).
        self.sp_entity_id = sp_entity_id
        # The configured SP signing verification certificates in PEM format. A maximum of two certificates are returned for the console or API caller to read and display.
        self.sp_signing_certificates = sp_signing_certificates
        # The configured SP SLO response URL.
        self.sp_slo_response_url = sp_slo_response_url
        # The SAML Assertion Consumer Service (ACS) URL of the application (SP).
        self.sp_sso_acs_url = sp_sso_acs_url

    def validate(self):
        if self.attribute_statements:
            for v1 in self.attribute_statements:
                 if v1:
                    v1.validate()
        if self.optional_relay_states:
            for v1 in self.optional_relay_states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assertion_signed is not None:
            result['AssertionSigned'] = self.assertion_signed

        result['AttributeStatements'] = []
        if self.attribute_statements is not None:
            for k1 in self.attribute_statements:
                result['AttributeStatements'].append(k1.to_map() if k1 else None)

        if self.default_relay_state is not None:
            result['DefaultRelayState'] = self.default_relay_state

        if self.id_pentity_id is not None:
            result['IdPEntityId'] = self.id_pentity_id

        if self.name_id_format is not None:
            result['NameIdFormat'] = self.name_id_format

        if self.name_id_value_expression is not None:
            result['NameIdValueExpression'] = self.name_id_value_expression

        result['OptionalRelayStates'] = []
        if self.optional_relay_states is not None:
            for k1 in self.optional_relay_states:
                result['OptionalRelayStates'].append(k1.to_map() if k1 else None)

        if self.require_authn_request_signed is not None:
            result['RequireAuthnRequestSigned'] = self.require_authn_request_signed

        if self.response_signed is not None:
            result['ResponseSigned'] = self.response_signed

        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm

        if self.sp_entity_id is not None:
            result['SpEntityId'] = self.sp_entity_id

        if self.sp_signing_certificates is not None:
            result['SpSigningCertificates'] = self.sp_signing_certificates

        if self.sp_slo_response_url is not None:
            result['SpSloResponseUrl'] = self.sp_slo_response_url

        if self.sp_sso_acs_url is not None:
            result['SpSsoAcsUrl'] = self.sp_sso_acs_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssertionSigned') is not None:
            self.assertion_signed = m.get('AssertionSigned')

        self.attribute_statements = []
        if m.get('AttributeStatements') is not None:
            for k1 in m.get('AttributeStatements'):
                temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements()
                self.attribute_statements.append(temp_model.from_map(k1))

        if m.get('DefaultRelayState') is not None:
            self.default_relay_state = m.get('DefaultRelayState')

        if m.get('IdPEntityId') is not None:
            self.id_pentity_id = m.get('IdPEntityId')

        if m.get('NameIdFormat') is not None:
            self.name_id_format = m.get('NameIdFormat')

        if m.get('NameIdValueExpression') is not None:
            self.name_id_value_expression = m.get('NameIdValueExpression')

        self.optional_relay_states = []
        if m.get('OptionalRelayStates') is not None:
            for k1 in m.get('OptionalRelayStates'):
                temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigOptionalRelayStates()
                self.optional_relay_states.append(temp_model.from_map(k1))

        if m.get('RequireAuthnRequestSigned') is not None:
            self.require_authn_request_signed = m.get('RequireAuthnRequestSigned')

        if m.get('ResponseSigned') is not None:
            self.response_signed = m.get('ResponseSigned')

        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')

        if m.get('SpEntityId') is not None:
            self.sp_entity_id = m.get('SpEntityId')

        if m.get('SpSigningCertificates') is not None:
            self.sp_signing_certificates = m.get('SpSigningCertificates')

        if m.get('SpSloResponseUrl') is not None:
            self.sp_slo_response_url = m.get('SpSloResponseUrl')

        if m.get('SpSsoAcsUrl') is not None:
            self.sp_sso_acs_url = m.get('SpSsoAcsUrl')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigOptionalRelayStates(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        relay_state: str = None,
    ):
        # The display name of the RelayState.
        self.display_name = display_name
        # The optional RelayState value. In the application portal, the application card displays multiple optional redirect addresses with display names. After a user clicks an address and completes SSO, the user is automatically redirected to the corresponding address.
        self.relay_state = relay_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.relay_state is not None:
            result['RelayState'] = self.relay_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigSamlSsoConfigAttributeStatements(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value_expression: str = None,
    ):
        # The Name of the attribute in the SAML assertion.
        self.attribute_name = attribute_name
        # The attribute value expression in the SAML assertion.
        self.attribute_value_expression = attribute_value_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_value_expression is not None:
            result['AttributeValueExpression'] = self.attribute_value_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeValueExpression') is not None:
            self.attribute_value_expression = m.get('AttributeValueExpression')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigProtocolEndpointDomain(DaraModel):
    def __init__(
        self,
        oauth_2authorization_endpoint: str = None,
        oauth_2device_authorization_endpoint: str = None,
        oauth_2revoke_endpoint: str = None,
        oauth_2token_endpoint: str = None,
        oauth_2userinfo_endpoint: str = None,
        oidc_issuer: str = None,
        oidc_jwks_endpoint: str = None,
        oidc_logout_endpoint: str = None,
        saml_meta_endpoint: str = None,
        saml_slo_endpoint: str = None,
        saml_sso_endpoint: str = None,
    ):
        # The OAuth 2.0 authorization endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oauth_2authorization_endpoint = oauth_2authorization_endpoint
        # The OAuth 2.0 device authorization endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oauth_2device_authorization_endpoint = oauth_2device_authorization_endpoint
        # The OAuth 2.0 token revocation endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oauth_2revoke_endpoint = oauth_2revoke_endpoint
        # The OAuth 2.0 token endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oauth_2token_endpoint = oauth_2token_endpoint
        # The OIDC user information endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oauth_2userinfo_endpoint = oauth_2userinfo_endpoint
        # The OIDC issuer information. This parameter is returned only when the application SSO protocol is OIDC.
        self.oidc_issuer = oidc_issuer
        # The OIDC JWKS endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oidc_jwks_endpoint = oidc_jwks_endpoint
        # The OIDC RP-initiated logout endpoint. This parameter is returned only when the application SSO protocol is OIDC.
        self.oidc_logout_endpoint = oidc_logout_endpoint
        # The SAML protocol metadata endpoint URL. This parameter is returned only when the application SSO protocol is SAML 2.0.
        self.saml_meta_endpoint = saml_meta_endpoint
        # The SAML single logout URL (SLO URL) on the IdP side. The SP redirects the user to this URL to initiate single logout.
        self.saml_slo_endpoint = saml_slo_endpoint
        # The SAML protocol AuthnRequest receiving endpoint. This parameter is returned only when the application SSO protocol is SAML 2.0.
        self.saml_sso_endpoint = saml_sso_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oauth_2authorization_endpoint is not None:
            result['Oauth2AuthorizationEndpoint'] = self.oauth_2authorization_endpoint

        if self.oauth_2device_authorization_endpoint is not None:
            result['Oauth2DeviceAuthorizationEndpoint'] = self.oauth_2device_authorization_endpoint

        if self.oauth_2revoke_endpoint is not None:
            result['Oauth2RevokeEndpoint'] = self.oauth_2revoke_endpoint

        if self.oauth_2token_endpoint is not None:
            result['Oauth2TokenEndpoint'] = self.oauth_2token_endpoint

        if self.oauth_2userinfo_endpoint is not None:
            result['Oauth2UserinfoEndpoint'] = self.oauth_2userinfo_endpoint

        if self.oidc_issuer is not None:
            result['OidcIssuer'] = self.oidc_issuer

        if self.oidc_jwks_endpoint is not None:
            result['OidcJwksEndpoint'] = self.oidc_jwks_endpoint

        if self.oidc_logout_endpoint is not None:
            result['OidcLogoutEndpoint'] = self.oidc_logout_endpoint

        if self.saml_meta_endpoint is not None:
            result['SamlMetaEndpoint'] = self.saml_meta_endpoint

        if self.saml_slo_endpoint is not None:
            result['SamlSloEndpoint'] = self.saml_slo_endpoint

        if self.saml_sso_endpoint is not None:
            result['SamlSsoEndpoint'] = self.saml_sso_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oauth2AuthorizationEndpoint') is not None:
            self.oauth_2authorization_endpoint = m.get('Oauth2AuthorizationEndpoint')

        if m.get('Oauth2DeviceAuthorizationEndpoint') is not None:
            self.oauth_2device_authorization_endpoint = m.get('Oauth2DeviceAuthorizationEndpoint')

        if m.get('Oauth2RevokeEndpoint') is not None:
            self.oauth_2revoke_endpoint = m.get('Oauth2RevokeEndpoint')

        if m.get('Oauth2TokenEndpoint') is not None:
            self.oauth_2token_endpoint = m.get('Oauth2TokenEndpoint')

        if m.get('Oauth2UserinfoEndpoint') is not None:
            self.oauth_2userinfo_endpoint = m.get('Oauth2UserinfoEndpoint')

        if m.get('OidcIssuer') is not None:
            self.oidc_issuer = m.get('OidcIssuer')

        if m.get('OidcJwksEndpoint') is not None:
            self.oidc_jwks_endpoint = m.get('OidcJwksEndpoint')

        if m.get('OidcLogoutEndpoint') is not None:
            self.oidc_logout_endpoint = m.get('OidcLogoutEndpoint')

        if m.get('SamlMetaEndpoint') is not None:
            self.saml_meta_endpoint = m.get('SamlMetaEndpoint')

        if m.get('SamlSloEndpoint') is not None:
            self.saml_slo_endpoint = m.get('SamlSloEndpoint')

        if m.get('SamlSsoEndpoint') is not None:
            self.saml_sso_endpoint = m.get('SamlSsoEndpoint')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfig(DaraModel):
    def __init__(
        self,
        access_token_effective_time: int = None,
        allowed_public_client: str = None,
        code_effective_time: int = None,
        custom_claims: List[main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims] = None,
        grant_scopes: List[str] = None,
        grant_types: List[str] = None,
        id_token_effective_time: int = None,
        password_authentication_source_id: str = None,
        password_totp_mfa_required: bool = None,
        pkce_challenge_methods: List[str] = None,
        pkce_required: bool = None,
        post_logout_redirect_uris: List[str] = None,
        redirect_uris: List[str] = None,
        refresh_token_effective: int = None,
        response_types: List[str] = None,
        subject_id_expression: str = None,
    ):
        # The validity period of the issued access token. Unit: seconds. Default value: 1200 (20 minutes).
        self.access_token_effective_time = access_token_effective_time
        # Specifies whether the application is allowed to request the IDaaS EIAM authorization server as a public client. This parameter can be enabled only in authorization code mode and device mode. Default value: false.
        self.allowed_public_client = allowed_public_client
        # The validity period of the issued code. Unit: seconds. Default value: 60 (1 minute).
        self.code_effective_time = code_effective_time
        # The custom user information included in the ID token response.
        self.custom_claims = custom_claims
        # The OIDC standard parameter scope, which specifies the range of user attributes that can be returned by the userinfo endpoint or ID token.
        self.grant_scopes = grant_scopes
        # The list of supported OIDC protocol grant types.
        self.grant_types = grant_types
        # The validity period of the issued ID token. Unit: seconds. Default value: 300 (5 minutes).
        self.id_token_effective_time = id_token_effective_time
        # The ID of the identity authentication source used in password mode. This parameter takes effect only when the GrantTypes specified for the OIDC protocol application include the password mode.
        self.password_authentication_source_id = password_authentication_source_id
        # Specifies whether TOTP-based secondary authentication is required in password mode. This parameter takes effect only when the GrantTypes specified for the OIDC protocol application include the password mode.
        self.password_totp_mfa_required = password_totp_mfa_required
        # The algorithm used to calculate the Code Challenge in PKCE.
        self.pkce_challenge_methods = pkce_challenge_methods
        # Specifies whether the application SSO requires PKCE (RFC 7636).
        self.pkce_required = pkce_required
        # The list of logout callback addresses supported by the application.
        self.post_logout_redirect_uris = post_logout_redirect_uris
        # The list of redirect URIs supported by the application.
        self.redirect_uris = redirect_uris
        # The validity period of the issued refresh token. Unit: seconds. Default value: 86400 (1 day).
        self.refresh_token_effective = refresh_token_effective
        # The response types supported by the application when OidcSsoConfig.GrantTypes includes the implicit mode.
        self.response_types = response_types
        # The custom expression for the sub value returned in the ID token.
        self.subject_id_expression = subject_id_expression

    def validate(self):
        if self.custom_claims:
            for v1 in self.custom_claims:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token_effective_time is not None:
            result['AccessTokenEffectiveTime'] = self.access_token_effective_time

        if self.allowed_public_client is not None:
            result['AllowedPublicClient'] = self.allowed_public_client

        if self.code_effective_time is not None:
            result['CodeEffectiveTime'] = self.code_effective_time

        result['CustomClaims'] = []
        if self.custom_claims is not None:
            for k1 in self.custom_claims:
                result['CustomClaims'].append(k1.to_map() if k1 else None)

        if self.grant_scopes is not None:
            result['GrantScopes'] = self.grant_scopes

        if self.grant_types is not None:
            result['GrantTypes'] = self.grant_types

        if self.id_token_effective_time is not None:
            result['IdTokenEffectiveTime'] = self.id_token_effective_time

        if self.password_authentication_source_id is not None:
            result['PasswordAuthenticationSourceId'] = self.password_authentication_source_id

        if self.password_totp_mfa_required is not None:
            result['PasswordTotpMfaRequired'] = self.password_totp_mfa_required

        if self.pkce_challenge_methods is not None:
            result['PkceChallengeMethods'] = self.pkce_challenge_methods

        if self.pkce_required is not None:
            result['PkceRequired'] = self.pkce_required

        if self.post_logout_redirect_uris is not None:
            result['PostLogoutRedirectUris'] = self.post_logout_redirect_uris

        if self.redirect_uris is not None:
            result['RedirectUris'] = self.redirect_uris

        if self.refresh_token_effective is not None:
            result['RefreshTokenEffective'] = self.refresh_token_effective

        if self.response_types is not None:
            result['ResponseTypes'] = self.response_types

        if self.subject_id_expression is not None:
            result['SubjectIdExpression'] = self.subject_id_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTokenEffectiveTime') is not None:
            self.access_token_effective_time = m.get('AccessTokenEffectiveTime')

        if m.get('AllowedPublicClient') is not None:
            self.allowed_public_client = m.get('AllowedPublicClient')

        if m.get('CodeEffectiveTime') is not None:
            self.code_effective_time = m.get('CodeEffectiveTime')

        self.custom_claims = []
        if m.get('CustomClaims') is not None:
            for k1 in m.get('CustomClaims'):
                temp_model = main_models.GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims()
                self.custom_claims.append(temp_model.from_map(k1))

        if m.get('GrantScopes') is not None:
            self.grant_scopes = m.get('GrantScopes')

        if m.get('GrantTypes') is not None:
            self.grant_types = m.get('GrantTypes')

        if m.get('IdTokenEffectiveTime') is not None:
            self.id_token_effective_time = m.get('IdTokenEffectiveTime')

        if m.get('PasswordAuthenticationSourceId') is not None:
            self.password_authentication_source_id = m.get('PasswordAuthenticationSourceId')

        if m.get('PasswordTotpMfaRequired') is not None:
            self.password_totp_mfa_required = m.get('PasswordTotpMfaRequired')

        if m.get('PkceChallengeMethods') is not None:
            self.pkce_challenge_methods = m.get('PkceChallengeMethods')

        if m.get('PkceRequired') is not None:
            self.pkce_required = m.get('PkceRequired')

        if m.get('PostLogoutRedirectUris') is not None:
            self.post_logout_redirect_uris = m.get('PostLogoutRedirectUris')

        if m.get('RedirectUris') is not None:
            self.redirect_uris = m.get('RedirectUris')

        if m.get('RefreshTokenEffective') is not None:
            self.refresh_token_effective = m.get('RefreshTokenEffective')

        if m.get('ResponseTypes') is not None:
            self.response_types = m.get('ResponseTypes')

        if m.get('SubjectIdExpression') is not None:
            self.subject_id_expression = m.get('SubjectIdExpression')

        return self

class GetApplicationSsoConfigResponseBodyApplicationSsoConfigOidcSsoConfigCustomClaims(DaraModel):
    def __init__(
        self,
        claim_name: str = None,
        claim_value_expression: str = None,
    ):
        # The name of the returned claim.
        self.claim_name = claim_name
        # The value expression of the returned claim.
        self.claim_value_expression = claim_value_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claim_name is not None:
            result['ClaimName'] = self.claim_name

        if self.claim_value_expression is not None:
            result['ClaimValueExpression'] = self.claim_value_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimName') is not None:
            self.claim_name = m.get('ClaimName')

        if m.get('ClaimValueExpression') is not None:
            self.claim_value_expression = m.get('ClaimValueExpression')

        return self

