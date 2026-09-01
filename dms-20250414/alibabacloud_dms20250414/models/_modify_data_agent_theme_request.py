# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataAgentThemeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        theme_id: str = None,
        theme_name: str = None,
    ):
        # The description of the theme. Maximum length: 255 characters. A value of null indicates that the field is not modified. An empty string clears the field.
        self.description = description
        # The business identifier of the theme.
        self.theme_id = theme_id
        # The display name of the theme. Maximum length: 64 characters. A value of null indicates that the field is not modified. An empty string clears the field.
        self.theme_name = theme_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.theme_name is not None:
            result['ThemeName'] = self.theme_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('ThemeName') is not None:
            self.theme_name = m.get('ThemeName')

        return self

