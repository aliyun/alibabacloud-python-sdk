# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFormDataByIDRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        id: str = None,
        language: str = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.id = id
        self.language = language
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.id is not None:
            result['Id'] = self.id

        if self.language is not None:
            result['Language'] = self.language

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

