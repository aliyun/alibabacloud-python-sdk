# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateSceneKeyRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        expire_time: int = None,
        region_id: str = None,
        scene: str = None,
    ):
        # The cloud desktop ID.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The validity period of the key, in hours. A value of 0 indicates that the key never expires. If this parameter is not specified, the default server value is used.
        self.expire_time = expire_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The scenario name.
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

