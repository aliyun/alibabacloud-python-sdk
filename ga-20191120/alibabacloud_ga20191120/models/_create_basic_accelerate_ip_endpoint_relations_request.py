# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateBasicAccelerateIpEndpointRelationsRequest(DaraModel):
    def __init__(
        self,
        accelerate_ip_endpoint_relations: List[main_models.CreateBasicAccelerateIpEndpointRelationsRequestAccelerateIpEndpointRelations] = None,
        accelerator_id: str = None,
        client_token: str = None,
        region_id: str = None,
    ):
        # A list of accelerated IP addresses and the endpoints with which the accelerated IP addresses are associated.
        # 
        # This parameter is required.
        self.accelerate_ip_endpoint_relations = accelerate_ip_endpoint_relations
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
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.accelerate_ip_endpoint_relations:
            for v1 in self.accelerate_ip_endpoint_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccelerateIpEndpointRelations'] = []
        if self.accelerate_ip_endpoint_relations is not None:
            for k1 in self.accelerate_ip_endpoint_relations:
                result['AccelerateIpEndpointRelations'].append(k1.to_map() if k1 else None)

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerate_ip_endpoint_relations = []
        if m.get('AccelerateIpEndpointRelations') is not None:
            for k1 in m.get('AccelerateIpEndpointRelations'):
                temp_model = main_models.CreateBasicAccelerateIpEndpointRelationsRequestAccelerateIpEndpointRelations()
                self.accelerate_ip_endpoint_relations.append(temp_model.from_map(k1))

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateBasicAccelerateIpEndpointRelationsRequestAccelerateIpEndpointRelations(DaraModel):
    def __init__(
        self,
        accelerate_ip_id: str = None,
        endpoint_id: str = None,
    ):
        # The IDs of the accelerated IP addresses.
        # 
        # You can call the [ListBasicAccelerateIps](https://help.aliyun.com/document_detail/2253393.html) operation to query the IDs of the accelerated IP addresses.
        # 
        # You can specify up to 20 IP address IDs.
        self.accelerate_ip_id = accelerate_ip_id
        # The IDs of the endpoints.
        # 
        # You can call the [ListBasicEndpoints](https://help.aliyun.com/document_detail/2253406.html) to query the IDs of the endpoints.
        # 
        # You can specify up to 20 endpoint IDs.
        self.endpoint_id = endpoint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        return self

