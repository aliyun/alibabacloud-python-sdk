# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorAuthenticationUpdateInput(DaraModel):
    def __init__(
        self,
        basic: main_models.ConnectorAuthenticationUpdateInputBasic = None,
        bot_token: main_models.ConnectorAuthenticationUpdateInputBotToken = None,
        oauth: main_models.ConnectorAuthenticationUpdateInputOauth = None,
        pat_token: main_models.ConnectorAuthenticationUpdateInputPatToken = None,
        role: main_models.ConnectorAuthenticationUpdateInputRole = None,
        satellite: main_models.ConnectorAuthenticationUpdateInputSatellite = None,
        type: str = None,
    ):
        # The configuration that uses a username and password to replace the existing authentication configuration.
        self.basic = basic
        # The configuration that uses a bot token and signing key to replace the existing authentication configuration.
        self.bot_token = bot_token
        # The configuration that uses an OAuth client identity to replace the existing authentication configuration.
        self.oauth = oauth
        # The configuration that uses a personal access token to replace the existing authentication configuration.
        self.pat_token = pat_token
        # The configuration that uses a RAM role ARN to replace the existing authentication configuration.
        self.role = role
        # The configuration that uses a local credential binding to replace the existing authentication configuration.
        self.satellite = satellite
        # Authentication type
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.basic:
            self.basic.validate()
        if self.bot_token:
            self.bot_token.validate()
        if self.oauth:
            self.oauth.validate()
        if self.pat_token:
            self.pat_token.validate()
        if self.role:
            self.role.validate()
        if self.satellite:
            self.satellite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic is not None:
            result['basic'] = self.basic.to_map()

        if self.bot_token is not None:
            result['botToken'] = self.bot_token.to_map()

        if self.oauth is not None:
            result['oauth'] = self.oauth.to_map()

        if self.pat_token is not None:
            result['patToken'] = self.pat_token.to_map()

        if self.role is not None:
            result['role'] = self.role.to_map()

        if self.satellite is not None:
            result['satellite'] = self.satellite.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basic') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputBasic()
            self.basic = temp_model.from_map(m.get('basic'))

        if m.get('botToken') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputBotToken()
            self.bot_token = temp_model.from_map(m.get('botToken'))

        if m.get('oauth') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputOauth()
            self.oauth = temp_model.from_map(m.get('oauth'))

        if m.get('patToken') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputPatToken()
            self.pat_token = temp_model.from_map(m.get('patToken'))

        if m.get('role') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputRole()
            self.role = temp_model.from_map(m.get('role'))

        if m.get('satellite') is not None:
            temp_model = main_models.ConnectorAuthenticationUpdateInputSatellite()
            self.satellite = temp_model.from_map(m.get('satellite'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ConnectorAuthenticationUpdateInputSatellite(DaraModel):
    def __init__(
        self,
        binding_name: str = None,
    ):
        # Local credential binding name
        # 
        # This parameter is required.
        self.binding_name = binding_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_name is not None:
            result['bindingName'] = self.binding_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingName') is not None:
            self.binding_name = m.get('bindingName')

        return self

class ConnectorAuthenticationUpdateInputRole(DaraModel):
    def __init__(
        self,
        role_arn: str = None,
    ):
        # Role ARN
        # 
        # This parameter is required.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        return self

class ConnectorAuthenticationUpdateInputPatToken(DaraModel):
    def __init__(
        self,
        pat_token: str = None,
    ):
        # The personal access token used to replace the existing credential.
        self.pat_token = pat_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pat_token is not None:
            result['patToken'] = self.pat_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('patToken') is not None:
            self.pat_token = m.get('patToken')

        return self

class ConnectorAuthenticationUpdateInputOauth(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OAuth client ID
        # 
        # This parameter is required.
        self.client_id = client_id
        # Replacement OAuth client secret
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_secret is not None:
            result['clientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientSecret') is not None:
            self.client_secret = m.get('clientSecret')

        return self

class ConnectorAuthenticationUpdateInputBotToken(DaraModel):
    def __init__(
        self,
        bot_token: str = None,
        signing_secret: str = None,
    ):
        # Replacement bot token
        # 
        # This parameter is required.
        self.bot_token = bot_token
        # Replacement signing secret
        self.signing_secret = signing_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_token is not None:
            result['botToken'] = self.bot_token

        if self.signing_secret is not None:
            result['signingSecret'] = self.signing_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('botToken') is not None:
            self.bot_token = m.get('botToken')

        if m.get('signingSecret') is not None:
            self.signing_secret = m.get('signingSecret')

        return self

class ConnectorAuthenticationUpdateInputBasic(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # Replacement password
        self.password = password
        # Username
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['password'] = self.password

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

