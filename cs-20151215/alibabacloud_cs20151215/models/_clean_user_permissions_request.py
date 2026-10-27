# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CleanUserPermissionsRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        force: bool = None,
    ):
        # The list of cluster IDs. If you specify this list, only the KubeConfig credentials and RBAC permissions of the specified user in the listed clusters are cleared.
        self.cluster_ids = cluster_ids
        # Specifies whether to force delete the specified KubeConfig. Valid values:
        # - false (default): Checks whether there are cluster access records within the last seven days before deleting the KubeConfig. If such records exist or cannot be found, the deletion is not allowed.
        # - true: Force deletes the KubeConfig without checking cluster access records.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

