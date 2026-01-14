# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceInfoRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        ds: str = None,
        factory_id: str = None,
    ):
        # The ID of the device.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The time string in the YYYY-mm-dd format.
        # 
        # This parameter is required.
        self.ds = ds
        # The ID of the site.
        # 
        # This parameter is required.
        self.factory_id = factory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.ds is not None:
            result['ds'] = self.ds

        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('ds') is not None:
            self.ds = m.get('ds')

        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        return self

