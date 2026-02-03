# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteNetworkPathRequest(DaraModel):
    def __init__(
        self,
        network_path_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of network paths.
        # 
        # This parameter is required.
        self.network_path_ids = network_path_ids
        # The region ID of the network path that you want to delete.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_path_ids is not None:
            result['NetworkPathIds'] = self.network_path_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPathIds') is not None:
            self.network_path_ids = m.get('NetworkPathIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

