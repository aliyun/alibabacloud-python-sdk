# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeShardingNetworkAddressResponseBody(DaraModel):
    def __init__(
        self,
        compatible_connections: main_models.DescribeShardingNetworkAddressResponseBodyCompatibleConnections = None,
        network_addresses: main_models.DescribeShardingNetworkAddressResponseBodyNetworkAddresses = None,
        request_id: str = None,
    ):
        # The endpoints of DynamoDB-compatible instances.
        self.compatible_connections = compatible_connections
        # The endpoints of the ApsaraDB for MongoDB sharded cluster instance.
        self.network_addresses = network_addresses
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compatible_connections:
            self.compatible_connections.validate()
        if self.network_addresses:
            self.network_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compatible_connections is not None:
            result['CompatibleConnections'] = self.compatible_connections.to_map()

        if self.network_addresses is not None:
            result['NetworkAddresses'] = self.network_addresses.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleConnections') is not None:
            temp_model = main_models.DescribeShardingNetworkAddressResponseBodyCompatibleConnections()
            self.compatible_connections = temp_model.from_map(m.get('CompatibleConnections'))

        if m.get('NetworkAddresses') is not None:
            temp_model = main_models.DescribeShardingNetworkAddressResponseBodyNetworkAddresses()
            self.network_addresses = temp_model.from_map(m.get('NetworkAddresses'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeShardingNetworkAddressResponseBodyNetworkAddresses(DaraModel):
    def __init__(
        self,
        network_address: List[main_models.DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress] = None,
    ):
        self.network_address = network_address

    def validate(self):
        if self.network_address:
            for v1 in self.network_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAddress'] = []
        if self.network_address is not None:
            for k1 in self.network_address:
                result['NetworkAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_address = []
        if m.get('NetworkAddress') is not None:
            for k1 in m.get('NetworkAddress'):
                temp_model = main_models.DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress()
                self.network_address.append(temp_model.from_map(k1))

        return self

class DescribeShardingNetworkAddressResponseBodyNetworkAddressesNetworkAddress(DaraModel):
    def __init__(
        self,
        connection_type: str = None,
        expired_time: str = None,
        ipaddress: str = None,
        network_address: str = None,
        network_type: str = None,
        node_id: str = None,
        node_type: str = None,
        port: str = None,
        role: str = None,
        txt_record: str = None,
        vpcid: str = None,
        vswitch_id: str = None,
    ):
        # The public endpoint type. Valid values:
        # 
        # *   **SRV**
        # *   **Normal**
        self.connection_type = connection_type
        # The remaining duration of the classic network endpoint. Unit: seconds.
        self.expired_time = expired_time
        # The IP address of the instance.
        self.ipaddress = ipaddress
        # The connection string of the instance.
        self.network_address = network_address
        # The network type of the instance.
        # 
        # *   **VPC**: virtual private cloud
        # *   **Classic**: classic network
        # *   **Public**: the Internet
        self.network_type = network_type
        # The ID of the mongos node.
        self.node_id = node_id
        # The type of the node. Valid values:
        # 
        # *   **mongos**: mongos node
        # *   **shard**: shard node
        # *   **configserver**: Configserver node
        self.node_type = node_type
        # The port that is used to connect to the instance.
        self.port = port
        # The role of the node. Valid values:
        # 
        # *   Primary
        # *   Secondary
        self.role = role
        # Txt record which can be used to store MongoDB-related meta data, such as version, configuration parameters and etc. With the combination of txt record and other technology, for example SRV record, the MongoDB client can complete the complex service discovery and configuration passing.
        self.txt_record = txt_record
        # The VPC ID of the instance.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vpcid = vpcid
        # The ID of the vSwitch in the VPC.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.role is not None:
            result['Role'] = self.role

        if self.txt_record is not None:
            result['TxtRecord'] = self.txt_record

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TxtRecord') is not None:
            self.txt_record = m.get('TxtRecord')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeShardingNetworkAddressResponseBodyCompatibleConnections(DaraModel):
    def __init__(
        self,
        compatible_connection: List[main_models.DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection] = None,
    ):
        self.compatible_connection = compatible_connection

    def validate(self):
        if self.compatible_connection:
            for v1 in self.compatible_connection:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CompatibleConnection'] = []
        if self.compatible_connection is not None:
            for k1 in self.compatible_connection:
                result['CompatibleConnection'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compatible_connection = []
        if m.get('CompatibleConnection') is not None:
            for k1 in m.get('CompatibleConnection'):
                temp_model = main_models.DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection()
                self.compatible_connection.append(temp_model.from_map(k1))

        return self

class DescribeShardingNetworkAddressResponseBodyCompatibleConnectionsCompatibleConnection(DaraModel):
    def __init__(
        self,
        expired_time: str = None,
        ipaddress: str = None,
        network_address: str = None,
        network_type: str = None,
        port: str = None,
        vpcid: str = None,
        vswitch_id: str = None,
    ):
        # The remaining duration of the classic network endpoint. Unit: seconds.
        self.expired_time = expired_time
        # The IP address of the instance.
        self.ipaddress = ipaddress
        # The endpoint of the instance.
        self.network_address = network_address
        # The network type of the instance.
        # 
        # *   **VPC**: virtual private cloud
        # *   **Classic**: classic network
        # *   **Public**: the Internet
        self.network_type = network_type
        # The port that is used to connect to the instance.
        self.port = port
        # The VPC ID of the instance.
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vpcid = vpcid
        # The ID of the vSwitch in the Virtual Private Cloud (VPC).
        # 
        # >  This parameter is returned when the network type is **VPC**.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.network_address is not None:
            result['NetworkAddress'] = self.network_address

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.port is not None:
            result['Port'] = self.port

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetworkAddress') is not None:
            self.network_address = m.get('NetworkAddress')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

