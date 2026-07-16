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
        # The list of port information.
        self.ports = ports
        # The request ID.
        self.request_id = request_id
        # The query task status.
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
        # The error code. A value of 200 indicates that the query task succeeded.
        self.error_code = error_code
        # The error message. A value of Successful indicates that the query task succeeded.
        self.error_message = error_message
        # The status of the asynchronous task. Valid values:
        # 
        # - **Initialized**: The query task is initialized.
        # - **Offline**: The Smart Access Gateway device is offline and the query task has not been delivered. The task will be delivered after the device comes online.
        # - **Succeed**: The query task is delivered.
        # - **Processing**: The query task is being delivered.
        # - **VersionNotSupport**: The current version of the Smart Access Gateway device does not support this operation.
        # - **BuildRequestError**: The China Cloud Management Platform does not support this operation.
        # - **HardwareError**: The query task failed to be delivered due to a device error.
        # - **TaskNotExist**: The query task does not exist.
        # - **OfflineNotConfiged**: The Smart Access Gateway device is offline and the query task has not been delivered. The task will not be delivered even after the device comes online.
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
        # The neighbor IP address.
        self.neighbor_ip = neighbor_ip
        # The port name.
        self.port_name = port_name
        # The autonomous system number of the peer BGP network.
        self.remote_as = remote_as
        # The IP address of the peer.
        self.remote_ip = remote_ip
        # The routable protocol of the port. Valid values:
        # 
        # - **STATIC**: static routable protocol.
        # - **OSPF**: OSPF dynamic routable protocol.
        # - **BGP**: BGP dynamic routable protocol.
        self.route_protocol = route_protocol
        # The port status. Valid values:
        # 
        # - **UP**: The port is enabled.
        # - **DOWN**: The port is disabled.
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

