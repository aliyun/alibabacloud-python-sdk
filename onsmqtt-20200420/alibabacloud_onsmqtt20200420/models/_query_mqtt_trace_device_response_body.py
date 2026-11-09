# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryMqttTraceDeviceResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_info_list: List[main_models.QueryMqttTraceDeviceResponseBodyDeviceInfoList] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The details of the device activity entries.
        self.device_info_list = device_info_list
        # The maximum number of device activity entries displayed per page.
        self.page_size = page_size
        # A common parameter. Each request has a unique ID that is active for troubleshooting and locating issues.
        self.request_id = request_id
        # The total number of device activity entries returned.
        self.total = total

    def validate(self):
        if self.device_info_list:
            for v1 in self.device_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k1 in self.device_info_list:
                result['DeviceInfoList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k1 in m.get('DeviceInfoList'):
                temp_model = main_models.QueryMqttTraceDeviceResponseBodyDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryMqttTraceDeviceResponseBodyDeviceInfoList(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        channel_id: str = None,
        time: str = None,
    ):
        # The device action. Valid values:
        # 
        # - **connect**: The client requests a connection to the server.
        # 
        # - **close**: The TCP connection is closed.
        # 
        # - **disconnect**: The client requests to disconnect from the server.
        self.action = action
        # The return code of the device action. Valid values:
        # 
        # - **mqtt.trace.action.connect**: returned when the device action is **connect**.
        # 
        # - **mqtt.trace.action.close**: returned when the device action is **close**.
        # 
        # - **mqtt.trace.action.disconnect**: returned when the device action is **disconnect**.
        self.action_code = action_code
        # The description of the device action. Valid values:
        # 
        # - **accepted**: The server accepts the connection request from the client.
        # 
        # - **not authorized**: The TCP connection is closed because the permission verification of the instance accessed by the client fails.
        # 
        # - **clientId conflict**: The TCP connection is closed because of a client ID conflict.
        # 
        # - **resource auth failed**: The TCP connection is closed because the permission verification of the topic or group ID resource accessed by the client fails.
        # 
        # - **no heart**: The TCP connection is closed because no heartbeat is detected from the client.
        # 
        # - **closed by client**: The TCP connection is closed because of a client exception.
        # 
        # - **disconnected by client**: The client requests to disconnect.
        # 
        # - **invalid param**: The TCP connection is closed because of invalid request parameters.
        # 
        # - **Socket IOException**: The TCP connection is closed because of network jitter or packet loss.
        self.action_info = action_info
        # The connection identifier of the device.
        self.channel_id = channel_id
        # The time when the device action occurred.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_code is not None:
            result['ActionCode'] = self.action_code

        if self.action_info is not None:
            result['ActionInfo'] = self.action_info

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')

        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

