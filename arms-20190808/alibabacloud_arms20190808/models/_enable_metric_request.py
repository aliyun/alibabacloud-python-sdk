# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableMetricRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        drop_metric: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The metric name.
        self.drop_metric = drop_metric
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.drop_metric is not None:
            result['DropMetric'] = self.drop_metric

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DropMetric') is not None:
            self.drop_metric = m.get('DropMetric')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

