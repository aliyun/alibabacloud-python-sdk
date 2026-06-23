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
        # The list of cluster IDs. If this list is specified, only the KubeConfig credentials and RBAC permissions of the current user in the specified clusters are cleaned up.
        self.cluster_ids_shrink = cluster_ids_shrink
        # Specifies whether to force delete the specified KubeConfig. Valid values:
        # - false (default): Before deleting the KubeConfig, the system checks whether cluster access records exist within the last seven days. If access records exist or cannot be retrieved, the deletion is not allowed.
        # - true: Force deletes the KubeConfig without checking cluster access records.
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

