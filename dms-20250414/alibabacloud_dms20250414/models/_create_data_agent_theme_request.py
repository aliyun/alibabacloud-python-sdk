# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentThemeRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        file_from: str = None,
        theme_id: str = None,
        theme_name: str = None,
        theme_type: str = None,
    ):
        # The application scenario, which affects filtering when viewing the theme list in the console. Valid values:
        # 
        # - (Recommended) custom: a user-uploaded custom theme with no preset style or information organization structure.
        # - report: a web report that conforms to the DataAgent information organization structure.
        # - (Not supported) infographic: an infographic that conforms to the DataAgent information organization structure.
        self.category = category
        # The description. The value can be up to 255 characters in length.
        self.description = description
        # The file source, which affects the backend logic for determining whether the theme is valid. Valid values:
        # 
        # - upload: uploaded through OSS.
        # - (Not supported) public_url: provided through an OSS URL that allows public network access.
        # - (Not supported) user_oss: provided through a user OSS URL.
        self.file_from = file_from
        # The UUID of the theme. The value must be returned by GetDataAgentThemeUploadSignature, and the file must have been uploaded. If the UUID is forged or the file has not been uploaded, the creation fails.
        self.theme_id = theme_id
        # The display name of the theme. The value can be up to 64 characters in length. This parameter is required during creation.
        self.theme_name = theme_name
        # The type of the custom theme. Valid values:
        # 
        # - (Default) template: The theme is a template.
        # - (Not supported) design: The theme is a DESIGN.md file.
        self.theme_type = theme_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.file_from is not None:
            result['FileFrom'] = self.file_from

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.theme_name is not None:
            result['ThemeName'] = self.theme_name

        if self.theme_type is not None:
            result['ThemeType'] = self.theme_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileFrom') is not None:
            self.file_from = m.get('FileFrom')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('ThemeName') is not None:
            self.theme_name = m.get('ThemeName')

        if m.get('ThemeType') is not None:
            self.theme_type = m.get('ThemeType')

        return self

