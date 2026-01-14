# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteIpSetsRequest(DaraModel):
    def __init__(
        self,
        ip_set_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of the acceleration regions that you want to delete.
        # 
        # This parameter is required.
        self.ip_set_ids = ip_set_ids
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
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
        if self.ip_set_ids is not None:
            result['IpSetIds'] = self.ip_set_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpSetIds') is not None:
            self.ip_set_ids = m.get('IpSetIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

