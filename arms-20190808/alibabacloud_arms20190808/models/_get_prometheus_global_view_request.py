# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPrometheusGlobalViewRequest(DaraModel):
    def __init__(
        self,
        global_view_cluster_id: str = None,
        region_id: str = None,
    ):
        # The ID of the global aggregation instance.
        # 
        # This parameter is required.
        self.global_view_cluster_id = global_view_cluster_id
        # The region ID.
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
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

