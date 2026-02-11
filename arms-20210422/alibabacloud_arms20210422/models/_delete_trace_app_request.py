# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTraceAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        pid: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.pid = pid
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

