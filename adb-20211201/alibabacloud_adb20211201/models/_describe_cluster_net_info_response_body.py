# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNetInfoResponseBody(DaraModel):
    def __init__(
        self,
        cluster_network_type: str = None,
        items: main_models.DescribeClusterNetInfoResponseBodyItems = None,
        request_id: str = None,
    ):
        # The network type of the cluster. Only the Virtual Private Cloud (VPC) network type is supported. **VPC** is returned.
        self.cluster_network_type = cluster_network_type
        # The queried network information about the cluster.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_network_type is not None:
            result['ClusterNetworkType'] = self.cluster_network_type

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetworkType') is not None:
            self.cluster_network_type = m.get('ClusterNetworkType')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeClusterNetInfoResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterNetInfoResponseBodyItems(DaraModel):
    def __init__(
        self,
        address: List[main_models.DescribeClusterNetInfoResponseBodyItemsAddress] = None,
    ):
        self.address = address

    def validate(self):
        if self.address:
            for v1 in self.address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Address'] = []
        if self.address is not None:
            for k1 in self.address:
                result['Address'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address = []
        if m.get('Address') is not None:
            for k1 in m.get('Address'):
                temp_model = main_models.DescribeClusterNetInfoResponseBodyItemsAddress()
                self.address.append(temp_model.from_map(k1))

        return self

class DescribeClusterNetInfoResponseBodyItemsAddress(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        connection_string_prefix: str = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        ports: main_models.DescribeClusterNetInfoResponseBodyItemsAddressPorts = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the cluster.
        # 
        # *   If NetType is set to VPC, the VPC endpoint of the cluster is returned.
        # *   If NetType is set to Public, the public endpoint of the cluster is returned.
        self.connection_string = connection_string
        # The prefix of the endpoint.
        # 
        # *   If NetType is set to VPC, the prefix of the VPC endpoint is returned.
        # *   If NetType is set to Public, the prefix of the public endpoint is returned.
        self.connection_string_prefix = connection_string_prefix
        # The IP address of the endpoint.
        # 
        # *   If NetType is set to VPC, the private IP address of the cluster is returned.
        # *   If NetType is set to Public, the public IP address of the cluster is returned.
        self.ipaddress = ipaddress
        # The network type of the cluster. Valid values:
        # 
        # *   **Public**: Internet.
        # *   **VPC**: VPC.
        self.net_type = net_type
        # The port number that is used to connect to the cluster. **3306** is returned.
        self.port = port
        # The ports.
        self.ports = ports
        # The VPC ID.
        # 
        # >  If NetType is set to Public, an empty string is returned.
        self.vpcid = vpcid
        # The vSwitch ID of the cluster.
        # 
        # >  If NetType is set to Public, an empty string is returned.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.ports:
            self.ports.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.ports is not None:
            result['Ports'] = self.ports.to_map()

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Ports') is not None:
            temp_model = main_models.DescribeClusterNetInfoResponseBodyItemsAddressPorts()
            self.ports = temp_model.from_map(m.get('Ports'))

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeClusterNetInfoResponseBodyItemsAddressPorts(DaraModel):
    def __init__(
        self,
        ports: List[main_models.DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts] = None,
    ):
        self.ports = ports

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts()
                self.ports.append(temp_model.from_map(k1))

        return self

class DescribeClusterNetInfoResponseBodyItemsAddressPortsPorts(DaraModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
    ):
        # The port.
        self.port = port
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**
        # *   **http**
        # *   **https**
        # *   **mysql**
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

