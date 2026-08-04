# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindAllContacterRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        locale_string: str = None,
        type: str = None,
        user_id: int = None,
    ):
        self.app_name = app_name
        self.locale_string = locale_string
        self.type = type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.locale_string is not None:
            result['LocaleString'] = self.locale_string

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('LocaleString') is not None:
            self.locale_string = m.get('LocaleString')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

