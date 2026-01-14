# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCustomRoutingEndpointsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_group_id: str = None,
        endpoint_ids: List[str] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the endpoint group to which the endpoint that you want to delete belongs.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The IDs of endpoints to be deleted.
        # 
        # If you do not set this parameter, all the endpoints in the specified endpoint group are deleted.
        # 
        # You can specify at most 10 endpoint IDs.
        # 
        # This parameter is required.
        self.endpoint_ids = endpoint_ids
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

