# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSystemPropertyTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        enable_auto: bool = None,
        file_path: str = None,
        system_property_info_shrink: str = None,
        template_name: str = None,
    ):
        # Specifies whether to automatically generate preset system properties.
        self.enable_auto = enable_auto
        # The URL of the property template file. The API parses the file synchronously. An error is returned if the file format is invalid.
        # 
        # > The file must be in the following format: `{ "properties":{"key1":"value1"}}`.
        self.file_path = file_path
        # The information about the system property template.
        self.system_property_info_shrink = system_property_info_shrink
        # The name of the template. The name must meet the following requirements:
        # 
        # - Be 2 to 32 characters in length.
        # 
        # - Start with an uppercase or lowercase letter or a Chinese character. It cannot start with `http://` or `https://`.
        # 
        # - Contain letters, digits, colons (:), underscores (_), and hyphens (-). Periods (.) are not supported.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto is not None:
            result['EnableAuto'] = self.enable_auto

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.system_property_info_shrink is not None:
            result['SystemPropertyInfo'] = self.system_property_info_shrink

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAuto') is not None:
            self.enable_auto = m.get('EnableAuto')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('SystemPropertyInfo') is not None:
            self.system_property_info_shrink = m.get('SystemPropertyInfo')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

