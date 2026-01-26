# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFilesystemsAssociatedHpnZonesShrinkRequest(DaraModel):
    def __init__(
        self,
        filesystems_shrink: str = None,
        region_id: str = None,
    ):
        self.filesystems_shrink = filesystems_shrink
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filesystems_shrink is not None:
            result['Filesystems'] = self.filesystems_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filesystems') is not None:
            self.filesystems_shrink = m.get('Filesystems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

