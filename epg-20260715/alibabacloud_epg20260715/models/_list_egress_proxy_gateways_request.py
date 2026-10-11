# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyGatewaysRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_configuration_ids: List[str] = None,
        egress_proxy_gateway_ids: List[str] = None,
        egress_proxy_gateway_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        skip: int = None,
        status: str = None,
        tag: List[main_models.ListEgressProxyGatewaysRequestTag] = None,
        vpc_ids: List[str] = None,
    ):
        self.egress_proxy_configuration_ids = egress_proxy_configuration_ids
        self.egress_proxy_gateway_ids = egress_proxy_gateway_ids
        self.egress_proxy_gateway_names = egress_proxy_gateway_names
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id
        self.skip = skip
        self.status = status
        self.tag = tag
        self.vpc_ids = vpc_ids

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_configuration_ids is not None:
            result['EgressProxyConfigurationIds'] = self.egress_proxy_configuration_ids

        if self.egress_proxy_gateway_ids is not None:
            result['EgressProxyGatewayIds'] = self.egress_proxy_gateway_ids

        if self.egress_proxy_gateway_names is not None:
            result['EgressProxyGatewayNames'] = self.egress_proxy_gateway_names

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyConfigurationIds') is not None:
            self.egress_proxy_configuration_ids = m.get('EgressProxyConfigurationIds')

        if m.get('EgressProxyGatewayIds') is not None:
            self.egress_proxy_gateway_ids = m.get('EgressProxyGatewayIds')

        if m.get('EgressProxyGatewayNames') is not None:
            self.egress_proxy_gateway_names = m.get('EgressProxyGatewayNames')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListEgressProxyGatewaysRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')

        return self

class ListEgressProxyGatewaysRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

