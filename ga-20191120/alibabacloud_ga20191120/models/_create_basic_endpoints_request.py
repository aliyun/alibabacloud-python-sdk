# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateBasicEndpointsRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_group_id: str = None,
        endpoints: List[main_models.CreateBasicEndpointsRequestEndpoints] = None,
        region_id: str = None,
    ):
        # The ID of the basic GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the endpoint group.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The endpoints.
        # 
        # This parameter is required.
        self.endpoints = endpoints
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateBasicEndpointsRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateBasicEndpointsRequestEndpoints(DaraModel):
    def __init__(
        self,
        endpoint_address: str = None,
        endpoint_sub_address: str = None,
        endpoint_sub_address_type: str = None,
        endpoint_type: str = None,
        endpoint_zone_id: str = None,
        name: str = None,
    ):
        # The address of the endpoint.
        self.endpoint_address = endpoint_address
        # The secondary address of the endpoint.
        # 
        # This parameter is required only if you set the endpoint type to **ECS**, **ENI**, or **NLB**.
        # 
        # *   If you set the endpoint type to **ECS**, you can set **EndpointSubAddress** to the secondary private IP address of the primary ENI. If you leave this parameter empty, the primary private IP address of the primary ENI is used.
        # *   If you set the endpoint type to **ENI**, you can set **EndpointSubAddress** to the secondary private IP address of the secondary ENI. If you leave this parameter empty, the primary private IP address of the secondary ENI is used.
        # *   If you set the endpoint type to **NLB**, you can set **EndpointSubAddress** to the primary private IP address of the NLB backend server.
        self.endpoint_sub_address = endpoint_sub_address
        # The secondary address type of the endpoint. Valid values:
        # 
        # *   **primary**: a primary private IP address.
        # *   **secondary**: a secondary private IP address.
        # 
        # This parameter is required only if you set the endpoint type to **ECS**, **ENI**, or **NLB**. If you set the endpoint type to **NLB**, only **primary** is supported.
        self.endpoint_sub_address_type = endpoint_sub_address_type
        # The type of the endpoint. Valid values:
        # 
        # *   **ENI**: elastic network interface (ENI).
        # *   **SLB**: Classic Load Balancer (CLB) instance.
        # *   **ECS**: Elastic Compute Service (ECS) instance.
        # *   **NLB**: Network Load Balancer (NLB) instance.
        # 
        # >  This parameter is required.
        self.endpoint_type = endpoint_type
        # The ID of the zone where the endpoint resides.
        # 
        # This parameter is required only if you set the endpoint type to **NLB**.
        self.endpoint_zone_id = endpoint_zone_id
        # The name of the endpoint.
        # 
        # The name must be 1 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

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

        return self

