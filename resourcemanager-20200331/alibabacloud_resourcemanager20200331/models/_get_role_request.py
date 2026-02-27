# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoleRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        role_name: str = None,
    ):
        # The language in which you want to return the description of the role. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The name of the role.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

