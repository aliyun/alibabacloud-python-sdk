# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListReleaseVersionsRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        iaas_type: str = None,
        region_id: str = None,
    ):
        # The type of the cluster.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The type of the IaaS resource.
        self.iaas_type = iaas_type
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
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.iaas_type is not None:
            result['IaasType'] = self.iaas_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('IaasType') is not None:
            self.iaas_type = m.get('IaasType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

