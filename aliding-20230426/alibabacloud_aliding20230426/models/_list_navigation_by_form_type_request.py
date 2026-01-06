# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNavigationByFormTypeRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_type: str = None,
        language: str = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.form_type = form_type
        self.language = language
        # This parameter is required.
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

        if self.form_type is not None:
            result['FormType'] = self.form_type

        if self.language is not None:
            result['Language'] = self.language

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormType') is not None:
            self.form_type = m.get('FormType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

