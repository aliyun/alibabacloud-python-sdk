# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyIpPoolsRequest(DaraModel):
    def __init__(
        self,
        egress_proxy_gateway_ids: List[str] = None,
        egress_proxy_ip_pool_ids: List[str] = None,
        egress_proxy_ip_pool_names: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
        status: str = None,
        tag: List[main_models.ListEgressProxyIpPoolsRequestTag] = None,
    ):
        self.egress_proxy_gateway_ids = egress_proxy_gateway_ids
        self.egress_proxy_ip_pool_ids = egress_proxy_ip_pool_ids
        self.egress_proxy_ip_pool_names = egress_proxy_ip_pool_names
        self.max_results = max_results
        self.next_token = next_token
        self.skip = skip
        self.status = status
        self.tag = tag

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
        if self.egress_proxy_gateway_ids is not None:
            result['EgressProxyGatewayIds'] = self.egress_proxy_gateway_ids

        if self.egress_proxy_ip_pool_ids is not None:
            result['EgressProxyIpPoolIds'] = self.egress_proxy_ip_pool_ids

        if self.egress_proxy_ip_pool_names is not None:
            result['EgressProxyIpPoolNames'] = self.egress_proxy_ip_pool_names

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyGatewayIds') is not None:
            self.egress_proxy_gateway_ids = m.get('EgressProxyGatewayIds')

        if m.get('EgressProxyIpPoolIds') is not None:
            self.egress_proxy_ip_pool_ids = m.get('EgressProxyIpPoolIds')

        if m.get('EgressProxyIpPoolNames') is not None:
            self.egress_proxy_ip_pool_names = m.get('EgressProxyIpPoolNames')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListEgressProxyIpPoolsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListEgressProxyIpPoolsRequestTag(DaraModel):
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

