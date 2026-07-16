# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateCustomRoutingEndpointsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_configurations: List[main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of a request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** value as the **ClientToken** value. The **RequestId** value is different for each API request.
        self.client_token = client_token
        # The endpoint configurations.
        # 
        # You can specify up to 20 endpoint configurations.
        # 
        # This parameter is required.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the endpoint group in which you want to create an endpoint.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The region ID of the Alibaba Cloud Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateCustomRoutingEndpointsRequestEndpointConfigurations(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        # The instance ID of the endpoint vSwitch.
        self.endpoint = endpoint
        # The traffic destination configurations.
        # 
        # You can specify up to 20 traffic destinations for each endpoint.
        self.policy_configurations = policy_configurations
        # The traffic policy for the backend service. Valid values:
        # - **DenyAll** (default): denies all traffic to the specified backend service.
        # - **AllowAll**: allows all traffic to the specified backend service.
        # - **AllowCustom**: allows traffic only to specified destinations.
        # You must specify the IP address and port range of the destination. If the port range is left empty, all ports of the destination are supported.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The backend service type of the endpoint. Valid values:
        # 
        #  **PrivateSubNet** (default): private CIDR block.
        self.type = type

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
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k1 in self.policy_configurations:
                result['PolicyConfigurations'].append(k1.to_map() if k1 else None)

        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k1 in m.get('PolicyConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k1))

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(DaraModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        # The IP address of the traffic destination that can receive traffic.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 traffic destination IP addresses for each endpoint.
        # 
        # This parameter is required.
        self.address = address
        # The port range of the traffic destination that can receive traffic. The port range must fall within the backend service port range of the endpoint group.
        # 
        # If this parameter is left empty, all ports of the traffic destination are supported.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 20 port ranges for each traffic destination.
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
                temp_model = main_models.CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        return self

class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The start port of the traffic destination that can receive traffic. The port value must fall within the backend service port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 20 start ports for each traffic destination.
        self.from_port = from_port
        # The end port of the traffic destination that can receive traffic. The port value must fall within the backend service port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 port ranges for each endpoint, and up to 20 end ports for each traffic destination.
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

