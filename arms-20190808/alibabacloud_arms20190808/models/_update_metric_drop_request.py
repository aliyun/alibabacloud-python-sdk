# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetricDropRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        metric_drop: str = None,
        region_id: str = None,
    ):
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The list of discarded metrics. Specify one metric name in each line.
        self.metric_drop = metric_drop
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.metric_drop is not None:
            result['MetricDrop'] = self.metric_drop

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MetricDrop') is not None:
            self.metric_drop = m.get('MetricDrop')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

