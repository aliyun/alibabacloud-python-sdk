# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteImagesRequest(DaraModel):
    def __init__(
        self,
        image_ids: List[str] = None,
    ):
        # The IDs of the images.
        # 
        # This parameter is required.
        self.image_ids = image_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        return self

