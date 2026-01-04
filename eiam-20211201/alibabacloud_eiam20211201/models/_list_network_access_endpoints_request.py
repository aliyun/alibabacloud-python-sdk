# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetworkAccessEndpointsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        network_access_endpoint_status: str = None,
        network_access_endpoint_type: str = None,
        next_token: str = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 分页查询时每页行数。默认值为20，最大值为100。
        self.max_results = max_results
        # 专属网络端点连接的状态。NetworkAccessEndpointType取值为shared时不生效。
        self.network_access_endpoint_status = network_access_endpoint_status
        # 专属网络端点连接的类型。取值可选范围：1. private - 专属网络端点；2. shared - 共享网络端点
        self.network_access_endpoint_type = network_access_endpoint_type
        # 查询凭证（Token），取值为上一次API调用返回的NextToken参数值。
        self.next_token = next_token
        # 专属网络端点连接的Vpc ID。NetworkAccessEndpointType取值为shared时不生效。
        self.vpc_id = vpc_id
        # 专属网络端点连接的Vpc所属地域，该地域取值必须在ListNetworkAccessEndpointAvailableRegions接口中返回。NetworkAccessEndpointType取值为shared时不生效。
        self.vpc_region_id = vpc_region_id

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

        if self.network_access_endpoint_status is not None:
            result['NetworkAccessEndpointStatus'] = self.network_access_endpoint_status

        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkAccessEndpointStatus') is not None:
            self.network_access_endpoint_status = m.get('NetworkAccessEndpointStatus')

        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

