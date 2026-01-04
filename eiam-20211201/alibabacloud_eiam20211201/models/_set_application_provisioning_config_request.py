# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class SetApplicationProvisioningConfigRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        callback_provisioning_config: main_models.SetApplicationProvisioningConfigRequestCallbackProvisioningConfig = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        provision_password: bool = None,
        provision_protocol_type: str = None,
        scim_provisioning_config: main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfig = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The configuration of event callback synchronization. This parameter is required when the ProvisionProtocolType parameter is set to idaas_callback.
        self.callback_provisioning_config = callback_provisioning_config
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.network_access_endpoint_id = network_access_endpoint_id
        # Specifies whether to synchronize the password in IDaaS user event callbacks. Valid values:
        # 
        # *   true: synchronize the password.
        # *   false: do not synchronize the password.
        self.provision_password = provision_password
        # The synchronization protocol type of the application. Valid values:
        # 
        # *   idaas_callback: custom event callback protocol of IDaaS.
        # *   scim2: System for Cross-domain Identity Management (SCIM) protocol.
        # 
        # This parameter is required.
        self.provision_protocol_type = provision_protocol_type
        # The configuration of SCIM-based IDaaS synchronization. This parameter is required when the ProvisionProtocolType parameter is set to scim2.
        self.scim_provisioning_config = scim_provisioning_config

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.provision_password is not None:
            result['ProvisionPassword'] = self.provision_password

        if self.provision_protocol_type is not None:
            result['ProvisionProtocolType'] = self.provision_protocol_type

        if self.scim_provisioning_config is not None:
            result['ScimProvisioningConfig'] = self.scim_provisioning_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CallbackProvisioningConfig') is not None:
            temp_model = main_models.SetApplicationProvisioningConfigRequestCallbackProvisioningConfig()
            self.callback_provisioning_config = temp_model.from_map(m.get('CallbackProvisioningConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('ProvisionPassword') is not None:
            self.provision_password = m.get('ProvisionPassword')

        if m.get('ProvisionProtocolType') is not None:
            self.provision_protocol_type = m.get('ProvisionProtocolType')

        if m.get('ScimProvisioningConfig') is not None:
            temp_model = main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfig()
            self.scim_provisioning_config = temp_model.from_map(m.get('ScimProvisioningConfig'))

        return self

class SetApplicationProvisioningConfigRequestScimProvisioningConfig(DaraModel):
    def __init__(
        self,
        authn_configuration: main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration = None,
        full_push_scopes: List[str] = None,
        provisioning_actions: List[str] = None,
        scim_base_url: str = None,
    ):
        # The configuration parameters related to SCIM-based synchronization.
        self.authn_configuration = authn_configuration
        # The full synchronization scope of the SCIM protocol. Valid value:
        # 
        # *   urn:alibaba:idaas:app:scim:User:PUSH: full account data synchronization.
        self.full_push_scopes = full_push_scopes
        # The resource operations of the SCIM protocol. Valid values:
        # 
        # *   urn:alibaba:idaas:app:scim:User:CREATE: account creation.
        # *   urn:alibaba:idaas:app:scim:User:UPDATE: account update.
        # *   urn:alibaba:idaas:app:scim:User:DELETE: account deletion.
        self.provisioning_actions = provisioning_actions
        # The base URL that the application uses to receive the SCIM protocol for IDaaS synchronization.
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
            temp_model = main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration()
            self.authn_configuration = temp_model.from_map(m.get('AuthnConfiguration'))

        if m.get('FullPushScopes') is not None:
            self.full_push_scopes = m.get('FullPushScopes')

        if m.get('ProvisioningActions') is not None:
            self.provisioning_actions = m.get('ProvisioningActions')

        if m.get('ScimBaseUrl') is not None:
            self.scim_base_url = m.get('ScimBaseUrl')

        return self

class SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfiguration(DaraModel):
    def __init__(
        self,
        authn_mode: str = None,
        authn_param: main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam = None,
        grant_type: str = None,
    ):
        # The authentication mode of the SCIM protocol. Valid value:
        # 
        # *   oauth2: OAuth2.0 mode.
        self.authn_mode = authn_mode
        # The configuration parameters related to authorization.
        # 
        # *   If the GrantType parameter is set to client_credentials, you can set the configuration parameters ClientId, ClientSecret, and AuthnMethod.
        # *   If the GrantType parameter is set to bearer_token, you can set the configuration parameter AccessToken.
        self.authn_param = authn_param
        # The grant type of the SCIM protocol. Valid values:
        # 
        # *   client_credentials: client mode.
        # *   bearer_token: key mode.
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
            temp_model = main_models.SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam()
            self.authn_param = temp_model.from_map(m.get('AuthnParam'))

        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        return self

class SetApplicationProvisioningConfigRequestScimProvisioningConfigAuthnConfigurationAuthnParam(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        authn_method: str = None,
        client_id: str = None,
        client_secret: str = None,
        token_endpoint: str = None,
    ):
        # The access token. If the GrantType parameter is set to bearer_token, you can set this parameter.
        self.access_token = access_token
        # The authentication mode of the SCIM protocol. Valid values:
        # 
        # *   client_secret_basic: The client secret is passed in the request header.
        # *   client_secret_post: The client secret is passed in the request body.
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

class SetApplicationProvisioningConfigRequestCallbackProvisioningConfig(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        encrypt_key: str = None,
        encrypt_required: bool = None,
        listen_event_scopes: List[str] = None,
    ):
        # The URL that the application uses to receive IDaaS event callbacks.
        self.callback_url = callback_url
        # The symmetric key for IDaaS event callbacks. The key is an AES-256 encryption key in the HEX format.
        self.encrypt_key = encrypt_key
        # Specifies whether to encrypt IDaaS event callback messages. Valid values:
        # 
        # *   true: encrypt the messages.
        # *   false: transmit the messages in plaintext.
        self.encrypt_required = encrypt_required
        # The list of types of IDaaS event callback messages that are supported by the listener.
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

