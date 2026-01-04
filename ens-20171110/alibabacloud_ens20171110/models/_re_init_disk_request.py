# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReInitDiskRequest(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        image_id: str = None,
    ):
        # The ID of the disk to be initialized. You can initialize only one disk at a time.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The ID of the image to use to create the instance.
        # 
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        return self

