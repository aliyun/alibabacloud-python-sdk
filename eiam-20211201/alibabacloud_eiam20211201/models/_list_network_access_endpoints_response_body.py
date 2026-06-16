# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListNetworkAccessEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        network_access_endpoints: List[main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A collection of network endpoints.
        self.network_access_endpoints = network_access_endpoints
        # The token returned for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.network_access_endpoints:
            for v1 in self.network_access_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAccessEndpoints'] = []
        if self.network_access_endpoints is not None:
            for k1 in self.network_access_endpoints:
                result['NetworkAccessEndpoints'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_access_endpoints = []
        if m.get('NetworkAccessEndpoints') is not None:
            for k1 in m.get('NetworkAccessEndpoints'):
                temp_model = main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints()
                self.network_access_endpoints.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        network_access_endpoint_name: str = None,
        network_access_endpoint_type: str = None,
        security_group_id: str = None,
        status: str = None,
        update_time: int = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # The time when the network endpoint was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The network endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The name of the network endpoint.
        self.network_access_endpoint_name = network_access_endpoint_name
        # The type of the network endpoint. Valid values:
        # 
        # - shared: a shared network endpoint.
        # 
        # - private: a private network endpoint.
        self.network_access_endpoint_type = network_access_endpoint_type
        # The ID of the security group used by the private network endpoint.
        self.security_group_id = security_group_id
        # The status of the network endpoint. Valid values:
        # 
        # - pending: The endpoint is pending initialization.
        # 
        # - creating: The endpoint is being created.
        # 
        # - running: The endpoint is running.
        # 
        # - deleting: The endpoint is being deleted.
        self.status = status
        # The time when the network endpoint was last updated. This value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time
        # A list of vSwitches to which the private network endpoint is connected.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the private network endpoint is connected.
        self.vpc_id = vpc_id
        # The region ID of the VPC to which the private network endpoint is connected.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name

        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')

        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

