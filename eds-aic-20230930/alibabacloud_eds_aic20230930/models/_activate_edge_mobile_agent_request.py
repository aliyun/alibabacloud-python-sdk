# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActivateEdgeMobileAgentRequest(DaraModel):
    def __init__(
        self,
        device_class: str = None,
        device_id: str = None,
        device_meta: str = None,
        license_key: str = None,
    ):
        # The device form factor. Valid values:
        # - BOX
        # - PHONE
        # - PAD
        # - OTHER
        self.device_class = device_class
        # The unique identifier of the device.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The extended device metadata in JSON format. The string contains information such as fingerprint, deviceModel, and firmwareVersion.
        self.device_meta = device_meta
        # The license key.
        # 
        # This parameter is required.
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_class is not None:
            result['DeviceClass'] = self.device_class

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_meta is not None:
            result['DeviceMeta'] = self.device_meta

        if self.license_key is not None:
            result['LicenseKey'] = self.license_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceMeta') is not None:
            self.device_meta = m.get('DeviceMeta')

        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')

        return self

