# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachSharedStoragesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about the shared storage resources that you want to attach to the cluster.
        # 
        # This parameter is required.
        self.shared_storages_shrink = shared_storages_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.shared_storages_shrink is not None:
            result['SharedStorages'] = self.shared_storages_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('SharedStorages') is not None:
            self.shared_storages_shrink = m.get('SharedStorages')

        return self

