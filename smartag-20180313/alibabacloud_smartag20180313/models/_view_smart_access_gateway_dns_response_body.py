# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ViewSmartAccessGatewayDnsResponseBody(DaraModel):
    def __init__(
        self,
        master_dns: str = None,
        request_id: str = None,
        slave_dns: str = None,
        task_states: List[main_models.ViewSmartAccessGatewayDnsResponseBodyTaskStates] = None,
    ):
        # The IP address of the primary DNS server.
        self.master_dns = master_dns
        # The request ID.
        self.request_id = request_id
        # The IP address of the secondary DNS server.
        self.slave_dns = slave_dns
        # The status of the task.
        self.task_states = task_states

    def validate(self):
        if self.task_states:
            for v1 in self.task_states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_dns is not None:
            result['MasterDns'] = self.master_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterDns') is not None:
            self.master_dns = m.get('MasterDns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.ViewSmartAccessGatewayDnsResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class ViewSmartAccessGatewayDnsResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        # 
        # The value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The error code. A value of 200 indicates that the task is successful.
        self.error_code = error_code
        # The error message. A value of Successful indicates that the task is successful.
        self.error_message = error_message
        # The status of the asynchronous task. Valid values:
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

