# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetApplicationSsoConfigRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        init_login_type: str = None,
        init_login_url: str = None,
        instance_id: str = None,
        oidc_sso_config: main_models.SetApplicationSsoConfigRequestOidcSsoConfig = None,
        saml_sso_config: main_models.SetApplicationSsoConfigRequestSamlSsoConfig = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Idp client token.
        self.client_token = client_token
        # The initial SSO method. Valid values:
        # 
        # *   only_app_init_sso: Only application-initiated SSO is allowed. This method is selected by default when the SSO protocol of the application is an OIDC protocol. If this method is selected when the SSO protocol of the application is SAML, the InitLoginUrl parameter is required.
        # *   idaas_or_app_init_sso: IDaaS-initiated SSO and application-initiated SSO are allowed. This method is selected by default when the SSO protocol of the application is SAML. If this method is selected when the SSO protocol of the application is an OIDC protocol, the InitLoginUrl parameter is required.
        self.init_login_type = init_login_type
        # The initial webhook URL of SSO. This parameter is required when the SSO protocol of the application is an OIDC protocol and the InitLoginType parameters is set to idaas_or_app_init_sso or when the SSO protocol of the application is SAML and the InitLoginType parameter is set to only_app_init_sso.
        self.init_login_url = init_login_url
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The Open ID Connect (OIDC)-based SSO configuration attributes of the application.
        self.oidc_sso_config = oidc_sso_config
        # The Security Assertion Markup Language (SAML)-based SSO configuration attributes of the application.
        self.saml_sso_config = saml_sso_config

    def validate(self):
        if self.oidc_sso_config:
            self.oidc_sso_config.validate()
        if self.saml_sso_config:
            self.saml_sso_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.init_login_type is not None:
            result['InitLoginType'] = self.init_login_type

        if self.init_login_url is not None:
            result['InitLoginUrl'] = self.init_login_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.oidc_sso_config is not None:
            result['OidcSsoConfig'] = self.oidc_sso_config.to_map()

        if self.saml_sso_config is not None:
            result['SamlSsoConfig'] = self.saml_sso_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InitLoginType') is not None:
            self.init_login_type = m.get('InitLoginType')

        if m.get('InitLoginUrl') is not None:
            self.init_login_url = m.get('InitLoginUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OidcSsoConfig') is not None:
            temp_model = main_models.SetApplicationSsoConfigRequestOidcSsoConfig()
            self.oidc_sso_config = temp_model.from_map(m.get('OidcSsoConfig'))

        if m.get('SamlSsoConfig') is not None:
            temp_model = main_models.SetApplicationSsoConfigRequestSamlSsoConfig()
            self.saml_sso_config = temp_model.from_map(m.get('SamlSsoConfig'))

        return self

class SetApplicationSsoConfigRequestSamlSsoConfig(DaraModel):
    def __init__(
        self,
        assertion_signed: bool = None,
        attribute_statements: List[main_models.SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements] = None,
        default_relay_state: str = None,
        id_pentity_id: str = None,
        name_id_format: str = None,
        name_id_value_expression: str = None,
        optional_relay_states: List[main_models.SetApplicationSsoConfigRequestSamlSsoConfigOptionalRelayStates] = None,
        response_signed: bool = None,
        signature_algorithm: str = None,
        sp_entity_id: str = None,
        sp_sso_acs_url: str = None,
    ):
        # Specifies whether to calculate the signature for the assertion. You cannot set the ResponseSigned and AssertionSigned parameters to false at the same time. Valid values:
        # 
        # *   true
        # *   false
        self.assertion_signed = assertion_signed
        # The additional user attributes in the SAML assertion.
        self.attribute_statements = attribute_statements
        # The default value of the RelayState attribute. If the SSO request is initiated in EIAM, the RelayState attribute in the SAML response is set to this default value.
        self.default_relay_state = default_relay_state
        # IdP entityId.
        self.id_pentity_id = id_pentity_id
        # The format of the NameID element in the SAML assertion. Valid values:
        # 
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified: No format is specified. How to resolve the NameID element depends on the application.
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress: The NameID element must be an email address.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:persistent: The NameID element must be persistent.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:transient: The NameID element must be transient.
        # 
        # Valid values:
        # 
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified: No format is specified. This is the default value.
        # *   urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress: The NameID element must be an email address.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:persistent: The NameID element must be persistent.
        # *   urn:oasis:names:tc:SAML:2.0:nameid-format:transient: The NameID element must be transient.
        self.name_id_format = name_id_format
        # The expression that is used to generate the value of NameID in the SAML assertion.
        self.name_id_value_expression = name_id_value_expression
        # Optional relayStates
        self.optional_relay_states = optional_relay_states
        # Specifies whether to calculate the signature for the response. You cannot set the ResponseSigned and AssertionSigned parameters to false at the same time. Valid values:
        # 
        # *   true
        # *   false
        self.response_signed = response_signed
        # The algorithm that is used to calculate the signature for the SAML assertion.
        # 
        # Valid value:
        # 
        # *   RSA-SHA256: the Rivest-Shamir-Adleman (RSA)-Secure Hash Algorithm 256 (SHA-256) algorithm.
        self.signature_algorithm = signature_algorithm
        # The entity ID of the application in SAML.
        self.sp_entity_id = sp_entity_id
        # The Assertion Consumer Service (ACS) URL of the application in SAML.
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

        if self.response_signed is not None:
            result['ResponseSigned'] = self.response_signed

        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm

        if self.sp_entity_id is not None:
            result['SpEntityId'] = self.sp_entity_id

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
                temp_model = main_models.SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements()
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
                temp_model = main_models.SetApplicationSsoConfigRequestSamlSsoConfigOptionalRelayStates()
                self.optional_relay_states.append(temp_model.from_map(k1))

        if m.get('ResponseSigned') is not None:
            self.response_signed = m.get('ResponseSigned')

        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')

        if m.get('SpEntityId') is not None:
            self.sp_entity_id = m.get('SpEntityId')

        if m.get('SpSsoAcsUrl') is not None:
            self.sp_sso_acs_url = m.get('SpSsoAcsUrl')

        return self

class SetApplicationSsoConfigRequestSamlSsoConfigOptionalRelayStates(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        relay_state: str = None,
    ):
        # RelayState displayName
        self.display_name = display_name
        # RelayState value
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

class SetApplicationSsoConfigRequestSamlSsoConfigAttributeStatements(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value_expression: str = None,
    ):
        # The name of the attribute in the SAML assertion.
        self.attribute_name = attribute_name
        # The expression that is used to generate the value of the attribute in the SAML assertion.
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

class SetApplicationSsoConfigRequestOidcSsoConfig(DaraModel):
    def __init__(
        self,
        access_token_effective_time: int = None,
        allowed_public_client: bool = None,
        code_effective_time: int = None,
        custom_claims: List[main_models.SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims] = None,
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
        # The validity period of the issued access token. Unit: seconds. Default value: 1200.
        self.access_token_effective_time = access_token_effective_time
        self.allowed_public_client = allowed_public_client
        # The validity period of the issued code. Unit: seconds. Default value: 60.
        self.code_effective_time = code_effective_time
        # The custom claims that are returned for the ID token.
        self.custom_claims = custom_claims
        # The scopes of user attributes that can be returned for the UserInfo endpoint or ID token.
        self.grant_scopes = grant_scopes
        # The authorization types that are supported for OIDC protocols.
        self.grant_types = grant_types
        # The validity period of the issued ID token. Unit: seconds. Default value: 300.
        self.id_token_effective_time = id_token_effective_time
        # The ID of the identity authentication source in password mode. Configure this parameter only when the value of the GrantTypes parameter includes the password mode.
        self.password_authentication_source_id = password_authentication_source_id
        # Specifies whether time-based one-time password (TOTP) authentication is required in password mode. Configure this parameter only when the value of the GrantTypes parameter includes the password mode.
        self.password_totp_mfa_required = password_totp_mfa_required
        # The algorithms that are used to calculate the code challenge for PKCE.
        self.pkce_challenge_methods = pkce_challenge_methods
        # Specifies whether the SSO of the application requires Proof Key for Code Exchange (PKCE) (RFC 7636).
        self.pkce_required = pkce_required
        # The logout redirect URIs that are supported by the application.
        self.post_logout_redirect_uris = post_logout_redirect_uris
        # The redirect URIs that are supported by the application.
        self.redirect_uris = redirect_uris
        # The validity period of the issued refresh token. Unit: seconds. Default value: 86400.
        self.refresh_token_effective = refresh_token_effective
        # The response types that are supported by the application. Configure this parameter when the value of the GrantTypes parameter includes the implicit mode.
        self.response_types = response_types
        # The custom expression that is used to calculate the subject ID returned for the ID token.
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
                temp_model = main_models.SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims()
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

class SetApplicationSsoConfigRequestOidcSsoConfigCustomClaims(DaraModel):
    def __init__(
        self,
        claim_name: str = None,
        claim_value_expression: str = None,
    ):
        # The claim name.
        self.claim_name = claim_name
        # The expression that is used to calculate the value of the claim.
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

