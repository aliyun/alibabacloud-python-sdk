# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVirtualMFADeviceRequest(DaraModel):
    def __init__(
        self,
        virtual_mfadevice_name: str = None,
    ):
        # This parameter is required.
        self.virtual_mfadevice_name = virtual_mfadevice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.virtual_mfadevice_name is not None:
            result['VirtualMFADeviceName'] = self.virtual_mfadevice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VirtualMFADeviceName') is not None:
            self.virtual_mfadevice_name = m.get('VirtualMFADeviceName')

        return self

