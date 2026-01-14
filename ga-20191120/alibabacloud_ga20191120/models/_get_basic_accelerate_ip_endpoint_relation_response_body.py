# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicAccelerateIpEndpointRelationResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_ip_id: str = None,
        accelerator_id: str = None,
        endpoint_address: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_sub_address: str = None,
        endpoint_sub_address_type: str = None,
        endpoint_type: str = None,
        endpoint_zone_id: str = None,
        ip_address: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The ID of the accelerated IP address.
        self.accelerate_ip_id = accelerate_ip_id
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The address of the endpoint.
        self.endpoint_address = endpoint_address
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The name of the endpoint.
        self.endpoint_name = endpoint_name
        # The secondary address of the endpoint.
        # 
        # This parameter is returned if the endpoint type is **ECS**, **ENI**, or **NLB**.
        # 
        # *   If the endpoint type is **ECS**, **EndpointSubAddress** returns the primary or secondary private IP address of the primary ENI.
        # *   If the endpoint type is **ENI**, **EndpointSubAddress** returns the primary or secondary private IP address of the secondary ENI.
        # *   If the endpoint type is **NLB**, **EndpointSubAddress** returns the primary private IP address of the NLB backend server.
        self.endpoint_sub_address = endpoint_sub_address
        # The type of the secondary address of the endpoint.
        # 
        # *   **primary**: a primary private IP address.
        # *   **secondary**: a secondary private IP address.
        # 
        # This parameter is returned if the endpoint type is **ECS**, **ENI**, or **NLB**. If the endpoint type is set to **NLB**, **primary** is returned.
        self.endpoint_sub_address_type = endpoint_sub_address_type
        # The type of endpoint. Valid values:
        # 
        # *   **ENI**: elastic network interface (ENI).
        # *   **SLB**: Classic Load Balancer (CLB) instance.
        # *   **ECS**: Elastic Compute Service (ECS) instance.
        # *   **NLB**: Network Load Balancer (NLB) instance.
        self.endpoint_type = endpoint_type
        # The ID of the zone where the endpoint is created.
        # 
        # This parameter is returned only when the endpoint type is **NLB**.
        self.endpoint_zone_id = endpoint_zone_id
        # The accelerated IP address of the basic GA instance.
        self.ip_address = ip_address
        # The ID of the request.
        self.request_id = request_id
        # The association status between the accelerated IP address and endpoint.
        # 
        # A value of **active** indicates that the accelerated IP address is associated with the endpoint.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address

        if self.endpoint_sub_address_type is not None:
            result['EndpointSubAddressType'] = self.endpoint_sub_address_type

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.endpoint_zone_id is not None:
            result['EndpointZoneId'] = self.endpoint_zone_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')

        if m.get('EndpointSubAddressType') is not None:
            self.endpoint_sub_address_type = m.get('EndpointSubAddressType')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('EndpointZoneId') is not None:
            self.endpoint_zone_id = m.get('EndpointZoneId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

