# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagPortRouteProtocolListResponseBody(DaraModel):
    def __init__(
        self,
        ports: List[main_models.DescribeSagPortRouteProtocolListResponseBodyPorts] = None,
        request_id: str = None,
        task_states: List[main_models.DescribeSagPortRouteProtocolListResponseBodyTaskStates] = None,
    ):
        # An array that consists of the details of the port.
        self.ports = ports
        # The ID of the request.
        self.request_id = request_id
        # The details about the status of the query task.
        self.task_states = task_states

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.task_states:
            for v1 in self.task_states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeSagPortRouteProtocolListResponseBodyPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagPortRouteProtocolListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagPortRouteProtocolListResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code returned. A value of 200 indicates that the query task is successful.
        self.error_code = error_code
        # The error message returned. A value of Successful indicates that the query task is successful.
        self.error_message = error_message
        # The status of the query task. Valid values:
        # 
        # *   **Initialized**: The query task is initialized.
        # *   **Offline**: The SAG device is disconnected from Alibaba Cloud and Alibaba Cloud has not assigned the query task to the SAG device. After the SAG device is connected to Alibaba Cloud, Alibaba Cloud assigns the query task to the SAG device.
        # *   **Succeed**: Alibaba Cloud has assigned the query task to the SAG device.
        # *   **Processing**: Alibaba Cloud is assigning the query task to the SAG device.
        # *   **VersionNotSupport**: The query task is not supported by the current version of the SAG device.
        # *   **BuildRequestError**: The query task is not supported by the controller of the SAG device.
        # *   **HardwareError**: Alibaba Cloud failed to assign the query task to the SAG device because the SAG device is faulty.
        # *   **TaskNotExist**: The query task does not exist.
        # *   **OfflineNotConfiged**: The SAG device is disconnected from Alibaba Cloud and Alibaba Cloud has not assigned the query task to the SAG device. Alibaba Cloud does not assign the query task to the SAG device even after the SAG device is connected to Alibaba Cloud.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeSagPortRouteProtocolListResponseBodyPorts(DaraModel):
    def __init__(
        self,
        neighbor_ip: str = None,
        port_name: str = None,
        remote_as: str = None,
        remote_ip: str = None,
        route_protocol: str = None,
        status: str = None,
        vlan: str = None,
    ):
        # The IP address of the neighbor device.
        self.neighbor_ip = neighbor_ip
        # The name of the port.
        self.port_name = port_name
        # The number of the autonomous system (AS) to which the SAG device belongs.
        self.remote_as = remote_as
        # The IP address of the peer device.
        self.remote_ip = remote_ip
        # The routing protocol. Valid values:
        # 
        # *   **STATIC**: static routing protocol
        # *   **OSPF**: Open Shortest Path First protocol (OSPF)
        # *   **BGP**: Border Gateway Protocol (BGP)
        self.route_protocol = route_protocol
        # The status of the port. Valid values:
        # 
        # *   **UP**: The port was enabled.
        # *   **DOWN**: The port was disabled.
        self.status = status
        # The VLAN ID.
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.neighbor_ip is not None:
            result['NeighborIp'] = self.neighbor_ip

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.remote_as is not None:
            result['RemoteAs'] = self.remote_as

        if self.remote_ip is not None:
            result['RemoteIp'] = self.remote_ip

        if self.route_protocol is not None:
            result['RouteProtocol'] = self.route_protocol

        if self.status is not None:
            result['Status'] = self.status

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeighborIp') is not None:
            self.neighbor_ip = m.get('NeighborIp')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('RemoteAs') is not None:
            self.remote_as = m.get('RemoteAs')

        if m.get('RemoteIp') is not None:
            self.remote_ip = m.get('RemoteIp')

        if m.get('RouteProtocol') is not None:
            self.route_protocol = m.get('RouteProtocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

