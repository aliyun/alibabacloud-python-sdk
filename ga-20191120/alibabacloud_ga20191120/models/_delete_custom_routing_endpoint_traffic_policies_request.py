# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCustomRoutingEndpointTrafficPoliciesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_id: str = None,
        policy_ids: List[str] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the endpoint for which you want to delete traffic destinations.
        # 
        # >  This parameter is required.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The IDs of the traffic destinations.
        # 
        # You can specify the IDs of up to 9,000 traffic destinations.
        # 
        # This parameter is required.
        self.policy_ids = policy_ids
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

