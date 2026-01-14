# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBasicAccelerateIpEndpointRelationRequest(DaraModel):
    def __init__(
        self,
        accelerate_ip_id: str = None,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        # The ID of the accelerated IP address.
        # 
        # >  You must specify **EndpointId** or **AccelerateIpId**.
        self.accelerate_ip_id = accelerate_ip_id
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
        # The ID of the endpoint.
        # 
        # >  You must specify **EndpointId** or **AccelerateIpId**.
        self.endpoint_id = endpoint_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

