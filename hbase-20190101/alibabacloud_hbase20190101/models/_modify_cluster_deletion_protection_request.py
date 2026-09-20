# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClusterDeletionProtectionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        protection: bool = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # - true: Enables deletion protection. The cluster cannot be deleted when deletion protection is enabled.
        # - false: Disables deletion protection. The cluster can be deleted.
        # 
        # This parameter is required.
        self.protection = protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.protection is not None:
            result['Protection'] = self.protection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Protection') is not None:
            self.protection = m.get('Protection')

        return self

