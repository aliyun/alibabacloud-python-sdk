# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocParserResultShrinkRequest(DaraModel):
    def __init__(
        self,
        exclude_fields_shrink: str = None,
        id: str = None,
        layout_num: int = None,
        layout_step_size: int = None,
    ):
        self.exclude_fields_shrink = exclude_fields_shrink
        self.id = id
        self.layout_num = layout_num
        self.layout_step_size = layout_step_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_fields_shrink is not None:
            result['ExcludeFields'] = self.exclude_fields_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.layout_num is not None:
            result['LayoutNum'] = self.layout_num

        if self.layout_step_size is not None:
            result['LayoutStepSize'] = self.layout_step_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeFields') is not None:
            self.exclude_fields_shrink = m.get('ExcludeFields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LayoutNum') is not None:
            self.layout_num = m.get('LayoutNum')

        if m.get('LayoutStepSize') is not None:
            self.layout_step_size = m.get('LayoutStepSize')

        return self

