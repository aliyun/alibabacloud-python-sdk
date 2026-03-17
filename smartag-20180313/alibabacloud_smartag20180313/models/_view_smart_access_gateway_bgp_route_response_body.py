# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ViewSmartAccessGatewayBgpRouteResponseBody(DaraModel):
    def __init__(
        self,
        hold_time: int = None,
        keep_alive: int = None,
        local_as: int = None,
        request_id: str = None,
        router_id: str = None,
        task_states: List[main_models.ViewSmartAccessGatewayBgpRouteResponseBodyTaskStates] = None,
    ):
        # The hold time. Unit: seconds.
        self.hold_time = hold_time
        # The time interval at which keep-alive packets are sent. Unit: seconds.
        self.keep_alive = keep_alive
        # The autonomous system number (ASN) to which the SAG device belongs.
        self.local_as = local_as
        # The request ID.
        self.request_id = request_id
        # The ID of the BGP router.
        self.router_id = router_id
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
        if self.hold_time is not None:
            result['HoldTime'] = self.hold_time

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        if self.local_as is not None:
            result['LocalAs'] = self.local_as

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoldTime') is not None:
            self.hold_time = m.get('HoldTime')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        if m.get('LocalAs') is not None:
            self.local_as = m.get('LocalAs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.ViewSmartAccessGatewayBgpRouteResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class ViewSmartAccessGatewayBgpRouteResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The timestamp when the task was created. Unit: milliseconds.
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

