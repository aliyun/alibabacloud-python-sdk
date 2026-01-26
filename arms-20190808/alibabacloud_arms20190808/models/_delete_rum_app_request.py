# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRumAppRequest(DaraModel):
    def __init__(
        self,
        app_group: str = None,
        app_id: str = None,
        real_region_id: str = None,
        region_id: str = None,
    ):
        # The group where the application resides.
        self.app_group = app_group
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The region where the application resides. You can leave this parameter empty or set it to China East 2 Finance.
        self.real_region_id = real_region_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group is not None:
            result['AppGroup'] = self.app_group

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.real_region_id is not None:
            result['RealRegionId'] = self.real_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroup') is not None:
            self.app_group = m.get('AppGroup')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('RealRegionId') is not None:
            self.real_region_id = m.get('RealRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

