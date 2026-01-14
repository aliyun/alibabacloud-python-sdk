# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicEndpointGroupResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_address: str = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
        name: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The description of the endpoint group.
        self.description = description
        # The address of the endpoint.
        self.endpoint_address = endpoint_address
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region where the endpoint group resides.
        self.endpoint_group_region = endpoint_group_region
        # The secondary address of the endpoint.
        # 
        # This parameter is returned if the endpoint type is **ECS**, **ENI**, or **NLB**.
        # 
        # *   If the endpoint type is **ECS**, **EndpointSubAddress** returns the primary or secondary private IP address of the primary ENI.
        # *   If the endpoint type is **ENI**, **EndpointSubAddress** returns the primary or secondary private IP address of the secondary ENI.
        # *   If the endpoint type is **NLB**, **EndpointSubAddress** returns the primary private IP address of the NLB backend server.
        self.endpoint_sub_address = endpoint_sub_address
        # The type of endpoint. Valid values:
        # 
        # *   **ENI**: elastic network interface (ENI).
        # *   **SLB**: Classic Load Balancer (CLB) instance.
        # *   **ECS**: Elastic Compute Service (ECS) instance.
        # *   **NLB**: Network Load Balancer (NLB) instance
        self.endpoint_type = endpoint_type
        # The name of the endpoint group.
        self.name = name
        # The ID of the request.
        self.request_id = request_id
        # The status of the endpoint group. Valid values:
        # 
        # *   **init**: being initialized.
        # *   **active**: running as expected.
        # *   **updating**: being updated.
        # *   **deleting**: being deleted.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

