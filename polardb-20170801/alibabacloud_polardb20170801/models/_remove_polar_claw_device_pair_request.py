# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemovePolarClawDevicePairRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        device_id: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The device ID.
        # 
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        return self

