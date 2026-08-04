# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetDeviceBasicInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetDeviceBasicInfoResponseBodyResult = None,
    ):
        # Error code returned. A value of 200 indicates that the call succeeded.
        self.code = code
        # Return result of invoking this API.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Detailed information returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetDeviceBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetDeviceBasicInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        firmware_version: str = None,
        mac: str = None,
        name: str = None,
        sn: str = None,
    ):
        # Firmware version of the device.
        self.firmware_version = firmware_version
        # MAC address of the device.
        self.mac = mac
        # Name of the device.
        self.name = name
        # SN information of the device.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.name is not None:
            result['Name'] = self.name

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

