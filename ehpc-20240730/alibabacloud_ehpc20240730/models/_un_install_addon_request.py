# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnInstallAddonRequest(DaraModel):
    def __init__(
        self,
        addon_id: str = None,
        cluster_id: str = None,
    ):
        # The addon ID.
        # 
        # This parameter is required.
        self.addon_id = addon_id
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
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
        if self.addon_id is not None:
            result['AddonId'] = self.addon_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonId') is not None:
            self.addon_id = m.get('AddonId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

