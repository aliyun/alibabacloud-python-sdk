# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetworkReachableAnalysisRequest(DaraModel):
    def __init__(
        self,
        network_reachable_analysis_id: str = None,
        region_id: str = None,
    ):
        # The ID of the task for analyzing network reachability. You can call the **CreateNetworkRearchableAnalysis** operation to obtain the ID of the task for analyzing network reachability.
        # 
        # This parameter is required.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The ID of the region for which you want to obtain the result of network reachability analysis.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

