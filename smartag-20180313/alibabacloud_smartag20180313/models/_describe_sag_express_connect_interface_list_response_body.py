# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagExpressConnectInterfaceListResponseBody(DaraModel):
    def __init__(
        self,
        interfaces: List[main_models.DescribeSagExpressConnectInterfaceListResponseBodyInterfaces] = None,
        request_id: str = None,
        task_states: List[main_models.DescribeSagExpressConnectInterfaceListResponseBodyTaskStates] = None,
    ):
        # The information about the port.
        self.interfaces = interfaces
        # The ID of the request.
        self.request_id = request_id
        # The state of the query task.
        self.task_states = task_states

    def validate(self):
        if self.interfaces:
            for v1 in self.interfaces:
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
        result['Interfaces'] = []
        if self.interfaces is not None:
            for k1 in self.interfaces:
                result['Interfaces'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.interfaces = []
        if m.get('Interfaces') is not None:
            for k1 in m.get('Interfaces'):
                temp_model = main_models.DescribeSagExpressConnectInterfaceListResponseBodyInterfaces()
                self.interfaces.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagExpressConnectInterfaceListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagExpressConnectInterfaceListResponseBodyTaskStates(DaraModel):
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
        # The error message. A value of Successful indicates that the query task is successful.
        self.error_message = error_message
        # The state of the asynchronous query task. Valid values:
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

class DescribeSagExpressConnectInterfaceListResponseBodyInterfaces(DaraModel):
    def __init__(
        self,
        ip: str = None,
        mask: str = None,
        vlan: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The subnet mask of the IP address of the port.
        self.mask = mask
        # The VLAN ID.
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

