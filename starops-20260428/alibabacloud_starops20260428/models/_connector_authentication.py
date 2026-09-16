# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class ConnectorAuthentication(DaraModel):
    def __init__(
        self,
        basic: main_models.ConnectorAuthenticationBasic = None,
        bot_token: main_models.ConnectorAuthenticationBotToken = None,
        oauth: main_models.ConnectorAuthenticationOauth = None,
        role: main_models.ConnectorAuthenticationRole = None,
        satellite: main_models.ConnectorAuthenticationSatellite = None,
        type: str = None,
    ):
        # The security identity information for basic authentication, excluding the password.
        self.basic = basic
        # The security identity information for the bot, excluding the token and signing key.
        self.bot_token = bot_token
        # The security identity information for OAuth, excluding the client secret.
        self.oauth = oauth
        # The security identity information based on the RAM role ARN.
        self.role = role
        # The security identity information based on local credential binding.
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
            temp_model = main_models.ConnectorAuthenticationBasic()
            self.basic = temp_model.from_map(m.get('basic'))

        if m.get('botToken') is not None:
            temp_model = main_models.ConnectorAuthenticationBotToken()
            self.bot_token = temp_model.from_map(m.get('botToken'))

        if m.get('oauth') is not None:
            temp_model = main_models.ConnectorAuthenticationOauth()
            self.oauth = temp_model.from_map(m.get('oauth'))

        if m.get('role') is not None:
            temp_model = main_models.ConnectorAuthenticationRole()
            self.role = temp_model.from_map(m.get('role'))

        if m.get('satellite') is not None:
            temp_model = main_models.ConnectorAuthenticationSatellite()
            self.satellite = temp_model.from_map(m.get('satellite'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ConnectorAuthenticationSatellite(DaraModel):
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

class ConnectorAuthenticationRole(DaraModel):
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

class ConnectorAuthenticationOauth(DaraModel):
    def __init__(
        self,
        client_id: str = None,
    ):
        # OAuth client ID
        # 
        # This parameter is required.
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        return self

class ConnectorAuthenticationBotToken(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
    ):
        # Bot ID
        # 
        # This parameter is required.
        self.bot_id = bot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['botId'] = self.bot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('botId') is not None:
            self.bot_id = m.get('botId')

        return self



class ConnectorAuthenticationBasic(DaraModel):
    def __init__(
        self,
        username: str = None,
    ):
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
        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')

        return self

