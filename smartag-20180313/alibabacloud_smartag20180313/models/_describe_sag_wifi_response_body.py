# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagWifiResponseBody(DaraModel):
    def __init__(
        self,
        authentication_type: str = None,
        bandwidth: str = None,
        channel: str = None,
        encrypt_algorithm: str = None,
        is_auth: str = None,
        is_broadcast: str = None,
        is_enable: str = None,
        request_id: str = None,
        ssid: str = None,
        task_states: List[main_models.DescribeSagWifiResponseBodyTaskStates] = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   **NONE**: authentication is disabled.
        # *   **WPA-PSK**: WPA-PSK authentication is enabled.
        # *   **WPA2-PSK**: WPA2-PSK authentication is enabled.
        self.authentication_type = authentication_type
        # The bandwidth of the Wi-Fi channel. Valid values:
        # 
        # *   **Automatic**
        # *   **20 HMz**
        # *   **40 MHz**
        self.bandwidth = bandwidth
        # The Wi-Fi channel.
        self.channel = channel
        # The encryption algorithm.
        # 
        # *   **AUTO**: automatically selects the encryption algorithm.
        # *   **TKIP**: uses the Temporal Key Integrity Protocol (TKIP).
        # *   **AES**: uses the Advanced Encryption Standard authorized by Wi-Fi®.
        self.encrypt_algorithm = encrypt_algorithm
        # Indicates whether wireless security is enabled.
        # 
        # *   **True**: wireless security is enabled.
        # *   **False**: wireless security is disabled.
        self.is_auth = is_auth
        # Indicates whether broadcast over Wi-Fi is enabled. Valid values:
        # 
        # *   **True**: broadcast is enabled.
        # *   **False**: broadcast is disabled.
        self.is_broadcast = is_broadcast
        # Indicates whether wireless connections are enabled. Valid values:
        # 
        # *   **True**: wireless connections are enabled.
        # *   **False**: wireless connections are disabled.
        self.is_enable = is_enable
        # The ID of the request.
        self.request_id = request_id
        # The service set identifier (SSID) of the Wi-Fi network.
        self.ssid = ssid
        # The information about the query task.
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
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth

        if self.is_broadcast is not None:
            result['IsBroadcast'] = self.is_broadcast

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ssid is not None:
            result['Ssid'] = self.ssid

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')

        if m.get('IsBroadcast') is not None:
            self.is_broadcast = m.get('IsBroadcast')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagWifiResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagWifiResponseBodyTaskStates(DaraModel):
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

