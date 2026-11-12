# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagLanListResponseBody(DaraModel):
    def __init__(
        self,
        lans: List[main_models.DescribeSagLanListResponseBodyLans] = None,
        request_id: str = None,
        task_states: List[main_models.DescribeSagLanListResponseBodyTaskStates] = None,
    ):
        # The list of LAN port information.
        self.lans = lans
        # The ID of the request.
        self.request_id = request_id
        # The status information of the query task.
        self.task_states = task_states

    def validate(self):
        if self.lans:
            for v1 in self.lans:
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
        result['Lans'] = []
        if self.lans is not None:
            for k1 in self.lans:
                result['Lans'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lans = []
        if m.get('Lans') is not None:
            for k1 in m.get('Lans'):
                temp_model = main_models.DescribeSagLanListResponseBodyLans()
                self.lans.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagLanListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        return self

class DescribeSagLanListResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code. 200 indicates that the query task succeeded.
        self.error_code = error_code
        # The error message. Successful indicates that the query task succeeded.
        self.error_message = error_message
        # The status of the asynchronous task. Valid values:
        # - **Initialized**: The query task is initialized.
        # - **Offline**: The Smart Access Gateway device is offline and the query task is not delivered. The task will be delivered after the device comes online.
        # - **Succeed**: The query task was delivered successfully.
        # - **Processing**: The query task is being delivered.
        # - **VersionNotSupport**: The current version of the Smart Access Gateway device does not support this operation.
        # - **BuildRequestError**: The request is not supported by the management system.
        # - **HardwareError**: The query task failed to be delivered due to a device error.
        # - **TaskNotExist**: The query task does not exist.
        # - **OfflineNotConfiged**: The Smart Access Gateway device is offline and the query task is not delivered. The task will not be delivered even after the device comes online.
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

class DescribeSagLanListResponseBodyLans(DaraModel):
    def __init__(
        self,
        end_ip: str = None,
        ip: str = None,
        iptype: str = None,
        lease: str = None,
        mask: str = None,
        port_name: str = None,
        start_ip: str = None,
    ):
        # The end address of the DHCP address pool.
        self.end_ip = end_ip
        # The IP address of the LAN port.
        self.ip = ip
        # The connection type of the LAN port. Valid values:
        # 
        # **DHCP**: Dynamic IP. Uses the DHCP protocol to dynamically assign IP addresses to connected devices.
        # 
        # **STATIC**: Static IP. Statically specifies the IP address of the LAN port.
        self.iptype = iptype
        # The DHCP lease time. Unit: minutes.
        self.lease = lease
        # The subnet mask.
        self.mask = mask
        # The name of the port.
        self.port_name = port_name
        # The start IP address of the DHCP address pool.
        self.start_ip = start_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip

        if self.ip is not None:
            result['IP'] = self.ip

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.lease is not None:
            result['Lease'] = self.lease

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.start_ip is not None:
            result['StartIp'] = self.start_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Lease') is not None:
            self.lease = m.get('Lease')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')

        return self

