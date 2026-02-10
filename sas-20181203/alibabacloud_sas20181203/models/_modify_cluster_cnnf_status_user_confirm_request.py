# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyClusterCnnfStatusUserConfirmRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        user_confirm: bool = None,
    ):
        # The cluster IDs.
        self.cluster_ids = cluster_ids
        # Specifies whether to fix the blocking status of the cluster. Valid values:
        # 
        # *   true: yes
        # *   false: no
        self.user_confirm = user_confirm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.user_confirm is not None:
            result['UserConfirm'] = self.user_confirm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('UserConfirm') is not None:
            self.user_confirm = m.get('UserConfirm')

        return self

