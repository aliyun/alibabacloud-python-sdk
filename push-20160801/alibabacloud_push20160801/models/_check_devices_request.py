# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDevicesRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        device_ids: str = None,
    ):
        # The AppKey value.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The unique identifier for each device in the push service. Each ID is 32 characters long and contains only digits and lowercase letters. Separate multiple IDs with commas. You can check up to 100 devices per request.
        # 
        # This parameter is required.
        self.device_ids = device_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')

        return self

