# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProvidersResponseBody(DaraModel):
    def __init__(
        self,
        identity_providers: List[main_models.ListIdentityProvidersResponseBodyIdentityProviders] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.identity_providers = identity_providers
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.identity_providers:
            for v1 in self.identity_providers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdentityProviders'] = []
        if self.identity_providers is not None:
            for k1 in self.identity_providers:
                result['IdentityProviders'].append(k1.to_map() if k1 else None)

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
        self.identity_providers = []
        if m.get('IdentityProviders') is not None:
            for k1 in m.get('IdentityProviders'):
                temp_model = main_models.ListIdentityProvidersResponseBodyIdentityProviders()
                self.identity_providers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIdentityProvidersResponseBodyIdentityProviders(DaraModel):
    def __init__(
        self,
        allowed_audience: List[str] = None,
        create_time: str = None,
        description: str = None,
        discovery_url: str = None,
        identity_provider_arn: str = None,
        identity_provider_name: str = None,
        update_time: str = None,
    ):
        self.allowed_audience = allowed_audience
        self.create_time = create_time
        self.description = description
        self.discovery_url = discovery_url
        self.identity_provider_arn = identity_provider_arn
        self.identity_provider_name = identity_provider_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_audience is not None:
            result['AllowedAudience'] = self.allowed_audience

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.discovery_url is not None:
            result['DiscoveryURL'] = self.discovery_url

        if self.identity_provider_arn is not None:
            result['IdentityProviderArn'] = self.identity_provider_arn

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedAudience') is not None:
            self.allowed_audience = m.get('AllowedAudience')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiscoveryURL') is not None:
            self.discovery_url = m.get('DiscoveryURL')

        if m.get('IdentityProviderArn') is not None:
            self.identity_provider_arn = m.get('IdentityProviderArn')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

