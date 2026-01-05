# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentShrinkRequest(DaraModel):
    def __init__(
        self,
        render_template: bool = None,
        values_shrink: str = None,
    ):
        self.render_template = render_template
        self.values_shrink = values_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.render_template is not None:
            result['RenderTemplate'] = self.render_template

        if self.values_shrink is not None:
            result['Values'] = self.values_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderTemplate') is not None:
            self.render_template = m.get('RenderTemplate')

        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')

        return self

