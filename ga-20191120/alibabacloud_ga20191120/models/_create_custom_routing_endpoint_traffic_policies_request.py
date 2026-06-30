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
        # The client token that is used to ensure the idempotence of a request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** value as the **ClientToken** value. The **RequestId** value is different for each API request.
        self.client_token = client_token
        # The ID of the endpoint for which you want to create traffic policies.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The traffic policy configurations.
        # 
        # You can specify up to 500 traffic policies for each endpoint.
        # 
        # This parameter is required.
        self.policy_configurations = policy_configurations
        # The region ID of the Global Accelerator instance. Set the value to **ap-southeast-1**.
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
        # The IP address of the traffic destination that is allowed to receive traffic.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 500 traffic destination IP addresses for each endpoint.
        # 
        # > This parameter is required.
        self.address = address
        # The port range of the traffic destination that is allowed to receive traffic. The port range must fall within the backend service port range of the endpoint group.
        # 
        # If you leave this parameter empty, all ports of the traffic destination are supported.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 500 port ranges for each endpoint, and up to 10 port ranges for each traffic destination.
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
        # The start port of the traffic destination that is allowed to receive traffic. The port value must fall within the backend service port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # If you leave both the start port and end port empty, all ports of the traffic destination are supported.
        # 
        # You can specify up to 500 port ranges for each endpoint, and up to 10 start ports for each traffic destination.
        self.from_port = from_port
        # The end port of the traffic destination that is allowed to receive traffic. The port value must fall within the backend service port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # If you leave both the start port and end port empty, all ports of the traffic destination are supported.
        # 
        # You can specify up to 500 port ranges for each endpoint, and up to 10 end ports for each traffic destination.
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

