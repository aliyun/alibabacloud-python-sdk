# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceEndpointShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_string_prefix: str = None,
        dbinstance_endpoint_description: str = None,
        dbinstance_endpoint_type: str = None,
        dbinstance_id: str = None,
        node_items_shrink: str = None,
        port: str = None,
        private_ip_address: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The prefix of the internal endpoint.
        # 
        # When you create any type of endpoint, an internal endpoint is automatically created for the endpoint. This parameter specifies the prefix of the internal endpoint.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The user-defined description of the endpoint.
        self.dbinstance_endpoint_description = dbinstance_endpoint_description
        # The endpoint type. Valid values:
        # 
        # *   Primary: read/write endpoint of the instance
        # *   Readonly: read-only endpoint of the instance
        # 
        # This parameter is required.
        self.dbinstance_endpoint_type = dbinstance_endpoint_type
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The information about the endpoint.
        # 
        # This parameter is required.
        self.node_items_shrink = node_items_shrink
        # The port number of the internal endpoint. You can specify the port number for the internal endpoint.
        # 
        # Valid values: 3000 to 5999.
        # 
        # This parameter is required.
        self.port = port
        # The IP address of the internal endpoint.
        self.private_ip_address = private_ip_address
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to obtain the ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        # The vSwitch ID of the internal endpoint.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID of the internal endpoint.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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

        if self.dbinstance_endpoint_description is not None:
            result['DBInstanceEndpointDescription'] = self.dbinstance_endpoint_description

        if self.dbinstance_endpoint_type is not None:
            result['DBInstanceEndpointType'] = self.dbinstance_endpoint_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_items_shrink is not None:
            result['NodeItems'] = self.node_items_shrink

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceEndpointDescription') is not None:
            self.dbinstance_endpoint_description = m.get('DBInstanceEndpointDescription')

        if m.get('DBInstanceEndpointType') is not None:
            self.dbinstance_endpoint_type = m.get('DBInstanceEndpointType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeItems') is not None:
            self.node_items_shrink = m.get('NodeItems')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

