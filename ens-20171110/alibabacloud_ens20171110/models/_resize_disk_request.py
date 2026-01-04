# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeDiskRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        new_size: str = None,
    ):
        # The ID of the disk that you want to resize.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The size of the disk that you want to resize. Unit: GiB.
        # 
        # This parameter is required.
        self.new_size = new_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.new_size is not None:
            result['NewSize'] = self.new_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')

        return self

