# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAdvancedMonitorStateRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sag_id: str = None,
    ):
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.sag_id = sag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        return self

