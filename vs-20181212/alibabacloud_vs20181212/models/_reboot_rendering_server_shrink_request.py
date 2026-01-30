# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootRenderingServerShrinkRequest(DaraModel):
    def __init__(
        self,
        rendering_instance_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.rendering_instance_ids_shrink = rendering_instance_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rendering_instance_ids_shrink is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceIds') is not None:
            self.rendering_instance_ids_shrink = m.get('RenderingInstanceIds')

        return self

