# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class ListEgressProxyIpPoolsResponseBody(DaraModel):
    def __init__(
        self,
        egress_proxy_ip_pools: List[main_models.ListEgressProxyIpPoolsResponseBodyEgressProxyIpPools] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.egress_proxy_ip_pools = egress_proxy_ip_pools
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.egress_proxy_ip_pools:
            for v1 in self.egress_proxy_ip_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EgressProxyIpPools'] = []
        if self.egress_proxy_ip_pools is not None:
            for k1 in self.egress_proxy_ip_pools:
                result['EgressProxyIpPools'].append(k1.to_map() if k1 else None)

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
        self.egress_proxy_ip_pools = []
        if m.get('EgressProxyIpPools') is not None:
            for k1 in m.get('EgressProxyIpPools'):
                temp_model = main_models.ListEgressProxyIpPoolsResponseBodyEgressProxyIpPools()
                self.egress_proxy_ip_pools.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEgressProxyIpPoolsResponseBodyEgressProxyIpPools(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        create_time: str = None,
        description: str = None,
        egress_proxy_gateway_id: str = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_ip_pool_name: str = None,
        hash_factor: str = None,
        hash_header_name: str = None,
        scheduler: str = None,
        status: str = None,
        tags: List[main_models.ListEgressProxyIpPoolsResponseBodyEgressProxyIpPoolsTags] = None,
    ):
        self.address_type = address_type
        self.create_time = create_time
        self.description = description
        self.egress_proxy_gateway_id = egress_proxy_gateway_id
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        self.egress_proxy_ip_pool_name = egress_proxy_ip_pool_name
        self.hash_factor = hash_factor
        self.hash_header_name = hash_header_name
        self.scheduler = scheduler
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_gateway_id is not None:
            result['EgressProxyGatewayId'] = self.egress_proxy_gateway_id

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_ip_pool_name is not None:
            result['EgressProxyIpPoolName'] = self.egress_proxy_ip_pool_name

        if self.hash_factor is not None:
            result['HashFactor'] = self.hash_factor

        if self.hash_header_name is not None:
            result['HashHeaderName'] = self.hash_header_name

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyGatewayId') is not None:
            self.egress_proxy_gateway_id = m.get('EgressProxyGatewayId')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyIpPoolName') is not None:
            self.egress_proxy_ip_pool_name = m.get('EgressProxyIpPoolName')

        if m.get('HashFactor') is not None:
            self.hash_factor = m.get('HashFactor')

        if m.get('HashHeaderName') is not None:
            self.hash_header_name = m.get('HashHeaderName')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEgressProxyIpPoolsResponseBodyEgressProxyIpPoolsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListEgressProxyIpPoolsResponseBodyEgressProxyIpPoolsTags(DaraModel):
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

