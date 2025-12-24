# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetDesktopMaintenanceRequest(DaraModel):
    def __init__(
        self,
        desktop_ids: List[str] = None,
        mode: str = None,
        region_id: str = None,
    ):
        # A list of cloud computer IDs for which you want to set maintenance mode. A maximum of 100 cloud computer IDs are supported.
        # 
        # This parameter is required.
        self.desktop_ids = desktop_ids
        # Enter or exit cloud computer maintenance mode.
        # 
        # Enumerated values:
        # 
        # *   ENTER: The enters the maintenance mode.
        # *   EXIT: The exits the maintenance mode.
        # 
        # This parameter is required.
        self.mode = mode
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
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
        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

