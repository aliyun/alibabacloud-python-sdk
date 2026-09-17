# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeRenderingInstanceImageShrinkRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        rendering_instance_ids_shrink: str = None,
    ):
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The list of cloud application service instance IDs. A maximum of 100 IDs can be specified.
        # 
        # This parameter is required.
        self.rendering_instance_ids_shrink = rendering_instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.rendering_instance_ids_shrink is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RenderingInstanceIds') is not None:
            self.rendering_instance_ids_shrink = m.get('RenderingInstanceIds')

        return self

