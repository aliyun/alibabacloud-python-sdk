# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        identity_provider: main_models.GetIdentityProviderResponseBodyIdentityProvider = None,
        request_id: str = None,
    ):
        self.identity_provider = identity_provider
        self.request_id = request_id

    def validate(self):
        if self.identity_provider:
            self.identity_provider.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider is not None:
            result['IdentityProvider'] = self.identity_provider.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProvider') is not None:
            temp_model = main_models.GetIdentityProviderResponseBodyIdentityProvider()
            self.identity_provider = temp_model.from_map(m.get('IdentityProvider'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIdentityProviderResponseBodyIdentityProvider(DaraModel):
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

