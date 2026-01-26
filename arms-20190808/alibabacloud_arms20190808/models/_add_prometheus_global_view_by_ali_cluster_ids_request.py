# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPrometheusGlobalViewByAliClusterIdsRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: str = None,
        group_name: str = None,
        product_code: str = None,
        region_id: str = None,
    ):
        # The IDs of clusters. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids
        # The name of the global aggregation instance.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The identifier to identify the service if custom dashboards are created for the specified clusters.
        self.product_code = product_code
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
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

