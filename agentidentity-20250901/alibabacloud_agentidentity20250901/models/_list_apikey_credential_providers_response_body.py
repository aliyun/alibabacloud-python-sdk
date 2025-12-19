# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListAPIKeyCredentialProvidersResponseBody(DaraModel):
    def __init__(
        self,
        apikey_credential_providers: List[main_models.ListAPIKeyCredentialProvidersResponseBodyAPIKeyCredentialProviders] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.apikey_credential_providers = apikey_credential_providers
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.apikey_credential_providers:
            for v1 in self.apikey_credential_providers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['APIKeyCredentialProviders'] = []
        if self.apikey_credential_providers is not None:
            for k1 in self.apikey_credential_providers:
                result['APIKeyCredentialProviders'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apikey_credential_providers = []
        if m.get('APIKeyCredentialProviders') is not None:
            for k1 in m.get('APIKeyCredentialProviders'):
                temp_model = main_models.ListAPIKeyCredentialProvidersResponseBodyAPIKeyCredentialProviders()
                self.apikey_credential_providers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAPIKeyCredentialProvidersResponseBodyAPIKeyCredentialProviders(DaraModel):
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

