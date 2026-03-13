# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20130221 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_type: str = None,
        auto_release_time: int = None,
        backend_servers: main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers = None,
        bandwidth: int = None,
        create_time: str = None,
        create_time_stamp: int = None,
        end_time: str = None,
        end_time_stamp: int = None,
        internet_charge_type: str = None,
        is_public_address: str = None,
        listener_ports: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPorts = None,
        listener_ports_and_protocal: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal = None,
        listener_ports_and_protocol: main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        master_zone_id: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        region_id_alias: str = None,
        request_id: str = None,
        slave_zone_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.address = address
        self.address_type = address_type
        self.auto_release_time = auto_release_time
        self.backend_servers = backend_servers
        self.bandwidth = bandwidth
        self.create_time = create_time
        self.create_time_stamp = create_time_stamp
        self.end_time = end_time
        self.end_time_stamp = end_time_stamp
        self.internet_charge_type = internet_charge_type
        self.is_public_address = is_public_address
        self.listener_ports = listener_ports
        self.listener_ports_and_protocal = listener_ports_and_protocal
        self.listener_ports_and_protocol = listener_ports_and_protocol
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_spec = load_balancer_spec
        self.load_balancer_status = load_balancer_status
        self.master_zone_id = master_zone_id
        self.network_type = network_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.region_id_alias = region_id_alias
        self.request_id = request_id
        self.slave_zone_id = slave_zone_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()
        if self.listener_ports:
            self.listener_ports.validate()
        if self.listener_ports_and_protocal:
            self.listener_ports_and_protocal.validate()
        if self.listener_ports_and_protocol:
            self.listener_ports_and_protocol.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_time_stamp is not None:
            result['EndTimeStamp'] = self.end_time_stamp

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.is_public_address is not None:
            result['IsPublicAddress'] = self.is_public_address

        if self.listener_ports is not None:
            result['ListenerPorts'] = self.listener_ports.to_map()

        if self.listener_ports_and_protocal is not None:
            result['ListenerPortsAndProtocal'] = self.listener_ports_and_protocal.to_map()

        if self.listener_ports_and_protocol is not None:
            result['ListenerPortsAndProtocol'] = self.listener_ports_and_protocol.to_map()

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_id_alias is not None:
            result['RegionIdAlias'] = self.region_id_alias

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slave_zone_id is not None:
            result['SlaveZoneId'] = self.slave_zone_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('BackendServers') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimeStamp') is not None:
            self.end_time_stamp = m.get('EndTimeStamp')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IsPublicAddress') is not None:
            self.is_public_address = m.get('IsPublicAddress')

        if m.get('ListenerPorts') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPorts()
            self.listener_ports = temp_model.from_map(m.get('ListenerPorts'))

        if m.get('ListenerPortsAndProtocal') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal()
            self.listener_ports_and_protocal = temp_model.from_map(m.get('ListenerPortsAndProtocal'))

        if m.get('ListenerPortsAndProtocol') is not None:
            temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol()
            self.listener_ports_and_protocol = temp_model.from_map(m.get('ListenerPortsAndProtocol'))

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIdAlias') is not None:
            self.region_id_alias = m.get('RegionIdAlias')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlaveZoneId') is not None:
            self.slave_zone_id = m.get('SlaveZoneId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocol(DaraModel):
    def __init__(
        self,
        listener_port_and_protocol: List[main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol] = None,
    ):
        self.listener_port_and_protocol = listener_port_and_protocol

    def validate(self):
        if self.listener_port_and_protocol:
            for v1 in self.listener_port_and_protocol:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListenerPortAndProtocol'] = []
        if self.listener_port_and_protocol is not None:
            for k1 in self.listener_port_and_protocol:
                result['ListenerPortAndProtocol'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocol = []
        if m.get('ListenerPortAndProtocol') is not None:
            for k1 in m.get('ListenerPortAndProtocol'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol()
                self.listener_port_and_protocol.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocolListenerPortAndProtocol(DaraModel):
    def __init__(
        self,
        listener_port: int = None,
        listener_protocol: str = None,
    ):
        self.listener_port = listener_port
        self.listener_protocol = listener_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocal(DaraModel):
    def __init__(
        self,
        listener_port_and_protocal: List[main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal] = None,
    ):
        self.listener_port_and_protocal = listener_port_and_protocal

    def validate(self):
        if self.listener_port_and_protocal:
            for v1 in self.listener_port_and_protocal:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListenerPortAndProtocal'] = []
        if self.listener_port_and_protocal is not None:
            for k1 in self.listener_port_and_protocal:
                result['ListenerPortAndProtocal'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener_port_and_protocal = []
        if m.get('ListenerPortAndProtocal') is not None:
            for k1 in m.get('ListenerPortAndProtocal'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal()
                self.listener_port_and_protocal.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocalListenerPortAndProtocal(DaraModel):
    def __init__(
        self,
        listener_port: int = None,
        listener_protocal: str = None,
    ):
        self.listener_port = listener_port
        self.listener_protocal = listener_protocal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocal is not None:
            result['ListenerProtocal'] = self.listener_protocal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocal') is not None:
            self.listener_protocal = m.get('ListenerProtocal')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPorts(DaraModel):
    def __init__(
        self,
        listener_port: List[str] = None,
    ):
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        return self

class DescribeLoadBalancerAttributeResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for v1 in self.backend_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k1 in self.backend_server:
                result['BackendServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k1 in m.get('BackendServer'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerAttributeResponseBodyBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        server_id: str = None,
        weight: int = None,
    ):
        self.server_id = server_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

