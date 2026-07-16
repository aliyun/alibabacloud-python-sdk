# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchCaptureRenderingInstanceScreenshotRequest(DaraModel):
    def __init__(
        self,
        quality: int = None,
        rendering_instance_ids: List[str] = None,
    ):
        # The image quality. Valid values: 1 to 100.
        self.quality = quality
        # The list of instance IDs. A maximum of 100 instance IDs can be specified.
        # 
        # This parameter is required.
        self.rendering_instance_ids = rendering_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quality is not None:
            result['Quality'] = self.quality

        if self.rendering_instance_ids is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('RenderingInstanceIds') is not None:
            self.rendering_instance_ids = m.get('RenderingInstanceIds')

        return self

