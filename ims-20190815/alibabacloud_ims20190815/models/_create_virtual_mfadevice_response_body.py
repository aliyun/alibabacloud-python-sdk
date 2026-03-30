# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class CreateVirtualMFADeviceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_mfadevice: main_models.CreateVirtualMFADeviceResponseBodyVirtualMFADevice = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the MFA device.
        self.virtual_mfadevice = virtual_mfadevice

    def validate(self):
        if self.virtual_mfadevice:
            self.virtual_mfadevice.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.virtual_mfadevice is not None:
            result['VirtualMFADevice'] = self.virtual_mfadevice.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VirtualMFADevice') is not None:
            temp_model = main_models.CreateVirtualMFADeviceResponseBodyVirtualMFADevice()
            self.virtual_mfadevice = temp_model.from_map(m.get('VirtualMFADevice'))

        return self

class CreateVirtualMFADeviceResponseBodyVirtualMFADevice(DaraModel):
    def __init__(
        self,
        base_32string_seed: str = None,
        qrcode_png: str = None,
        serial_number: str = None,
    ):
        # The key of the MFA device.
        self.base_32string_seed = base_32string_seed
        # The Base64-encoded QR code of the key.
        self.qrcode_png = qrcode_png
        # The serial number of the MFA device.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_32string_seed is not None:
            result['Base32StringSeed'] = self.base_32string_seed

        if self.qrcode_png is not None:
            result['QRCodePNG'] = self.qrcode_png

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base32StringSeed') is not None:
            self.base_32string_seed = m.get('Base32StringSeed')

        if m.get('QRCodePNG') is not None:
            self.qrcode_png = m.get('QRCodePNG')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

