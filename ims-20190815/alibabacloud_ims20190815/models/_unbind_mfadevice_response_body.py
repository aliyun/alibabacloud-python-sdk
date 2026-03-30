# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class UnbindMFADeviceResponseBody(DaraModel):
    def __init__(
        self,
        mfadevice: main_models.UnbindMFADeviceResponseBodyMFADevice = None,
        request_id: str = None,
    ):
        # The information about the MFA device.
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
            temp_model = main_models.UnbindMFADeviceResponseBodyMFADevice()
            self.mfadevice = temp_model.from_map(m.get('MFADevice'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UnbindMFADeviceResponseBodyMFADevice(DaraModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        # The serial number of the MFA device.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

