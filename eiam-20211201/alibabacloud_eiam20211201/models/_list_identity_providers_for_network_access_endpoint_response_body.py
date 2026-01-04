# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProvidersForNetworkAccessEndpointResponseBody(DaraModel):
    def __init__(
        self,
        identity_providers_for_network_access_endpoint: List[main_models.ListIdentityProvidersForNetworkAccessEndpointResponseBodyIdentityProvidersForNetworkAccessEndpoint] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.identity_providers_for_network_access_endpoint = identity_providers_for_network_access_endpoint
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.identity_providers_for_network_access_endpoint:
            for v1 in self.identity_providers_for_network_access_endpoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdentityProvidersForNetworkAccessEndpoint'] = []
        if self.identity_providers_for_network_access_endpoint is not None:
            for k1 in self.identity_providers_for_network_access_endpoint:
                result['IdentityProvidersForNetworkAccessEndpoint'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.identity_providers_for_network_access_endpoint = []
        if m.get('IdentityProvidersForNetworkAccessEndpoint') is not None:
            for k1 in m.get('IdentityProvidersForNetworkAccessEndpoint'):
                temp_model = main_models.ListIdentityProvidersForNetworkAccessEndpointResponseBodyIdentityProvidersForNetworkAccessEndpoint()
                self.identity_providers_for_network_access_endpoint.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIdentityProvidersForNetworkAccessEndpointResponseBodyIdentityProvidersForNetworkAccessEndpoint(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        identity_provider_name: str = None,
        instance_id: str = None,
    ):
        # IdP的ID。
        self.identity_provider_id = identity_provider_id
        # IdP名称。
        self.identity_provider_name = identity_provider_name
        # IDaaS EIAM 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

