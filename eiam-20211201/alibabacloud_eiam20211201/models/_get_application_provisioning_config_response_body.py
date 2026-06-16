# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationProvisioningConfigResponseBody(DaraModel):
    def __init__(
        self,
        application_provisioning_config: main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig = None,
        request_id: str = None,
    ):
        # The account synchronization configuration of the application.
        self.application_provisioning_config = application_provisioning_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_provisioning_config:
            self.application_provisioning_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_provisioning_config is not None:
            result['ApplicationProvisioningConfig'] = self.application_provisioning_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationProvisioningConfig') is not None:
            temp_model = main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig()
            self.application_provisioning_config = temp_model.from_map(m.get('ApplicationProvisioningConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfig(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        callback_provisioning_config: main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig = None,
        config_operate_mode: str = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        provision_jwks_endpoint: str = None,
        provision_password: bool = None,
        provision_protocol_type: str = None,
        scim_provisioning_config: main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig = None,
        status: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The configuration parameters for the custom event callback protocol of IDaaS.
        self.callback_provisioning_config = callback_provisioning_config
        # The rendering mode of the account synchronization page. Valid values:
        # 
        # - standard: standard mode.
        # 
        # - template: template mode.
        self.config_operate_mode = config_operate_mode
        # The instance ID.
        self.instance_id = instance_id
        # The network endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The public key endpoint for signature verification of application synchronization callback messages.
        self.provision_jwks_endpoint = provision_jwks_endpoint
        # Indicates whether to synchronize passwords in IDaaS user event callbacks. Valid values:
        # 
        # - true: Passwords are synchronized.
        # 
        # - false: Passwords are not synchronized.
        self.provision_password = provision_password
        # The protocol type for application synchronization. Valid values:
        # 
        # - idaas_callback: the custom event callback protocol of IDaaS.
        # 
        # - scim2: the System for Cross-domain Identity Management (SCIM) protocol.
        self.provision_protocol_type = provision_protocol_type
        # The configuration parameters for IDaaS SCIM protocol synchronization.
        self.scim_provisioning_config = scim_provisioning_config
        # The status of the IDaaS account synchronization feature. Valid values:
        # 
        # - enabled: The feature is enabled.
        # 
        # - disabled: The feature is disabled.
        self.status = status

    def validate(self):
        if self.callback_provisioning_config:
            self.callback_provisioning_config.validate()
        if self.scim_provisioning_config:
            self.scim_provisioning_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.callback_provisioning_config is not None:
            result['CallbackProvisioningConfig'] = self.callback_provisioning_config.to_map()

        if self.config_operate_mode is not None:
            result['ConfigOperateMode'] = self.config_operate_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.provision_jwks_endpoint is not None:
            result['ProvisionJwksEndpoint'] = self.provision_jwks_endpoint

        if self.provision_password is not None:
            result['ProvisionPassword'] = self.provision_password

        if self.provision_protocol_type is not None:
            result['ProvisionProtocolType'] = self.provision_protocol_type

        if self.scim_provisioning_config is not None:
            result['ScimProvisioningConfig'] = self.scim_provisioning_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CallbackProvisioningConfig') is not None:
            temp_model = main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig()
            self.callback_provisioning_config = temp_model.from_map(m.get('CallbackProvisioningConfig'))

        if m.get('ConfigOperateMode') is not None:
            self.config_operate_mode = m.get('ConfigOperateMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('ProvisionJwksEndpoint') is not None:
            self.provision_jwks_endpoint = m.get('ProvisionJwksEndpoint')

        if m.get('ProvisionPassword') is not None:
            self.provision_password = m.get('ProvisionPassword')

        if m.get('ProvisionProtocolType') is not None:
            self.provision_protocol_type = m.get('ProvisionProtocolType')

        if m.get('ScimProvisioningConfig') is not None:
            temp_model = main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig()
            self.scim_provisioning_config = temp_model.from_map(m.get('ScimProvisioningConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfig(DaraModel):
    def __init__(
        self,
        authn_configuration: main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration = None,
        full_push_scopes: List[str] = None,
        provisioning_actions: List[str] = None,
        scim_base_url: str = None,
    ):
        # The configuration parameters for SCIM protocol synchronization.
        self.authn_configuration = authn_configuration
        # The scope of a full push for the SCIM protocol. Valid values:
        # 
        # - urn:alibaba:idaas:app:scim:User:PUSH: performs a full synchronization of users.
        self.full_push_scopes = full_push_scopes
        # The operations on the target resource for the SCIM protocol. Valid values:
        # 
        # - urn:alibaba:idaas:app:scim:User:CREATE: creates an account.
        # 
        # - urn:alibaba:idaas:app:scim:User:UPDATE: updates an account.
        # 
        # - urn:alibaba:idaas:app:scim:User:DELETE: deletes an account.
        self.provisioning_actions = provisioning_actions
        # The base URL where the application receives IDaaS SCIM protocol synchronization.
        self.scim_base_url = scim_base_url

    def validate(self):
        if self.authn_configuration:
            self.authn_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_configuration is not None:
            result['AuthnConfiguration'] = self.authn_configuration.to_map()

        if self.full_push_scopes is not None:
            result['FullPushScopes'] = self.full_push_scopes

        if self.provisioning_actions is not None:
            result['ProvisioningActions'] = self.provisioning_actions

        if self.scim_base_url is not None:
            result['ScimBaseUrl'] = self.scim_base_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnConfiguration') is not None:
            temp_model = main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration()
            self.authn_configuration = temp_model.from_map(m.get('AuthnConfiguration'))

        if m.get('FullPushScopes') is not None:
            self.full_push_scopes = m.get('FullPushScopes')

        if m.get('ProvisioningActions') is not None:
            self.provisioning_actions = m.get('ProvisioningActions')

        if m.get('ScimBaseUrl') is not None:
            self.scim_base_url = m.get('ScimBaseUrl')

        return self

class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfiguration(DaraModel):
    def __init__(
        self,
        authn_mode: str = None,
        authn_param: main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam = None,
        grant_type: str = None,
    ):
        # The authorization mode for the SCIM protocol interface. Valid values:
        # 
        # - oauth2: OAuth2 mode.
        self.authn_mode = authn_mode
        # The authorization configuration parameters. Usage:
        # 
        # - If GrantType is set to client_credentials, you must specify ClientId, ClientSecret, and AuthnMethod.
        # 
        # - If GrantType is set to bearer_token, you must specify AccessToken.
        self.authn_param = authn_param
        # The authorization mode for the SCIM protocol. Valid values:
        # 
        # - client_credentials: client credentials mode.
        # 
        # - bearer_token: bearer token mode.
        self.grant_type = grant_type

    def validate(self):
        if self.authn_param:
            self.authn_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authn_mode is not None:
            result['AuthnMode'] = self.authn_mode

        if self.authn_param is not None:
            result['AuthnParam'] = self.authn_param.to_map()

        if self.grant_type is not None:
            result['GrantType'] = self.grant_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthnMode') is not None:
            self.authn_mode = m.get('AuthnMode')

        if m.get('AuthnParam') is not None:
            temp_model = main_models.GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam()
            self.authn_param = temp_model.from_map(m.get('AuthnParam'))

        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        return self

class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigScimProvisioningConfigAuthnConfigurationAuthnParam(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        authn_method: str = None,
        client_id: str = None,
        client_secret: str = None,
        token_endpoint: str = None,
    ):
        # The access token. This parameter is required when GrantType is set to bearer_token.
        self.access_token = access_token
        # The authentication mode for the SCIM protocol. Valid values:
        # 
        # - client_secret_basic: The key is passed in the request header.
        # 
        # - client_secret_post: The key is passed in the request body.
        self.authn_method = authn_method
        # The client ID of the application.
        self.client_id = client_id
        # The client secret of the application.
        self.client_secret = client_secret
        # The token endpoint.
        self.token_endpoint = token_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.authn_method is not None:
            result['AuthnMethod'] = self.authn_method

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.token_endpoint is not None:
            result['TokenEndpoint'] = self.token_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AuthnMethod') is not None:
            self.authn_method = m.get('AuthnMethod')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('TokenEndpoint') is not None:
            self.token_endpoint = m.get('TokenEndpoint')

        return self

class GetApplicationProvisioningConfigResponseBodyApplicationProvisioningConfigCallbackProvisioningConfig(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        encrypt_key: str = None,
        encrypt_required: bool = None,
        listen_event_scopes: List[str] = None,
    ):
        # The destination address where the application receives IDaaS event callbacks.
        self.callback_url = callback_url
        # The symmetric key for encrypting and decrypting IDaaS event callbacks. This key uses the AES-256 algorithm and is in hexadecimal format.
        self.encrypt_key = encrypt_key
        # Indicates whether to encrypt IDaaS event callback messages. Valid values:
        # 
        # - true: The messages are encrypted.
        # 
        # - false: The messages are not encrypted and are transmitted in plaintext.
        self.encrypt_required = encrypt_required
        # The list of message types for the IDaaS event callback listener.
        self.listen_event_scopes = listen_event_scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.encrypt_key is not None:
            result['EncryptKey'] = self.encrypt_key

        if self.encrypt_required is not None:
            result['EncryptRequired'] = self.encrypt_required

        if self.listen_event_scopes is not None:
            result['ListenEventScopes'] = self.listen_event_scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('EncryptKey') is not None:
            self.encrypt_key = m.get('EncryptKey')

        if m.get('EncryptRequired') is not None:
            self.encrypt_required = m.get('EncryptRequired')

        if m.get('ListenEventScopes') is not None:
            self.listen_event_scopes = m.get('ListenEventScopes')

        return self

