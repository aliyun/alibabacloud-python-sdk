# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeMultiZoneClusterDiskSizeRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        core_disk_size: int = None,
        log_disk_size: int = None,
    ):
        # The ID of the multi-zone instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The disk size of core nodes. The value must be greater than the current disk size and must be a multiple of 40. Unit: GB. Maximum value: 64000.
        self.core_disk_size = core_disk_size
        # The disk size of log nodes. The value must be greater than the current disk size of log nodes and must be a multiple of 40. Unit: GB. Maximum value: 8000.
        self.log_disk_size = log_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size

        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')

        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')

        return self

