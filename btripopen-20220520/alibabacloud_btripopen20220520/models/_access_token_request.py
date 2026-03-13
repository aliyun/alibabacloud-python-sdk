# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccessTokenRequest(DaraModel):
    def __init__(
        self,
        app_secret: str = None,
    ):
        # This parameter is required.
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')

        return self

