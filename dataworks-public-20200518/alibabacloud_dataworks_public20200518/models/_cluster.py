# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Cluster(DaraModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        cluster_id: int = None,
    ):
        # The unique business identifier of the cluster.
        # 
        # This parameter is required.
        self.cluster_biz_id = cluster_biz_id
        # The ID of the cluster associated with DataWorks.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

