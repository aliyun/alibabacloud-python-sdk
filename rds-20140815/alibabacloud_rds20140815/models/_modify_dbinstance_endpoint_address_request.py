# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_string: str = None,
        connection_string_prefix: str = None,
        dbinstance_endpoint_id: str = None,
        dbinstance_id: str = None,
        port: str = None,
        private_ip_address: str = None,
        resource_owner_id: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The endpoint that you want to modify. The endpoint can be a public endpoint or an internal endpoint.
        # 
        # This parameter is required.
        self.connection_string = connection_string
        # The prefix of the new endpoint. You can modify only the prefix of the endpoint that is specified by the ConnectionString parameter.
        self.connection_string_prefix = connection_string_prefix
        # The endpoint ID of the instance. You can call the DescribeDBInstanceEndpoints operation to query the endpoint ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_endpoint_id = dbinstance_endpoint_id
        # The instance ID. You can call the DescribeDBInstances operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The port number of the new endpoint.
        self.port = port
        # The IP address of the internal endpoint.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # The vSwitch ID of the internal endpoint.
        self.v_switch_id = v_switch_id
        # The VPC ID of the internal endpoint.
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

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_endpoint_id is not None:
            result['DBInstanceEndpointId'] = self.dbinstance_endpoint_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

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

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceEndpointId') is not None:
            self.dbinstance_endpoint_id = m.get('DBInstanceEndpointId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

