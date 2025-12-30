# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiRtcAuthCodeDTO(DaraModel):
    def __init__(
        self,
        activated_time: str = None,
        auth_code: str = None,
        creation_time: str = None,
        device_id: str = None,
        license: str = None,
        license_item_id: str = None,
        modification_time: str = None,
        status: int = None,
        type: int = None,
    ):
        self.activated_time = activated_time
        self.auth_code = auth_code
        self.creation_time = creation_time
        self.device_id = device_id
        self.license = license
        self.license_item_id = license_item_id
        self.modification_time = modification_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activated_time is not None:
            result['ActivatedTime'] = self.activated_time

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.license is not None:
            result['License'] = self.license

        if self.license_item_id is not None:
            result['LicenseItemId'] = self.license_item_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivatedTime') is not None:
            self.activated_time = m.get('ActivatedTime')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('License') is not None:
            self.license = m.get('License')

        if m.get('LicenseItemId') is not None:
            self.license_item_id = m.get('LicenseItemId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

