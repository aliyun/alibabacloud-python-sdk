# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitorResourceQuotaAttributeRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        show_used: bool = None,
    ):
        self.region_id = region_id
        # Specifies whether to return information about used quotas. Valid values:
        # 
        # *   true (default): yes
        # *   false: no
        self.show_used = show_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_used is not None:
            result['ShowUsed'] = self.show_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowUsed') is not None:
            self.show_used = m.get('ShowUsed')

        return self

