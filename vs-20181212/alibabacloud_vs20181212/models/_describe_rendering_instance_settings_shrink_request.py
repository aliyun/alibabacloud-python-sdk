# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRenderingInstanceSettingsShrinkRequest(DaraModel):
    def __init__(
        self,
        attribute_names_shrink: str = None,
        rendering_instance_id: str = None,
    ):
        self.attribute_names_shrink = attribute_names_shrink
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_names_shrink is not None:
            result['AttributeNames'] = self.attribute_names_shrink

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeNames') is not None:
            self.attribute_names_shrink = m.get('AttributeNames')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

