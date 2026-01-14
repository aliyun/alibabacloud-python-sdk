# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateCustomRoutingEndpointGroupsRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_configurations: List[main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # > If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The information about the endpoint groups.
        # 
        # You can specify at most five endpoint groups.
        # 
        # This parameter is required.
        self.endpoint_group_configurations = endpoint_group_configurations
        # The ID of the custom routing listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.endpoint_group_configurations:
            for v1 in self.endpoint_group_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k1 in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k1 in m.get('EndpointGroupConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_configurations: List[main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations] = None,
        endpoint_configurations: List[main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        name: str = None,
    ):
        # The description of the endpoint group.
        # 
        # The description cannot exceed 256 characters in length and cannot contain `http://` or `https://`.
        # 
        # You can specify at most five endpoint group descriptions.
        self.description = description
        # The mapping configuration of the endpoint group.
        # 
        # You need to specify the backend service ports and protocols for the endpoint group. The ports are mapped to listener ports.
        # 
        # You can specify at most 20 mapping configurations for each endpoint group.
        self.destination_configurations = destination_configurations
        # The information about the endpoints.
        # 
        # You can specify at most 10 endpoints for each endpoint group.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the region in which the endpoint group resides.
        # 
        # You can specify at most five region IDs.
        # 
        # This parameter is required.
        self.endpoint_group_region = endpoint_group_region
        # The name of the endpoint group.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # You can specify at most five endpoint group names.
        self.name = name

    def validate(self):
        if self.destination_configurations:
            for v1 in self.destination_configurations:
                 if v1:
                    v1.validate()
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k1 in self.destination_configurations:
                result['DestinationConfigurations'].append(k1.to_map() if k1 else None)

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k1 in m.get('DestinationConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k1))

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        # The name of the vSwitch that is specified as an endpoint.
        self.endpoint = endpoint
        # The destination to which traffic is forwarded.
        # 
        # You can specify at most 20 destinations for each endpoint.
        self.policy_configurations = policy_configurations
        # The traffic policy that is used to process traffic to the endpoint. Valid values:
        # 
        # *   **AllowAll**: allows all traffic to the endpoint.
        # *   **DenyAll** (default): denies all traffic to the endpoint.
        # *   **AllowCustom**: allows traffic only to specified destinations in the endpoint.
        # 
        # If you set this parameter to AllowCustom, you must specify IP addresses and port ranges as the destinations to which traffic is distributed. If you specify only IP addresses and do not specify port ranges, GA can forward traffic to the specified IP addresses over all destination ports.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The type of endpoint.
        # 
        # Set the value to **PrivateSubNet**, which specifies a private CIDR block. This is the default value.
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
                temp_model = main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k1))

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(DaraModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        # The IP address of the destination to which traffic is forwarded.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify at most 20 destination IP addresses for each endpoint.
        self.address = address
        # The port range of the destination to which traffic is forwarded. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # If you leave this parameter empty, traffic is forwarded to all destination ports.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for at most 20 destinations in each endpoint and specify at most five port ranges for each destination.
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
                temp_model = main_models.CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        return self

class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The first port of the destination port range. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for at most 20 destinations in each endpoint and specify at most five first ports for each destination.
        self.from_port = from_port
        # The last port of the destination port range. The value of this parameter must fall within the port range of the endpoint group.
        # 
        # This parameter takes effect only when **TrafficToEndpointPolicy** is set to **AllowCustom**.
        # 
        # You can specify port ranges for at most 20 destinations in each endpoint and specify at most five last ports for each destination.
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

class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        # The first backend service port for the endpoint group.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be smaller than or equal to the value of **ToPort**.
        # 
        # You can specify at most 20 first backend service ports for each endpoint group.
        self.from_port = from_port
        # The backend service protocol.
        # 
        # You can specify up to four backend service protocols in each mapping configuration.
        self.protocols = protocols
        # The last backend service port for the endpoint group.
        # 
        # Valid values: **1** to **65499**. The value of **FromPort** must be smaller than or equal to the value of **ToPort**.
        # 
        # You can specify at most 20 last backend service ports for each endpoint group.
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

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

