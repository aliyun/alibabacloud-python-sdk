# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CleanUserPermissionsShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_ids_shrink: str = None,
        force: bool = None,
    ):
        # The cluster IDs. If you specify a list of cluster IDs, only the kubeconfig files and RBAC permissions of the clusters that belong to the current user in the list are revoked.
        self.cluster_ids_shrink = cluster_ids_shrink
        # Specifies whether to forcefully delete the specified kubeconfig files. Valid values:
        # 
        # *   false (default): checks the cluster access records within the previous seven days before deleting the kubeconfig files. The kubeconfig files are not deleted if cluster access records are found or fail to be retrieved.
        # *   true: forcefully deletes the kubeconfig files without checking the cluster access records.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids_shrink is not None:
            result['ClusterIds'] = self.cluster_ids_shrink

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids_shrink = m.get('ClusterIds')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

