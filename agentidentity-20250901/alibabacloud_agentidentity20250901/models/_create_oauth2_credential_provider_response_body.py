# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class CreateOAuth2CredentialProviderResponseBody(DaraModel):
    def __init__(
        self,
        oauth2_credential_provider: main_models.CreateOAuth2CredentialProviderResponseBodyOAuth2CredentialProvider = None,
        request_id: str = None,
    ):
        self.oauth2_credential_provider = oauth2_credential_provider
        self.request_id = request_id

    def validate(self):
        if self.oauth2_credential_provider:
            self.oauth2_credential_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oauth2_credential_provider is not None:
            result['OAuth2CredentialProvider'] = self.oauth2_credential_provider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OAuth2CredentialProvider') is not None:
            temp_model = main_models.CreateOAuth2CredentialProviderResponseBodyOAuth2CredentialProvider()
            self.oauth2_credential_provider = temp_model.from_map(m.get('OAuth2CredentialProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateOAuth2CredentialProviderResponseBodyOAuth2CredentialProvider(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        create_time: str = None,
        credential_provider_arn: str = None,
        credential_provider_vendor: str = None,
        description: str = None,
        oauth2_credential_provider_name: str = None,
        oauth2_provider_config: main_models.OAuth2ProviderConfig = None,
        update_time: str = None,
    ):
        self.callback_url = callback_url
        self.create_time = create_time
        self.credential_provider_arn = credential_provider_arn
        self.credential_provider_vendor = credential_provider_vendor
        self.description = description
        self.oauth2_credential_provider_name = oauth2_credential_provider_name
        self.oauth2_provider_config = oauth2_provider_config
        self.update_time = update_time

    def validate(self):
        if self.oauth2_provider_config:
            self.oauth2_provider_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_provider_arn is not None:
            result['CredentialProviderArn'] = self.credential_provider_arn

        if self.credential_provider_vendor is not None:
            result['CredentialProviderVendor'] = self.credential_provider_vendor

        if self.description is not None:
            result['Description'] = self.description

        if self.oauth2_credential_provider_name is not None:
            result['OAuth2CredentialProviderName'] = self.oauth2_credential_provider_name

        if self.oauth2_provider_config is not None:
            result['OAuth2ProviderConfig'] = self.oauth2_provider_config.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialProviderArn') is not None:
            self.credential_provider_arn = m.get('CredentialProviderArn')

        if m.get('CredentialProviderVendor') is not None:
            self.credential_provider_vendor = m.get('CredentialProviderVendor')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OAuth2CredentialProviderName') is not None:
            self.oauth2_credential_provider_name = m.get('OAuth2CredentialProviderName')

        if m.get('OAuth2ProviderConfig') is not None:
            temp_model = main_models.OAuth2ProviderConfig()
            self.oauth2_provider_config = temp_model.from_map(m.get('OAuth2ProviderConfig'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

