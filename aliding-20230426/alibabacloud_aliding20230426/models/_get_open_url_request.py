# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpenUrlRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        file_url: str = None,
        language: str = None,
        system_token: str = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.file_url = file_url
        self.language = language
        # This parameter is required.
        self.system_token = system_token
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.language is not None:
            result['Language'] = self.language

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

