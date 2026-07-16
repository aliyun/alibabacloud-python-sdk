# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RequestUploadTokenRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        os: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.os is not None:
            result['Os'] = self.os

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        return self

