# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateMessageAppRequest(DaraModel):
    def __init__(
        self,
        app_config: Dict[str, str] = None,
        app_name: str = None,
        extension: Dict[str, str] = None,
    ):
        # The configurations of the application.
        self.app_config = app_config
        # The name of the interactive message application. The name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The extended fields.
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.extension is not None:
            result['Extension'] = self.extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        return self

