# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNetworkReachableAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        network_reachable_analysis_ids_shrink: str = None,
        region_id: str = None,
    ):
        # The IDs of the tasks for analyzing network reachability.
        # 
        # This parameter is required.
        self.network_reachable_analysis_ids_shrink = network_reachable_analysis_ids_shrink
        # The ID of the region for which you want to delete a task for analyzing network reachability.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_reachable_analysis_ids_shrink is not None:
            result['NetworkReachableAnalysisIds'] = self.network_reachable_analysis_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisIds') is not None:
            self.network_reachable_analysis_ids_shrink = m.get('NetworkReachableAnalysisIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

