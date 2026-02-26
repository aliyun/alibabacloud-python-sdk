# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateCredentialRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        credential_content: main_models.UpdateCredentialRequestCredentialContent = None,
        credential_id: str = None,
        credential_name: str = None,
        instance_id: str = None,
    ):
        # 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        # 
        # This parameter is required.
        self.client_token = client_token
        # 凭据的内容。
        self.credential_content = credential_content
        # 凭据ID。
        # 
        # This parameter is required.
        self.credential_id = credential_id
        # 凭据名称。
        self.credential_name = credential_name
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.credential_content:
            self.credential_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.credential_content is not None:
            result['CredentialContent'] = self.credential_content.to_map()

        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.credential_name is not None:
            result['CredentialName'] = self.credential_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CredentialContent') is not None:
            temp_model = main_models.UpdateCredentialRequestCredentialContent()
            self.credential_content = temp_model.from_map(m.get('CredentialContent'))

        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('CredentialName') is not None:
            self.credential_name = m.get('CredentialName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateCredentialRequestCredentialContent(DaraModel):
    def __init__(
        self,
        api_key_content: main_models.UpdateCredentialRequestCredentialContentApiKeyContent = None,
        oauth_client_content: main_models.UpdateCredentialRequestCredentialContentOAuthClientContent = None,
    ):
        # Api Key的内容。
        self.api_key_content = api_key_content
        # OAuth客户端认证凭证类型的凭据内容。
        self.oauth_client_content = oauth_client_content

    def validate(self):
        if self.api_key_content:
            self.api_key_content.validate()
        if self.oauth_client_content:
            self.oauth_client_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_content is not None:
            result['ApiKeyContent'] = self.api_key_content.to_map()

        if self.oauth_client_content is not None:
            result['OAuthClientContent'] = self.oauth_client_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyContent') is not None:
            temp_model = main_models.UpdateCredentialRequestCredentialContentApiKeyContent()
            self.api_key_content = temp_model.from_map(m.get('ApiKeyContent'))

        if m.get('OAuthClientContent') is not None:
            temp_model = main_models.UpdateCredentialRequestCredentialContentOAuthClientContent()
            self.oauth_client_content = temp_model.from_map(m.get('OAuthClientContent'))

        return self

class UpdateCredentialRequestCredentialContentOAuthClientContent(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
    ):
        # OAuth协议的client_id。
        self.client_id = client_id
        # OAuth协议的client_secret。
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class UpdateCredentialRequestCredentialContentApiKeyContent(DaraModel):
    def __init__(
        self,
        api_key: str = None,
    ):
        # API Key 凭证类型的凭据内容。
        self.api_key = api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        return self

