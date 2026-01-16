# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLogstashSettingsRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        client_token: str = None,
    ):
        self.body = body
        # 5A2CFF0E-5718-45B5-9D4D-70B3FF\\*\\*\\*\\*
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

