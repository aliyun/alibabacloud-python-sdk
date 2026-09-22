# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitAiAppScanRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        commodity_code: str = None,
        region_id: str = None,
    ):
        # The channel type.
        self.channel = channel
        # The commodity code.
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

