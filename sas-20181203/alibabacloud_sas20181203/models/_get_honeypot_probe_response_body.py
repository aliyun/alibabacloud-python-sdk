# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetHoneypotProbeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHoneypotProbeResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The information about the probe.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHoneypotProbeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHoneypotProbeResponseBodyData(DaraModel):
    def __init__(
        self,
        arp: bool = None,
        can_listen_ip_list: List[str] = None,
        cidr_list: List[str] = None,
        control_node: main_models.GetHoneypotProbeResponseBodyDataControlNode = None,
        cpu_load: float = None,
        deploy_time: int = None,
        display_name: str = None,
        honey_pot_probe_scan_port: main_models.GetHoneypotProbeResponseBodyDataHoneyPotProbeScanPort = None,
        honeypot_probe_bind_list: List[main_models.GetHoneypotProbeResponseBodyDataHoneypotProbeBindList] = None,
        host_ip: str = None,
        listen_ip_list: List[str] = None,
        memory_load: float = None,
        os_type: str = None,
        ping: bool = None,
        probe_id: str = None,
        probe_type: str = None,
        probe_version: str = None,
        proxy_ip: str = None,
        status: int = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        # Indicates whether address resolution protocol (ARP) is enabled for the check type.
        self.arp = arp
        # An array consisting of the IP addresses that can be monitored.
        self.can_listen_ip_list = can_listen_ip_list
        # The CIDR blocks of the probe deployed in a virtual private cloud (VPC).
        self.cidr_list = cidr_list
        # The information about the management node.
        self.control_node = control_node
        # The CPU utilization.
        self.cpu_load = cpu_load
        # The time when the probe was deployed.
        self.deploy_time = deploy_time
        # The name of the probe.
        self.display_name = display_name
        # The ports that the honeypot monitors.
        self.honey_pot_probe_scan_port = honey_pot_probe_scan_port
        # The honeypots that are bound to the probe.
        self.honeypot_probe_bind_list = honeypot_probe_bind_list
        # The IP address of the server on which the probe is deployed.
        self.host_ip = host_ip
        # An array consisting of the IP addresses that can be monitored.
        self.listen_ip_list = listen_ip_list
        # The memory usage.
        self.memory_load = memory_load
        # The operating system of the server on which the probe is deployed. Valid values:
        # 
        # *   windows
        # *   linux
        self.os_type = os_type
        # Indicates whether ping is enabled for the check type.
        self.ping = ping
        # The ID of the probe.
        self.probe_id = probe_id
        # The type of the probe. Valid values:
        # 
        # *   **host_probe**: host probe
        # *   **vpc_black_hole_probe**: virtual private cloud (VPC) probe
        self.probe_type = probe_type
        # The version of the probe.
        self.probe_version = probe_version
        # The IP address of the proxy server.
        self.proxy_ip = proxy_ip
        # The status of the probe. Valid values:
        # 
        # *   **installed**: installed
        # *   **install_failed**: installation failed
        # *   **online**: online
        # *   **offline**: offline
        # *   **unnormal**: abnormal
        # *   **unprobe**: unauthorized
        # *   **uninstalling**: being uninstalled
        # *   **uninstalled**: uninstalled
        # *   **uninstall_failed**: uninstallation failed
        # *   **not_exist**: not installed
        self.status = status
        # The UUID of the asset on which the host probe is deployed.
        self.uuid = uuid
        # The ID of the VPC in which the probe is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        if self.control_node:
            self.control_node.validate()
        if self.honey_pot_probe_scan_port:
            self.honey_pot_probe_scan_port.validate()
        if self.honeypot_probe_bind_list:
            for v1 in self.honeypot_probe_bind_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arp is not None:
            result['Arp'] = self.arp

        if self.can_listen_ip_list is not None:
            result['CanListenIpList'] = self.can_listen_ip_list

        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list

        if self.control_node is not None:
            result['ControlNode'] = self.control_node.to_map()

        if self.cpu_load is not None:
            result['CpuLoad'] = self.cpu_load

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.honey_pot_probe_scan_port is not None:
            result['HoneyPotProbeScanPort'] = self.honey_pot_probe_scan_port.to_map()

        result['HoneypotProbeBindList'] = []
        if self.honeypot_probe_bind_list is not None:
            for k1 in self.honeypot_probe_bind_list:
                result['HoneypotProbeBindList'].append(k1.to_map() if k1 else None)

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.listen_ip_list is not None:
            result['ListenIpList'] = self.listen_ip_list

        if self.memory_load is not None:
            result['MemoryLoad'] = self.memory_load

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.ping is not None:
            result['Ping'] = self.ping

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        if self.probe_version is not None:
            result['ProbeVersion'] = self.probe_version

        if self.proxy_ip is not None:
            result['ProxyIp'] = self.proxy_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arp') is not None:
            self.arp = m.get('Arp')

        if m.get('CanListenIpList') is not None:
            self.can_listen_ip_list = m.get('CanListenIpList')

        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')

        if m.get('ControlNode') is not None:
            temp_model = main_models.GetHoneypotProbeResponseBodyDataControlNode()
            self.control_node = temp_model.from_map(m.get('ControlNode'))

        if m.get('CpuLoad') is not None:
            self.cpu_load = m.get('CpuLoad')

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('HoneyPotProbeScanPort') is not None:
            temp_model = main_models.GetHoneypotProbeResponseBodyDataHoneyPotProbeScanPort()
            self.honey_pot_probe_scan_port = temp_model.from_map(m.get('HoneyPotProbeScanPort'))

        self.honeypot_probe_bind_list = []
        if m.get('HoneypotProbeBindList') is not None:
            for k1 in m.get('HoneypotProbeBindList'):
                temp_model = main_models.GetHoneypotProbeResponseBodyDataHoneypotProbeBindList()
                self.honeypot_probe_bind_list.append(temp_model.from_map(k1))

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('ListenIpList') is not None:
            self.listen_ip_list = m.get('ListenIpList')

        if m.get('MemoryLoad') is not None:
            self.memory_load = m.get('MemoryLoad')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Ping') is not None:
            self.ping = m.get('Ping')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        if m.get('ProbeVersion') is not None:
            self.probe_version = m.get('ProbeVersion')

        if m.get('ProxyIp') is not None:
            self.proxy_ip = m.get('ProxyIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetHoneypotProbeResponseBodyDataHoneypotProbeBindList(DaraModel):
    def __init__(
        self,
        bind_id: str = None,
        bind_port_list: List[main_models.GetHoneypotProbeResponseBodyDataHoneypotProbeBindListBindPortList] = None,
        honeypot_id: str = None,
        service_ip_list: List[str] = None,
        status: int = None,
    ):
        # The unique ID of the honeypot that is bound to the probe.
        self.bind_id = bind_id
        # The ports that are bound to the probe.
        self.bind_port_list = bind_port_list
        # The honeypot ID.
        self.honeypot_id = honeypot_id
        # The IP addresses that are monitored.
        self.service_ip_list = service_ip_list
        # The status of the honeypot that is bound to the probe. Valid values:
        # 
        # *   **1**: abnormal
        # *   **3**: normal
        self.status = status

    def validate(self):
        if self.bind_port_list:
            for v1 in self.bind_port_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        result['BindPortList'] = []
        if self.bind_port_list is not None:
            for k1 in self.bind_port_list:
                result['BindPortList'].append(k1.to_map() if k1 else None)

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.service_ip_list is not None:
            result['ServiceIpList'] = self.service_ip_list

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        self.bind_port_list = []
        if m.get('BindPortList') is not None:
            for k1 in m.get('BindPortList'):
                temp_model = main_models.GetHoneypotProbeResponseBodyDataHoneypotProbeBindListBindPortList()
                self.bind_port_list.append(temp_model.from_map(k1))

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('ServiceIpList') is not None:
            self.service_ip_list = m.get('ServiceIpList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetHoneypotProbeResponseBodyDataHoneypotProbeBindListBindPortList(DaraModel):
    def __init__(
        self,
        bind_port: bool = None,
        end_port: int = None,
        err: str = None,
        fixed: bool = None,
        id: int = None,
        msg: str = None,
        proto: str = None,
        start_port: int = None,
        status: int = None,
        target_port: int = None,
    ):
        # Indicates whether the port is bound.
        self.bind_port = bind_port
        # The end port on which the probe monitors.
        self.end_port = end_port
        # The error that is returned if an error occurred in the port of the honeypot that is bound to the probe.
        self.err = err
        # Indicates whether the port is a fixed port.
        self.fixed = fixed
        # The unique ID of the port binding record.
        self.id = id
        # The error message that is returned if an error occurred in the port of the honeypot that is bound to the probe.
        self.msg = msg
        # The type of the protocol.
        self.proto = proto
        # The start port on which the probe monitors.
        self.start_port = start_port
        # The status of the port of the honeypot that is bound to the probe. Valid values:
        # 
        # *   **1**: abnormal
        # *   **3**: normal
        self.status = status
        # The destination port.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_port is not None:
            result['BindPort'] = self.bind_port

        if self.end_port is not None:
            result['EndPort'] = self.end_port

        if self.err is not None:
            result['Err'] = self.err

        if self.fixed is not None:
            result['Fixed'] = self.fixed

        if self.id is not None:
            result['Id'] = self.id

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.start_port is not None:
            result['StartPort'] = self.start_port

        if self.status is not None:
            result['Status'] = self.status

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindPort') is not None:
            self.bind_port = m.get('BindPort')

        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')

        if m.get('Err') is not None:
            self.err = m.get('Err')

        if m.get('Fixed') is not None:
            self.fixed = m.get('Fixed')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

class GetHoneypotProbeResponseBodyDataHoneyPotProbeScanPort(DaraModel):
    def __init__(
        self,
        id: int = None,
        ports: str = None,
        probe_id: str = None,
        service_ip_list: List[str] = None,
        status: int = None,
    ):
        # The unique ID of the service that is monitored.
        self.id = id
        # The ports that are monitored.
        self.ports = ports
        # The ID of the probe.
        self.probe_id = probe_id
        # The IP addresses that are monitored.
        self.service_ip_list = service_ip_list
        # The monitoring status. Valid values:
        # 
        # *   **1**: abnormal
        # *   **3**: normal
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.service_ip_list is not None:
            result['ServiceIpList'] = self.service_ip_list

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ServiceIpList') is not None:
            self.service_ip_list = m.get('ServiceIpList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetHoneypotProbeResponseBodyDataControlNode(DaraModel):
    def __init__(
        self,
        ecs_instance_id: str = None,
        node_id: str = None,
        node_name: str = None,
    ):
        # The instance ID of the management node.
        self.ecs_instance_id = ecs_instance_id
        # The ID of the management node.
        self.node_id = node_id
        # The name of the management node.
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

