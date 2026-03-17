# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagPortListResponseBody(DaraModel):
    def __init__(
        self,
        ports: List[main_models.DescribeSagPortListResponseBodyPorts] = None,
        request_id: str = None,
        task_states: List[main_models.DescribeSagPortListResponseBodyTaskStates] = None,
    ):
        # The list of the port information.
        self.ports = ports
        # The ID of the request.
        self.request_id = request_id
        # The state of the query task.
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
                temp_model = main_models.DescribeSagPortListResponseBodyPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagPortListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagPortListResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code. 200 indicates that the query task is successful.
        self.error_code = error_code
        # The error message. Successful indicates that the query task is successful.
        self.error_message = error_message
        # Asynchronous task states:
        # 
        # *   **Initialized**: The query task is initialized.
        # *   **Offline**: The SAG device is disconnected from Alibaba Cloud and Alibaba Cloud has not assigned the query task to the SAG device. When the SAG device is connected to Alibaba Cloud, Alibaba Cloud continues to assign the query task to the SAG device.
        # *   **Succeed**: Alibaba Cloud has assigned the query task to the SAG device.
        # *   **Processing**: Alibaba Cloud is assigning the query task to the SAG device.
        # *   **VersionNotSupport**: not supported by the current version of the SAG device.
        # *   **BuildRequestError**: not supported by the control and management center in the cloud.
        # *   **HardwareError**: Alibaba Cloud failed to assign the query task to the SAG device because the SAG device is faulty.
        # *   **TaskNotExist**: The query task does not exist.
        # *   **OfflineNotConfiged**: The SAG device is disconnected from Alibaba Cloud and Alibaba Cloud has not assigned the query task to the SAG device. When the SAG device is connected to Alibaba Cloud, Alibaba Cloud does not assign the query task to the SAG device.
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

class DescribeSagPortListResponseBodyPorts(DaraModel):
    def __init__(
        self,
        mac: str = None,
        port_name: str = None,
        role: str = None,
        status: str = None,
    ):
        # The Mac address of the port.
        self.mac = mac
        # The name of the port.
        self.port_name = port_name
        # Port role:
        # 
        # *   **NONE**: No role is assigned to the port.
        # *   **WAN**: The port is used as a WAN port. The WAN port supports a Dynamic Host Configuration Protocol (DHCP) client, PPPoE, or a static IP address to access the Internet.
        # *   **LAN**: The port is used as a LAN port. The LAN port supports a DHCP server or a static IP address to connect to a local terminal or switch.
        # *   **ECC**: The port is used as a leased line port to connect to a leased line.
        # *   **MGT**: The port is used as the management port.
        self.role = role
        # Port states:
        # 
        # *   **Up**: The port is enabled.
        # *   **Down**: The port is disabled.
        # *   **Unavailable**: The SAG device is disconnected from Alibaba Cloud.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mac is not None:
            result['Mac'] = self.mac

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

