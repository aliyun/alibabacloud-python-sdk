# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVirtualBridgeRequest(DaraModel):
    def __init__(
        self,
        bridge_id: str = None,
        region_id: str = None,
    ):
        # The virtual bridge ID.
        # 
        # This parameter is required.
        self.bridge_id = bridge_id
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
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
        if self.bridge_id is not None:
            result['BridgeId'] = self.bridge_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BridgeId') is not None:
            self.bridge_id = m.get('BridgeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

