# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagHaResponseBody(DaraModel):
    def __init__(
        self,
        mode: str = None,
        ports: List[main_models.DescribeSagHaResponseBodyPorts] = None,
        request_id: str = None,
        task_states: List[main_models.DescribeSagHaResponseBodyTaskStates] = None,
    ):
        # The HA mode. Valid values:
        # 
        # *   **NONE**: HA is disabled.
        # *   **STATIC**: static HA is enabled.
        # *   **DYNAMIC**: dynamic HA is enabled.
        self.mode = mode
        # The information about the port.
        self.ports = ports
        # The ID of the request.
        self.request_id = request_id
        # The information about the query task.
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
        if self.mode is not None:
            result['Mode'] = self.mode

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
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeSagHaResponseBodyPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagHaResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagHaResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code returned for a query task. The 200 error code indicates that the query task is successful.
        self.error_code = error_code
        # The error message returned for a query task. The Successful error message indicates that the query task is successful.
        self.error_message = error_message
        # The status of the query task. Valid values:
        # 
        # *   **Initialized**: The query task has been initialized.
        # *   **Offline**: The query task is not dispatched because the SAG device is disconnected from Alibaba Cloud. The task will be dispatched after the SAG device is connected to Alibaba Cloud.
        # *   **Succeed**: The query task has been dispatched.
        # *   **Processing**: The query task is being dispatched.
        # *   **VersionNotSupport**: The current version of the SAG device does not support query tasks.
        # *   **BuildRequestError**: The SAG control system does not support query tasks.
        # *   **HardwareError**: The query task failed to be dispatched due to device errors.
        # *   **TaskNotExist**: The query task does not exist.
        # *   **OfflineNotConfiged**: The query task is not dispatched because the SAG device is disconnected from Alibaba Cloud. The task will not be dispatched after the device is connected to Alibaba Cloud.
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

class DescribeSagHaResponseBodyPorts(DaraModel):
    def __init__(
        self,
        port_name: str = None,
        virtual_ip: str = None,
    ):
        # The name of the port.
        self.port_name = port_name
        # The virtual IP address of the SAG device.
        self.virtual_ip = virtual_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.virtual_ip is not None:
            result['VirtualIp'] = self.virtual_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('VirtualIp') is not None:
            self.virtual_ip = m.get('VirtualIp')

        return self

