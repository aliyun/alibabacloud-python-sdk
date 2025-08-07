# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class GetUserRequest(DaraModel):
    def __init__(
        self,
        user_principal: str = None,
    ):
        self.user_principal = user_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')

        return self

