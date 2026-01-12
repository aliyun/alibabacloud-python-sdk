# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRayDashboardRequest(DaraModel):
    def __init__(
        self,
        is_shared: bool = None,
        token: str = None,
    ):
        # Specifies whether the link is a sharing link. If yes, a token is required.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.is_shared = is_shared
        # The token obtained from GetToken
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_shared is not None:
            result['isShared'] = self.is_shared

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isShared') is not None:
            self.is_shared = m.get('isShared')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

