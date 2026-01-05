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
        self.enable_auto = enable_auto
        self.file_path = file_path
        self.system_property_info_shrink = system_property_info_shrink
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

