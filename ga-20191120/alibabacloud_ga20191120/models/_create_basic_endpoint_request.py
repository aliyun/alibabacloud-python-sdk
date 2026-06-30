# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBasicEndpointRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_address: str = None,
        endpoint_group_id: str = None,
        endpoint_sub_address: str = None,
        endpoint_sub_address_type: str = None,
        endpoint_type: str = None,
        endpoint_zone_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The instance ID of the basic Alibaba Cloud Global Accelerator (GA).
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The address of the endpoint.
        # 
        # This parameter is required.
        self.endpoint_address = endpoint_address
        # The endpoint group ID of the basic Alibaba Cloud Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The secondary address of the endpoint.
        # 
        # This parameter is required when the endpoint type is **ECS**, **ENI**, or **NLB**.
        # - If the endpoint type is **ECS**, EndpointSubAddress can be set to a secondary private IP of the primary network interface controller (NIC). If you leave this parameter empty, the primary private IP of the primary network interface controller (NIC) is used.
        # - If the endpoint type is **ENI**, EndpointSubAddress can be set to a secondary private IP of the secondary network interface controller (NIC). If you leave this parameter empty, the primary private IP of the secondary network interface controller (NIC) is used.
        # - If the endpoint type is **NLB**, this parameter is required. Set EndpointSubAddress to the primary private IP of the NLB backend server.
        self.endpoint_sub_address = endpoint_sub_address
        # The type of the secondary address of the endpoint. Valid values:
        # - **primary**: The secondary address type is the primary private IP address.
        # - **secondary**: The secondary address type is a secondary private IP address.
        # 
        # This parameter is required when the endpoint type is **ECS**, **ENI**, or **NLB**. If the endpoint type is **NLB**, only **primary** is supported.
        self.endpoint_sub_address_type = endpoint_sub_address_type
        # The endpoint type. Valid values:
        # - **ENI**: Alibaba Cloud elastic network interface (ENI).
        # - **SLB**: Alibaba Cloud Classic Load Balancer (CLB) instance.
        # - **ECS**: Alibaba Cloud ECS instance.
        # - **NLB**: Alibaba Cloud Network Load Balancer (NLB) instance.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The zone ID of the endpoint.
        # 
        # Currently, this parameter is required only when the endpoint type is **NLB**.
        self.endpoint_zone_id = endpoint_zone_id
        # The name of the endpoint for the basic Alibaba Cloud Global Accelerator (GA) instance.
        # 
        # The name must be 1 to 128 characters in length and must start with a letter or a Chinese character. The name can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The region ID of the Global Accelerator instance. Set the value to **ap-southeast-1**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address

        if self.endpoint_sub_address_type is not None:
            result['EndpointSubAddressType'] = self.endpoint_sub_address_type

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_zone_id is not None:
            result['EndpointZoneId'] = self.endpoint_zone_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')

        if m.get('EndpointSubAddressType') is not None:
            self.endpoint_sub_address_type = m.get('EndpointSubAddressType')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointZoneId') is not None:
            self.endpoint_zone_id = m.get('EndpointZoneId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

