# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteImagesShrinkRequest(DaraModel):
    def __init__(
        self,
        image_ids_shrink: str = None,
    ):
        # The IDs of the images.
        # 
        # This parameter is required.
        self.image_ids_shrink = image_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')

        return self

