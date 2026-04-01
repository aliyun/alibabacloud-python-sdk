# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_string_prefix: str = None,
        dbinstance_endpoint_id: str = None,
        dbinstance_id: str = None,
        ip_type: str = None,
        port: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The prefix of the public endpoint.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The endpoint ID of the instance. You can call the DescribeDBInstanceEndpoints operation to query the endpoint ID.
        # 
        # This parameter is required.
        self.dbinstance_endpoint_id = dbinstance_endpoint_id
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the endpoint. Only Internet is supported. Set the value to **Public**.
        # 
        # This parameter is required.
        self.ip_type = ip_type
        # The port number of the public endpoint.
        # 
        # This parameter is required.
        self.port = port
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to obtain the ID of the resource group.
        self.resource_group_id = resource_group_id
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

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_endpoint_id is not None:
            result['DBInstanceEndpointId'] = self.dbinstance_endpoint_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceEndpointId') is not None:
            self.dbinstance_endpoint_id = m.get('DBInstanceEndpointId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

