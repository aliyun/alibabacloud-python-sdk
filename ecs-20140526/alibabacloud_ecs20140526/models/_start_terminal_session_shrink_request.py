# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartTerminalSessionShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_line: str = None,
        connection_type: str = None,
        encryption_options_shrink: str = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        password_name: str = None,
        port_number: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_server: str = None,
        username: str = None,
    ):
        self.client_token = client_token
        # The command to run after the session is initiated. The command length cannot exceed 512 characters.
        # 
        # >  If you specify the `CommandLine` parameter, you cannot specify the `PortNumber` or `TargetServer` parameter.
        self.command_line = command_line
        # The network type of the WebSocket URL required to connect to the instance. Valid values:
        # 
        # *   Internet (default)
        # *   Intranet
        self.connection_type = connection_type
        self.encryption_options_shrink = encryption_options_shrink
        # The instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.password_name = password_name
        # The port number of the ECS instance. The port is used to forward data. After this parameter is configured, Cloud Assistant Agent forwards data to the specified port. For example, you can set this parameter to 22 for data forwarding over SSH.
        # 
        # This parameter is empty by default, which indicates that no port is configured to forward data.
        self.port_number = port_number
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IP address of the instance. You can use the IP address to access the destination service in a virtual private cloud (VPC).
        # 
        # >  If this parameter is not empty, `PortNumber` specifies the port number that is used by the managed instance to access the destination service in the VPC.
        self.target_server = target_server
        # The username used for connection establishment.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.encryption_options_shrink is not None:
            result['EncryptionOptions'] = self.encryption_options_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password_name is not None:
            result['PasswordName'] = self.password_name

        if self.port_number is not None:
            result['PortNumber'] = self.port_number

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_server is not None:
            result['TargetServer'] = self.target_server

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('EncryptionOptions') is not None:
            self.encryption_options_shrink = m.get('EncryptionOptions')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PasswordName') is not None:
            self.password_name = m.get('PasswordName')

        if m.get('PortNumber') is not None:
            self.port_number = m.get('PortNumber')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetServer') is not None:
            self.target_server = m.get('TargetServer')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

