# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagRouteProtocolOspfResponseBody(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        area_type: str = None,
        authentication_type: str = None,
        dead_time: int = None,
        hello_time: int = None,
        md_5key: str = None,
        md_5key_id: int = None,
        request_id: str = None,
        router_id: str = None,
        task_states: List[main_models.DescribeSagRouteProtocolOspfResponseBodyTaskStates] = None,
    ):
        # The ID of the OSPF area.
        self.area_id = area_id
        # The type of the OSPF area.
        # 
        # >  Only the NSSA area type is supported.
        self.area_type = area_type
        # The authentication type. Valid values:
        # 
        # *   **NONE**: Authentication is disabled.
        # *   **CLEARTEXT**: plaintext authentication
        # *   **MD5**: MD5 authentication
        self.authentication_type = authentication_type
        # The timeout period of connections between OSPF peers.
        # 
        # Unit: seconds.
        self.dead_time = dead_time
        # The time interval at which Hello packets are sent.
        # 
        # Unit: seconds.
        self.hello_time = hello_time
        # The MD5 key value.
        self.md_5key = md_5key
        # The ID of the MD5 key.
        self.md_5key_id = md_5key_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the router that has OSPF enabled.
        self.router_id = router_id
        # The status of the query task.
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
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.area_type is not None:
            result['AreaType'] = self.area_type

        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.dead_time is not None:
            result['DeadTime'] = self.dead_time

        if self.hello_time is not None:
            result['HelloTime'] = self.hello_time

        if self.md_5key is not None:
            result['Md5Key'] = self.md_5key

        if self.md_5key_id is not None:
            result['Md5KeyId'] = self.md_5key_id

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
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('AreaType') is not None:
            self.area_type = m.get('AreaType')

        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('DeadTime') is not None:
            self.dead_time = m.get('DeadTime')

        if m.get('HelloTime') is not None:
            self.hello_time = m.get('HelloTime')

        if m.get('Md5Key') is not None:
            self.md_5key = m.get('Md5Key')

        if m.get('Md5KeyId') is not None:
            self.md_5key_id = m.get('Md5KeyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagRouteProtocolOspfResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagRouteProtocolOspfResponseBodyTaskStates(DaraModel):
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
        # The state of the query task. Valid values:
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

