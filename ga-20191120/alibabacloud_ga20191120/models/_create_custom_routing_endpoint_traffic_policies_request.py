# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateCustomRoutingEndpointTrafficPoliciesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_id: str = None,
        policy_configurations: List[main_models.CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # > If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request is different.
        self.client_token = client_token
        # The ID of the endpoint for which you want to create traffic destinations.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The configurations of the traffic destinations.
        # 
        # You can specify up to 500 traffic destinations for each endpoint.
        # 
        # This parameter is required.
        self.policy_configurations = policy_configurations
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.policy_configurations:
            for v1 in self.policy_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k1 in self.policy_configurations:
                result['PolicyConfigurations'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k1 in m.get('PolicyConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations(DaraModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[main_models.CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges] = None,
    ):
        # The IP address of the destination to which traffic is forwarded.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 500 destination IP addresses for each endpoint.
        # 
        # > This parameter is required.
        self.address = address
        # The port range of the destination to which traffic is forwarded. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # If you leave this parameter empty, traffic is forwarded to all destination ports.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 500 traffic destinations in each endpoint and specify up to 10 port ranges for each traffic destination.
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        return self

class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port of the destination port range. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # If the first port and the last port are not specified, traffic on all ports of the destination is allowed.
        # 
        # You can specify port ranges for up to 500 destinations in each endpoint and specify up to 10 first ports for each destination.
        self.from_port = from_port
        # The last port of the destination port range. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # If the first port and the last port are not specified, traffic on all ports of the destination is allowed.
        # 
        # You can specify port ranges for up to 500 destinations in each endpoint and specify up to 10 last ports for each destination.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

