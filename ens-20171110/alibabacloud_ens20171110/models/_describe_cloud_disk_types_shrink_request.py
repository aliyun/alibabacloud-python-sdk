# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudDiskTypesShrinkRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids_shrink: str = None,
    ):
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The edge nodes.
        self.ens_region_ids_shrink = ens_region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids_shrink is not None:
            result['EnsRegionIds'] = self.ens_region_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids_shrink = m.get('EnsRegionIds')

        return self

