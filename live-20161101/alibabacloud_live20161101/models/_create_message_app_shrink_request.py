# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMessageAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_config_shrink: str = None,
        app_name: str = None,
        extension_shrink: str = None,
    ):
        # The configurations of the application.
        self.app_config_shrink = app_config_shrink
        # The name of the interactive message application. The name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The extended fields.
        self.extension_shrink = extension_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config_shrink is not None:
            result['AppConfig'] = self.app_config_shrink

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config_shrink = m.get('AppConfig')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')

        return self

