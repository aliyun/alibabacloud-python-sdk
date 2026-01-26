# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCmsInstancesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        type_filter: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.region_id = region_id
        # The type of the cloud service integration. Valid values:
        # 
        # *   direct: self-monitoring
        # *   cms: Hybrid Cloud Monitoring
        self.type_filter = type_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type_filter is not None:
            result['TypeFilter'] = self.type_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TypeFilter') is not None:
            self.type_filter = m.get('TypeFilter')

        return self

