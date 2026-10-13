# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HandleOidcCallbackRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        state: str = None,
    ):
        # The code parameter carried in the OIDC callback request.
        self.code = code
        # The state parameter carried in the OIDC callback request.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

