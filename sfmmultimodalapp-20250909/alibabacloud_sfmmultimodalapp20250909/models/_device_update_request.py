# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeviceUpdateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_name: str = None,
        remark: str = None,
        status: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.device_name = device_name
        self.remark = remark
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

