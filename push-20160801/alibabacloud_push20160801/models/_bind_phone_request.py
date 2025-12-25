# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindPhoneRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
        phone_number: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        return self

