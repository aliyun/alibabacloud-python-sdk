# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterMemberRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_member_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The member ID of the ECS instance that you want to remove from the cluster.
        # 
        # This parameter is required.
        self.cluster_member_id = cluster_member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_member_id is not None:
            result['ClusterMemberId'] = self.cluster_member_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterMemberId') is not None:
            self.cluster_member_id = m.get('ClusterMemberId')

        return self

