# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBasicEndpointGroupRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        description: str = None,
        endpoint_address: str = None,
        endpoint_group_region: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
        name: str = None,
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
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The endpoint address.
        self.endpoint_address = endpoint_address
        # The ID of the region to which the endpoint group belongs.
        # 
        # You can call the [ListAvailableBusiRegions](https://help.aliyun.com/document_detail/2253223.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.endpoint_group_region = endpoint_group_region
        # The secondary address of the endpoint.
        # 
        # You must specify this parameter when the accelerated IP address is associated with the secondary private IP address of an Elastic Compute Service (ECS) instance or an elastic network interface (ENI).
        # 
        # *   When the endpoint type is **ECS**, you can set **EndpointSubAddress** to the secondary private IP address of the primary ENI. If the parameter is left empty, the primary private IP address of the primary ENI is used.
        # *   If the endpoint type is **ENI**, you can set **EndpointSubAddress** to the secondary private IP address of the secondary ENI. If the parameter is left empty, the primary private IP address of the secondary ENI is used.
        self.endpoint_sub_address = endpoint_sub_address
        # The type of the endpoint. Valid values:
        # 
        # *   **ENI**
        # *   **SLB**
        # *   **ECS**
        self.endpoint_type = endpoint_type
        # The name of the endpoint group.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

