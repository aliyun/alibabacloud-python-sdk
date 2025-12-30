# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActiveAiRtcLicenseRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        device_id: str = None,
        license_item_id: str = None,
    ):
        # The authorization code.
        self.auth_code = auth_code
        # The device ID.
        self.device_id = device_id
        # The batch ID.
        self.license_item_id = license_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.license_item_id is not None:
            result['LicenseItemId'] = self.license_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('LicenseItemId') is not None:
            self.license_item_id = m.get('LicenseItemId')

        return self

