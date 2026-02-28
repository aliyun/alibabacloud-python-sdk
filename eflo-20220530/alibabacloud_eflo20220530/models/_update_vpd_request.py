# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVpdRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the VPD instance.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The name of the VPD instance.
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        return self

