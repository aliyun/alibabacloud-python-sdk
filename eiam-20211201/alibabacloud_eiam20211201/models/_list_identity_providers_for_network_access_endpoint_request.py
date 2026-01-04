# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdentityProvidersForNetworkAccessEndpointRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        network_access_endpoint_id: str = None,
        next_token: str = None,
    ):
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 分页查询时每页行数。默认值为20，最大值为100。
        self.max_results = max_results
        # 网络端点ID。
        # 
        # This parameter is required.
        self.network_access_endpoint_id = network_access_endpoint_id
        # 查询凭证（Token），取值为上一次API调用返回的NextToken参数值。
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

