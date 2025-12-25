# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceEndpointShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_endpoint_description: str = None,
        dbinstance_endpoint_id: str = None,
        dbinstance_id: str = None,
        node_items_shrink: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The user-defined description of the endpoint.
        self.dbinstance_endpoint_description = dbinstance_endpoint_description
        # The endpoint ID of the instance. You can call the DescribeDBInstanceEndpoints operation to query the endpoint ID.
        # 
        # This parameter is required.
        self.dbinstance_endpoint_id = dbinstance_endpoint_id
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The information about the endpoint.
        self.node_items_shrink = node_items_shrink
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_endpoint_description is not None:
            result['DBInstanceEndpointDescription'] = self.dbinstance_endpoint_description

        if self.dbinstance_endpoint_id is not None:
            result['DBInstanceEndpointId'] = self.dbinstance_endpoint_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_items_shrink is not None:
            result['NodeItems'] = self.node_items_shrink

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceEndpointDescription') is not None:
            self.dbinstance_endpoint_description = m.get('DBInstanceEndpointDescription')

        if m.get('DBInstanceEndpointId') is not None:
            self.dbinstance_endpoint_id = m.get('DBInstanceEndpointId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeItems') is not None:
            self.node_items_shrink = m.get('NodeItems')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

