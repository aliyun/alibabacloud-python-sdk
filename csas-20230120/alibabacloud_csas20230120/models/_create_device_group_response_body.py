# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeviceGroupResponseBody(DaraModel):
    def __init__(
        self,
        device_group_id: str = None,
        request_id: str = None,
    ):
        # The device label ID.
        self.device_group_id = device_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

