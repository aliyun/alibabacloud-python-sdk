# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagWanListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_states: List[main_models.DescribeSagWanListResponseBodyTaskStates] = None,
        wans: List[main_models.DescribeSagWanListResponseBodyWans] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of and information about the query task.
        self.task_states = task_states
        # The settings of the WAN port.
        self.wans = wans

    def validate(self):
        if self.task_states:
            for v1 in self.task_states:
                 if v1:
                    v1.validate()
        if self.wans:
            for v1 in self.wans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskStates'] = []
        if self.task_states is not None:
            for k1 in self.task_states:
                result['TaskStates'].append(k1.to_map() if k1 else None)

        result['Wans'] = []
        if self.wans is not None:
            for k1 in self.wans:
                result['Wans'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_states = []
        if m.get('TaskStates') is not None:
            for k1 in m.get('TaskStates'):
                temp_model = main_models.DescribeSagWanListResponseBodyTaskStates()
                self.task_states.append(temp_model.from_map(k1))

        self.wans = []
        if m.get('Wans') is not None:
            for k1 in m.get('Wans'):
                temp_model = main_models.DescribeSagWanListResponseBodyWans()
                self.wans.append(temp_model.from_map(k1))

        return self

class DescribeSagWanListResponseBodyWans(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        gateway: str = None,
        ip: str = None,
        iptype: str = None,
        isp: str = None,
        mask: str = None,
        port_name: str = None,
        priority: int = None,
        traffic_state: str = None,
        username: str = None,
        weight: int = None,
    ):
        # The bandwidth cap of the WAN port. Unit: Mbit/s.
        self.band_width = band_width
        # The IP address of the gateway.
        self.gateway = gateway
        # The IP address of the WAN port.
        self.ip = ip
        # The connection type of the WAN port. Valid values:
        # 
        # *   **DHCP**: The WAN port connects to the Internet through an IP address that is dynamically assigned by the Dynamic Host Configuration Protocol (DHCP) server.
        # *   **STATIC**: The WAN port connects to the Internet through a static IP address.
        # *   **PPPOE**: The WAN port connects to the Internet through dial-up connections.
        self.iptype = iptype
        # The Internet service provider (ISP) used by the WAN port.
        # 
        # *   **CT**: China Telecom
        # *   **CM**: China Mobile
        # *   **CU**: China Unicom
        # *   **Other**: Other ISPs
        self.isp = isp
        # The subnet mask of the WAN port IP address.
        self.mask = mask
        # The number of the WAN port.
        self.port_name = port_name
        # The priority of the WAN port.
        # 
        # Valid values: **-1** and **1 to 50**. A smaller number represents a higher priority.
        # 
        # >  A value of **-1** indicates that the WAN port is not used to forward network traffic.
        self.priority = priority
        # The status of data transfer on the WAN port. Valid values:
        # 
        # *   **active**: The WAN port is the active port for data transfer.
        # *   **standby**: The WAN port is a standby port. If the active port is down, data transfer is switched to the WAN port.
        self.traffic_state = traffic_state
        # The username of the PPPoE account.
        self.username = username
        # The weight of the WAN port.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.ip is not None:
            result['IP'] = self.ip

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state

        if self.username is not None:
            result['Username'] = self.username

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeSagWanListResponseBodyTaskStates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        state: str = None,
    ):
        # The time when the query task was created.
        self.create_time = create_time
        # The error code returned to the query task. A value of 200 indicates that the query task is successful.
        self.error_code = error_code
        # The error message returned to the query task. A value of Successful indicates that the query task is successful.
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

