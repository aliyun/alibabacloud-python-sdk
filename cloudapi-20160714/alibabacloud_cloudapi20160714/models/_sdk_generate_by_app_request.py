# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SdkGenerateByAppRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        language: str = None,
        security_token: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.language = language
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.language is not None:
            result['Language'] = self.language

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

