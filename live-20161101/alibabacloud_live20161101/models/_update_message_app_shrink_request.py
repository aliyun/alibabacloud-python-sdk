# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMessageAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_config_shrink: str = None,
        app_id: str = None,
        app_name: str = None,
        extension_shrink: str = None,
    ):
        # Application configuration.
        self.app_config_shrink = app_config_shrink
        # Interactive message application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Interactive message application name.
        self.app_name = app_name
        # Extension field.
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

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config_shrink = m.get('AppConfig')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')

        return self

