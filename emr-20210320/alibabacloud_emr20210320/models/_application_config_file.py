# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplicationConfigFile(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        config_file_name: str = None,
    ):
        # 应用名称。
        # 
        # This parameter is required.
        self.application_name = application_name
        # 配置文件名称。
        self.config_file_name = config_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        return self

