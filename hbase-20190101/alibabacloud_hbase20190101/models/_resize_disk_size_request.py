# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeDiskSizeRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_disk_size: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The disk size of a single node. Unit: GB.
        # 
        # This parameter is required.
        self.node_disk_size = node_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')

        return self

