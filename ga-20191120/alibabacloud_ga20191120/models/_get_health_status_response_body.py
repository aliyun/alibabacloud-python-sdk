# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class GetHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_groups: List[main_models.GetHealthStatusResponseBodyEndpointGroups] = None,
        health_status: str = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        # The information about the endpoint groups.
        self.endpoint_groups = endpoint_groups
        # The health status of endpoints and endpoint groups. Valid values:
        # 
        # *   **normal**
        # *   **abnormal**
        # *   **partiallyAbnormal**
        self.health_status = health_status
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.endpoint_groups:
            for v1 in self.endpoint_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k1 in self.endpoint_groups:
                result['EndpointGroups'].append(k1.to_map() if k1 else None)

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k1 in m.get('EndpointGroups'):
                temp_model = main_models.GetHealthStatusResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k1))

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHealthStatusResponseBodyEndpointGroups(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        endpoint_group_type: str = None,
        endpoints: List[main_models.GetHealthStatusResponseBodyEndpointGroupsEndpoints] = None,
        forwarding_rule_ids: List[str] = None,
        health_status: str = None,
    ):
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The type of the endpoint group. Valid values:
        # 
        # *   **default:** the default endpoint group.
        # *   **virtual:** a virtual endpoint group.
        self.endpoint_group_type = endpoint_group_type
        # The information about the endpoints.
        self.endpoints = endpoints
        # The IDs of the forwarding rules.
        self.forwarding_rule_ids = forwarding_rule_ids
        # The health status of the endpoint group. Valid values:
        # 
        # *   **init:** The endpoint group is being initialized.
        # *   **normal:** The endpoint group is normal.
        # *   **abnormal:** The endpoint group is abnormal.
        # *   **partiallyAbnormal:** The endpoint group is partially abnormal.
        self.health_status = health_status

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.GetHealthStatusResponseBodyEndpointGroupsEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        return self

class GetHealthStatusResponseBodyEndpointGroupsEndpoints(DaraModel):
    def __init__(
        self,
        address: str = None,
        endpoint_id: str = None,
        health_detail: str = None,
        health_status: str = None,
        port: int = None,
        type: str = None,
    ):
        # The IP address of the endpoint.
        self.address = address
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The health check details of the endpoint.
        # 
        # >  This parameter is unavailable.
        self.health_detail = health_detail
        # The health status of the endpoint. Valid values:
        # 
        # *   **init:** The endpoint is being initialized.
        # *   **normal:** The endpoint is normal.
        # *   **abnormal:** The endpoint is abnormal.
        self.health_status = health_status
        # The port that is used to connect to the endpoint.
        self.port = port
        # The type of the endpoint. Valid values:
        # 
        # *   **Domain:** a custom domain name.
        # *   **Ip:** a custom IP address.
        # *   **PublicIp:** a public IP address provided by Alibaba Cloud.
        # *   **ECS:** an Elastic Compute Service (ECS) instance.
        # *   **SLB:** a Classic Load Balancer (CLB) instance.
        # *   **ALB:** an Application Load Balancer (ALB) instance.
        # *   **OSS:** an Object Storage Service (OSS) bucket.
        # *   **ENI:** an elastic network interface (ENI).
        # *   **NLB:** a Network Load Balancer (NLB) instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.health_detail is not None:
            result['HealthDetail'] = self.health_detail

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.port is not None:
            result['Port'] = self.port

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('HealthDetail') is not None:
            self.health_detail = m.get('HealthDetail')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

