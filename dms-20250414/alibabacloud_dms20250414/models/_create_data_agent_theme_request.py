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
        workspace_id: str = None,
    ):
        # The scenario, which affects the filtering when you view the theme list in the console. Valid values:
        # 
        # - (Recommended) custom: A user-uploaded custom theme with no preset style or information organization structure.
        # - report: A web report that conforms to the DataAgent information organization structure.
        # - (Not supported) infographic: An infographic that conforms to the DataAgent information organization structure.
        self.category = category
        # The description. The value can be up to 255 characters in length.
        self.description = description
        # The file source, which affects the backend logic for determining whether the theme is valid. Valid values:
        # 
        # - upload: The file is uploaded through OSS.
        # - (Not supported) public_url: The file is provided through a public network access OSS URL.
        # - (Not supported) user_oss: The file is provided through a user OSS URL.
        self.file_from = file_from
        # The UUID of the theme. The value must be returned by GetDataAgentThemeUploadSignature, and the file must have been uploaded. If the UUID is forged or the file has not been uploaded, the creation fails.
        self.theme_id = theme_id
        # The display name of the theme. The value can be up to 64 characters in length. This parameter is required when you create a theme.
        self.theme_name = theme_name
        # The type of the custom theme. Valid values:
        # 
        # - (Default) template: The theme is a template.
        # - (Not supported) design: The theme is a DESIGN.md file.
        self.theme_type = theme_type
        # The workspace to which the theme belongs. If this parameter is not specified or is set to personal, the personal workspace is used. You can also specify a collaboration workspace ID.
        self.workspace_id = workspace_id

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

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

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

