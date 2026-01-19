# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteImageCacheRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        image_cache_id: str = None,
        region_id: str = None,
    ):
        self.force = force
        # This parameter is required.
        self.image_cache_id = image_cache_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

