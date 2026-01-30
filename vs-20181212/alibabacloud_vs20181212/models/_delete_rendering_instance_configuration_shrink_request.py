# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRenderingInstanceConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        configuration_shrink: str = None,
        rendering_instance_id: str = None,
    ):
        self.configuration_shrink = configuration_shrink
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_shrink is not None:
            result['Configuration'] = self.configuration_shrink

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            self.configuration_shrink = m.get('Configuration')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

