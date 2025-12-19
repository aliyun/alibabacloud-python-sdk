# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class UpdateOAuth2CredentialProviderRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        credential_provider_vendor: str = None,
        description: str = None,
        oauth2_credential_provider_name: str = None,
        oauth2_provider_config: main_models.OAuth2ProviderConfig = None,
    ):
        self.callback_url = callback_url
        # AliyunOAuth2
        self.credential_provider_vendor = credential_provider_vendor
        self.description = description
        self.oauth2_credential_provider_name = oauth2_credential_provider_name
        self.oauth2_provider_config = oauth2_provider_config

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

        if self.credential_provider_vendor is not None:
            result['CredentialProviderVendor'] = self.credential_provider_vendor

        if self.description is not None:
            result['Description'] = self.description

        if self.oauth2_credential_provider_name is not None:
            result['OAuth2CredentialProviderName'] = self.oauth2_credential_provider_name

        if self.oauth2_provider_config is not None:
            result['OAuth2ProviderConfig'] = self.oauth2_provider_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('CredentialProviderVendor') is not None:
            self.credential_provider_vendor = m.get('CredentialProviderVendor')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OAuth2CredentialProviderName') is not None:
            self.oauth2_credential_provider_name = m.get('OAuth2CredentialProviderName')

        if m.get('OAuth2ProviderConfig') is not None:
            temp_model = main_models.OAuth2ProviderConfig()
            self.oauth2_provider_config = temp_model.from_map(m.get('OAuth2ProviderConfig'))

        return self

