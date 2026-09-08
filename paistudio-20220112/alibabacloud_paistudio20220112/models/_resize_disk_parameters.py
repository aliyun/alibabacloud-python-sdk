# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeDiskParameters(DaraModel):
    def __init__(
        self,
        new_disk_size: str = None,
    ):
        # The target disk capacity after the change.
        self.new_disk_size = new_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_disk_size is not None:
            result['NewDiskSize'] = self.new_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDiskSize') is not None:
            self.new_disk_size = m.get('NewDiskSize')

        return self

