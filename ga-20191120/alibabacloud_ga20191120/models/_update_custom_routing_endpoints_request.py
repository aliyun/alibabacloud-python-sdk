# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateCustomRoutingEndpointsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_configurations: List[main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # The configurations of the endpoint.
        # 
        # This parameter is required.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the endpoint group to which the endpoints that you want to modify belong.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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
                temp_model = main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateCustomRoutingEndpointsRequestEndpointConfigurations(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        policy_configurations: List[main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
    ):
        # The ID of the endpoint.
        # 
        # You can specify up to 20 endpoint IDs.
        self.endpoint_id = endpoint_id
        # The configurations of the policy.
        self.policy_configurations = policy_configurations
        # The access policy of traffic for the specified endpoint. Default value: DenyAll. Valid values:
        # 
        # *   **DenyAll**: denies all traffic to the endpoint.
        # 
        # *   **AllowAll**: allows all traffic to the endpoint.
        # 
        # *   **AllowCustom**: allows traffic only to specified destinations.
        # 
        #     If you set this parameter to AllowCustom, you must specify IP addresses and port ranges of destinations to which to allow traffic. If you specify only IP addresses and do not specify port ranges, GA can forward traffic to all ports and the specified IP addresses in the destinations.
        # 
        # You can specify up to 20 access policies of traffic for the specified endpoint.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy

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
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k1 in self.policy_configurations:
                result['PolicyConfigurations'].append(k1.to_map() if k1 else None)

        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k1 in m.get('PolicyConfigurations'):
                temp_model = main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k1))

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        return self

class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(DaraModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        # The IP address of the destination to which to allow traffic.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify up to 20 destination IP addresses for each endpoint.
        self.address = address
        # The port range of the destination to which traffic is forwarded. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # If you leave this parameter empty, traffic is forwarded to all destination ports.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations for each endpoint and specify up to 20 port ranges for each destination.
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
                temp_model = main_models.UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        return self

class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(DaraModel):
    def __init__(
        self,
        from_port: str = None,
        to_port: str = None,
    ):
        # The start port of the port range in the destination to which to allow traffic. The specified port must fall within the port range of the specified endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations for each endpoint and specify up to 20 start ports for each destination.
        self.from_port = from_port
        # The end port of the port range in the destination to which to allow traffic. The specified port must fall within the port range of the specified endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for up to 20 destinations for each endpoint and specify up to 20 end ports for each destination.
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

