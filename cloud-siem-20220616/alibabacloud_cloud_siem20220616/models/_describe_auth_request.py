# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuthRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region of the threat analysis center. Select a region based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Select this value if your assets are deployed in the Chinese mainland or the China (Hong Kong) region.
        # 
        # - ap-southeast-1: Select this value if your assets are deployed in regions outside the Chinese mainland.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

