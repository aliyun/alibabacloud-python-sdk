# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class GetUserMFAInfoResponseBody(DaraModel):
    def __init__(
        self,
        mfadevice: main_models.GetUserMFAInfoResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        # The information about the MFA device that is bound to the RAM user.
        self.mfadevice = mfadevice
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mfadevice:
            self.mfadevice.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mfadevice is not None:
            result['MFADevice'] = self.mfadevice.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFADevice') is not None:
            temp_model = main_models.GetUserMFAInfoResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m.get('MFADevice'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetUserMFAInfoResponseBodyMFADevice(DaraModel):
    def __init__(
        self,
        serial_number: str = None,
        type: str = None,
    ):
        # The serial number of the MFA device.
        self.serial_number = serial_number
        # The type of the MFA device. Valid values:
        # 
        # *   VMFA: virtual MFA device.
        # *   U2F: Universal 2nd Factor (U2F) security key.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

