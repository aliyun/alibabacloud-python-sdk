# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelCopyImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        region_id: str = None,
    ):
        # The ID of the new image in the destination region.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the region to which the image is copied.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

