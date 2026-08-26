# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataAgentThemeRequest(DaraModel):
    def __init__(
        self,
        theme_id: str = None,
    ):
        # The business ID of the theme.
        self.theme_id = theme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        return self

