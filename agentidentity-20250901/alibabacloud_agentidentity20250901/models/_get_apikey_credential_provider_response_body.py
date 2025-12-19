# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetAPIKeyCredentialProviderResponseBody(DaraModel):
    def __init__(
        self,
        apikey_credential_provider: main_models.GetAPIKeyCredentialProviderResponseBodyAPIKeyCredentialProvider = None,
        request_id: str = None,
    ):
        self.apikey_credential_provider = apikey_credential_provider
        self.request_id = request_id

    def validate(self):
        if self.apikey_credential_provider:
            self.apikey_credential_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_credential_provider is not None:
            result['APIKeyCredentialProvider'] = self.apikey_credential_provider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKeyCredentialProvider') is not None:
            temp_model = main_models.GetAPIKeyCredentialProviderResponseBodyAPIKeyCredentialProvider()
            self.apikey_credential_provider = temp_model.from_map(m.get('APIKeyCredentialProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAPIKeyCredentialProviderResponseBodyAPIKeyCredentialProvider(DaraModel):
    def __init__(
        self,
        apikey_credential_provider_name: str = None,
        create_time: str = None,
        credential_provider_arn: str = None,
        description: str = None,
        update_time: str = None,
    ):
        self.apikey_credential_provider_name = apikey_credential_provider_name
        self.create_time = create_time
        self.credential_provider_arn = credential_provider_arn
        self.description = description
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_credential_provider_name is not None:
            result['APIKeyCredentialProviderName'] = self.apikey_credential_provider_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_provider_arn is not None:
            result['CredentialProviderArn'] = self.credential_provider_arn

        if self.description is not None:
            result['Description'] = self.description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKeyCredentialProviderName') is not None:
            self.apikey_credential_provider_name = m.get('APIKeyCredentialProviderName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialProviderArn') is not None:
            self.credential_provider_arn = m.get('CredentialProviderArn')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

