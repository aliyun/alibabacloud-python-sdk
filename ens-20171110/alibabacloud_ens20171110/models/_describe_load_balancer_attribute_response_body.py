# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        address_type: str = None,
        backend_servers: List[main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers] = None,
        bandwidth: int = None,
        create_time: str = None,
        end_time: str = None,
        ens_region_id: str = None,
        listener_ports: List[str] = None,
        listener_ports_and_protocols: List[main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols] = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        network_id: str = None,
        pay_type: str = None,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        # The IP address that the Edge Load Balancer (ELB) instance uses to provide services.
        self.address = address
        # The IP version of the ELB instance. Valid values: ipv4 and ipv6.
        self.address_ipversion = address_ipversion
        self.address_type = address_type
        # The list of backend servers.
        self.backend_servers = backend_servers
        # The peak bandwidth of the ELB. The default value is -1, which indicates that the bandwidth is unlimited.
        self.bandwidth = bandwidth
        # The time when the ELB instance was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the ELB instance was disabled.
        self.end_time = end_time
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The frontend ports that are used by the ELB instance.
        self.listener_ports = listener_ports
        # The frontend ports and protocols that are used by the ELB instance.
        self.listener_ports_and_protocols = listener_ports_and_protocols
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the ELB instance.
        self.load_balancer_name = load_balancer_name
        # The specifications of the ELB instance.
        self.load_balancer_spec = load_balancer_spec
        # The status of the ELB instance. Valid values:
        # 
        # *   **Active** (default): The listener for the instance can forward the received traffic based on the rule.
        # *   **InActive**: The listener for the instance does not forward the received traffic.
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        # The ID of the network.
        self.network_id = network_id
        # The billing method. Valid values:
        # 
        # *   **PrePaid**: subscription.
        # *   **PostPaid**: pay-as-you-go. Only this billing method is supported.
        self.pay_type = pay_type
        # The ID of the request.
        self.request_id = request_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.backend_servers:
            for v1 in self.backend_servers:
                 if v1:
                    v1.validate()
        if self.listener_ports_and_protocols:
            for v1 in self.listener_ports_and_protocols:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k1 in self.backend_servers:
                result['BackendServers'].append(k1.to_map() if k1 else None)

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.listener_ports is not None:
            result['ListenerPorts'] = self.listener_ports

        result['ListenerPortsAndProtocols'] = []
        if self.listener_ports_and_protocols is not None:
            for k1 in self.listener_ports_and_protocols:
                result['ListenerPortsAndProtocols'].append(k1.to_map() if k1 else None)

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k1 in m.get('BackendServers'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyBackendServers()
                self.backend_servers.append(temp_model.from_map(k1))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ListenerPorts') is not None:
            self.listener_ports = m.get('ListenerPorts')

        self.listener_ports_and_protocols = []
        if m.get('ListenerPortsAndProtocols') is not None:
            for k1 in m.get('ListenerPortsAndProtocols'):
                temp_model = main_models.DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols()
                self.listener_ports_and_protocols.append(temp_model.from_map(k1))

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeLoadBalancerAttributeResponseBodyListenerPortsAndProtocols(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        description: str = None,
        forward_port: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
    ):
        # The backend port that is used by the ELB instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The description of the listener.
        self.description = description
        # The destination listening port to which requests are forwarded.
        self.forward_port = forward_port
        # Indicates whether the listener is enabled.
        self.listener_forward = listener_forward
        # The listener port of the instance.
        self.listener_port = listener_port
        # The listener protocol of the instance.
        self.listener_protocol = listener_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port

        if self.description is not None:
            result['Description'] = self.description

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        return self

class DescribeLoadBalancerAttributeResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: str = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The IP address of the backend server.
        self.ip = ip
        # The port that is used by the backend server.
        self.port = port
        # The ID of the backend server.
        self.server_id = server_id
        # The type of backend server.
        self.type = type
        # The weight of the backend server.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

