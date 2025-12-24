# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDevicesResponseBody(DaraModel):
    def __init__(
        self,
        devices: List[main_models.DescribeDevicesResponseBodyDevices] = None,
        request_id: str = None,
    ):
        # The information about devices that you queried.
        self.devices = devices
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for v1 in self.devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['Devices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.DescribeDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDevicesResponseBodyDevices(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        end_user_list: List[main_models.DescribeDevicesResponseBodyDevicesEndUserList] = None,
    ):
        # The ID of the device. The serial number (SN) of the hardware client or the UUID of the software client.
        self.device_id = device_id
        # The users who are bound to the device.
        self.end_user_list = end_user_list

    def validate(self):
        if self.end_user_list:
            for v1 in self.end_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        result['EndUserList'] = []
        if self.end_user_list is not None:
            for k1 in self.end_user_list:
                result['EndUserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        self.end_user_list = []
        if m.get('EndUserList') is not None:
            for k1 in m.get('EndUserList'):
                temp_model = main_models.DescribeDevicesResponseBodyDevicesEndUserList()
                self.end_user_list.append(temp_model.from_map(k1))

        return self

class DescribeDevicesResponseBodyDevicesEndUserList(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        directory_id: str = None,
        end_user_id: str = None,
        user_type: str = None,
    ):
        # The address of the AD office network.
        self.ad_domain = ad_domain
        # The ID of the convenient office network.
        self.directory_id = directory_id
        # The ID of the user.
        self.end_user_id = end_user_id
        # The account type of the user.
        # 
        # Valid values:
        # 
        # *   AD: enterprise AD account.
        # *   SIMPLE: convenience account
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

