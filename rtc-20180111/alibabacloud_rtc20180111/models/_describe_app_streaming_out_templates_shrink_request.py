# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppStreamingOutTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        condition_shrink: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.condition_shrink = condition_shrink
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.condition_shrink is not None:
            result['Condition'] = self.condition_shrink

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Condition') is not None:
            self.condition_shrink = m.get('Condition')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

