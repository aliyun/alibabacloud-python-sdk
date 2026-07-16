# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeLangfuseEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeLangfuseEndpointsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
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
            temp_model = main_models.DescribeLangfuseEndpointsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLangfuseEndpointsResponseBodyData(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.DescribeLangfuseEndpointsResponseBodyDataEndpoints] = None,
        instance_network_type: str = None,
    ):
        # The list of endpoints.
        self.endpoints = endpoints
        # The network type of the instance. Valid values:
        # 
        # * **VPC**: virtual private cloud (VPC).
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
                temp_model = main_models.DescribeLangfuseEndpointsResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        return self

class DescribeLangfuseEndpointsResponseBodyDataEndpoints(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        endpoint_name: str = None,
        ipaddress: str = None,
        net_type: str = None,
        ports: List[main_models.DescribeLangfuseEndpointsResponseBodyDataEndpointsPorts] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The endpoint of the instance.
        self.connection_string = connection_string
        # The endpoint name.
        self.endpoint_name = endpoint_name
        # The IP address.
        self.ipaddress = ipaddress
        # The network type of the endpoint. Valid values:
        # 
        # - VPC: VPC.
        # - PUBLIC: Internet.
        self.net_type = net_type
        # The port details.
        self.ports = ports
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id

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
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeLangfuseEndpointsResponseBodyDataEndpointsPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeLangfuseEndpointsResponseBodyDataEndpointsPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The access port. Valid values:
        # 
        # - http: 3000
        self.port = port
        # The protocol type. Valid values:
        # 
        # - http: HTTP port.
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

