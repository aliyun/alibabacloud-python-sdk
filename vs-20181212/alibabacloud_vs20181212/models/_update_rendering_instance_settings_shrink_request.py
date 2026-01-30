# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRenderingInstanceSettingsShrinkRequest(DaraModel):
    def __init__(
        self,
        rendering_instance_id: str = None,
        settings_shrink: str = None,
    ):
        self.rendering_instance_id = rendering_instance_id
        self.settings_shrink = settings_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.settings_shrink is not None:
            result['Settings'] = self.settings_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('Settings') is not None:
            self.settings_shrink = m.get('Settings')

        return self

