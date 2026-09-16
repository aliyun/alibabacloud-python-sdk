# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorAuthenticationInput(DaraModel):
    def __init__(
        self,
        basic: main_models.ConnectorAuthenticationInputBasic = None,
        bot_token: main_models.ConnectorAuthenticationInputBotToken = None,
        oauth: main_models.ConnectorAuthenticationInputOauth = None,
        pat_token: main_models.ConnectorAuthenticationInputPatToken = None,
        role: main_models.ConnectorAuthenticationInputRole = None,
        satellite: main_models.ConnectorAuthenticationInputSatellite = None,
        type: str = None,
    ):
        # Authenticates by using a username and password.
        self.basic = basic
        # Authenticates by using a bot token and a signing key.
        self.bot_token = bot_token
        # Authenticates by using an OAuth client identity.
        self.oauth = oauth
        # Authenticates by using a personal access token.
        self.pat_token = pat_token
        # Authenticates by using a RAM role ARN.
        self.role = role
        # Authenticates by using local credential binding.
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
            temp_model = main_models.ConnectorAuthenticationInputBasic()
            self.basic = temp_model.from_map(m.get('basic'))

        if m.get('botToken') is not None:
            temp_model = main_models.ConnectorAuthenticationInputBotToken()
            self.bot_token = temp_model.from_map(m.get('botToken'))

        if m.get('oauth') is not None:
            temp_model = main_models.ConnectorAuthenticationInputOauth()
            self.oauth = temp_model.from_map(m.get('oauth'))

        if m.get('patToken') is not None:
            temp_model = main_models.ConnectorAuthenticationInputPatToken()
            self.pat_token = temp_model.from_map(m.get('patToken'))

        if m.get('role') is not None:
            temp_model = main_models.ConnectorAuthenticationInputRole()
            self.role = temp_model.from_map(m.get('role'))

        if m.get('satellite') is not None:
            temp_model = main_models.ConnectorAuthenticationInputSatellite()
            self.satellite = temp_model.from_map(m.get('satellite'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ConnectorAuthenticationInputSatellite(DaraModel):
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

class ConnectorAuthenticationInputRole(DaraModel):
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

class ConnectorAuthenticationInputPatToken(DaraModel):
    def __init__(
        self,
        pat_token: str = None,
    ):
        # The personal access token used to access the target service.
        # 
        # This parameter is required.
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

class ConnectorAuthenticationInputOauth(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OAuth client ID
        # 
        # This parameter is required.
        self.client_id = client_id
        # OAuth client secret
        # 
        # This parameter is required.
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

class ConnectorAuthenticationInputBotToken(DaraModel):
    def __init__(
        self,
        bot_token: str = None,
        signing_secret: str = None,
    ):
        # Bot token
        # 
        # This parameter is required.
        self.bot_token = bot_token
        # Signing secret
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

class ConnectorAuthenticationInputBasic(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        # Password
        # 
        # This parameter is required.
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

