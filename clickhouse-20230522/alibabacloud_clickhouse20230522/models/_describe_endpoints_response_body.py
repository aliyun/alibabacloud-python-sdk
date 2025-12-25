# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeEndpointsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeEndpointsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEndpointsResponseBodyData(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.DescribeEndpointsResponseBodyDataEndpoints] = None,
        instance_network_type: str = None,
    ):
        # The details of the endpoints.
        self.endpoints = endpoints
        # The network type of the cluster. Valid values:
        # 
        # *   **VPC**
        # *   **PUBLIC**
        self.instance_network_type = instance_network_type

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeEndpointsResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        return self

class DescribeEndpointsResponseBodyDataEndpoints(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        ipaddress: str = None,
        net_type: str = None,
        ports: List[main_models.DescribeEndpointsResponseBodyDataEndpointsPorts] = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # *   VPC
        # *   PUBLIC
        self.net_type = net_type
        # The details of the ports.
        self.ports = ports
        # The state of the cluster.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id

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
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeEndpointsResponseBodyDataEndpointsPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

class DescribeEndpointsResponseBodyDataEndpointsPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port used to connect to the cluster. Valid values:
        # 
        # *   8123: This value is returned when the value of Protocol is HttpPort.
        # *   8443: This value is returned when the value of Protocol is HttpsPort.
        # *   9000: This value is returned when the value of Protocol is TcpPort.
        self.port = port
        # The protocol type. Valid values:
        # 
        # *   HttpPort
        # *   HttpsPort
        # *   TcpPort
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

