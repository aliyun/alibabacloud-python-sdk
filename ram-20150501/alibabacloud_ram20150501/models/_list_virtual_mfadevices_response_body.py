# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListVirtualMFADevicesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_mfadevices: main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevices = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        if self.virtual_mfadevices:
            self.virtual_mfadevices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virtual_mfadevices is not None:
            result['VirtualMFADevices'] = self.virtual_mfadevices.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirtualMFADevices') is not None:
            temp_model = main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevices()
            self.virtual_mfadevices = temp_model.from_map(m.get('VirtualMFADevices'))

        return self

class ListVirtualMFADevicesResponseBodyVirtualMFADevices(DaraModel):
    def __init__(
        self,
        virtual_mfadevice: List[main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice] = None,
    ):
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            for v1 in self.virtual_mfadevice:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VirtualMFADevice'] = []
        if self.virtual_mfadevice is not None:
            for k1 in self.virtual_mfadevice:
                result['VirtualMFADevice'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_mfadevice = []
        if m.get('VirtualMFADevice') is not None:
            for k1 in m.get('VirtualMFADevice'):
                temp_model = main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice()
                self.virtual_mfadevice.append(temp_model.from_map(k1))

        return self

class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADevice(DaraModel):
    def __init__(
        self,
        activate_date: str = None,
        serial_number: str = None,
        user: main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser = None,
    ):
        self.activate_date = activate_date
        self.serial_number = serial_number
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('User') is not None:
            temp_model = main_models.ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class ListVirtualMFADevicesResponseBodyVirtualMFADevicesVirtualMFADeviceUser(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

