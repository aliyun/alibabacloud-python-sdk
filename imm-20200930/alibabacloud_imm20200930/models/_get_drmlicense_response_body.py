# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDRMLicenseResponseBody(DaraModel):
    def __init__(
        self,
        device_info: str = None,
        license: str = None,
        request_id: str = None,
        states: int = None,
    ):
        self.device_info = device_info
        self.license = license
        self.request_id = request_id
        self.states = states

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info

        if self.license is not None:
            result['License'] = self.license

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.states is not None:
            result['States'] = self.states

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')

        if m.get('License') is not None:
            self.license = m.get('License')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('States') is not None:
            self.states = m.get('States')

        return self

