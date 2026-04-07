# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTableThemeRequest(DaraModel):
    def __init__(
        self,
        project_id: int = None,
        theme_id: int = None,
    ):
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The ID of the theme.
        # 
        # This parameter is required.
        self.theme_id = theme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        return self

