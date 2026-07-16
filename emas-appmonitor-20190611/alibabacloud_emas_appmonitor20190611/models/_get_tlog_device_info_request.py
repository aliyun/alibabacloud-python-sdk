# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTlogDeviceInfoRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
        os: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.device_id = device_id
        # This parameter is required.
        self.os = os

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

        if self.os is not None:
            result['Os'] = self.os

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        return self

