# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPassThroughAuthInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
    ):
        self.app_id = app_id
        self.device_name = device_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        return self

