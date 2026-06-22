# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupClientsRequest(DaraModel):
    def __init__(
        self,
        support_region_id: str = None,
    ):
        # The region supported by the anti-ransomware feature. You can call [DescribeSupportRegion](~~DescribeSupportRegion~~) to query the regions supported by the anti-ransomware feature.
        # 
        # This parameter is required.
        self.support_region_id = support_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.support_region_id is not None:
            result['SupportRegionId'] = self.support_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportRegionId') is not None:
            self.support_region_id = m.get('SupportRegionId')

        return self

