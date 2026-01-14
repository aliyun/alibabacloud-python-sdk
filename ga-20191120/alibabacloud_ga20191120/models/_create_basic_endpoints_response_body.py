# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateBasicEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        endpoints: List[main_models.CreateBasicEndpointsResponseBodyEndpoints] = None,
        request_id: str = None,
    ):
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The endpoints in the endpoint group.
        self.endpoints = endpoints
        # The ID of the request.
        self.request_id = request_id

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
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateBasicEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateBasicEndpointsResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        endpoint_address: str = None,
        endpoint_id: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
    ):
        # The address of the endpoint.
        self.endpoint_address = endpoint_address
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The secondary address of the endpoint.
        # 
        # This parameter is returned if the endpoint type is **ECS**, **ENI**, or **NLB**.
        # 
        # *   If the endpoint type is **ECS**, **EndpointSubAddress** returns the primary or secondary private IP address of the primary ENI.
        # *   If the endpoint type is **ENI**, **EndpointSubAddress** returns the primary or secondary private IP address of the secondary ENI.
        # *   If the endpoint type is **NLB**, **EndpointSubAddress** returns the primary private IP address of the NLB backend server.
        self.endpoint_sub_address = endpoint_sub_address
        # The type of the endpoint. Valid values:
        # 
        # *   **ENI:** ENI.
        # *   **SLB:** CLB instance.
        # *   **ECS:** ECS instance.
        # *   **NLB:** NLB instance.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        return self

