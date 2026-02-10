# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterSuspEventStatisticsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        from_: str = None,
    ):
        # The ID of the container cluster.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The ID of the request source. Set the value to sas.
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.from_ is not None:
            result['From'] = self.from_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        return self

