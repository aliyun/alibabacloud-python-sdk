# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadPolicyRequest(DaraModel):
    def __init__(
        self,
        jwt_token: str = None,
        type: str = None,
    ):
        self.jwt_token = jwt_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jwt_token is not None:
            result['jwtToken'] = self.jwt_token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jwtToken') is not None:
            self.jwt_token = m.get('jwtToken')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

