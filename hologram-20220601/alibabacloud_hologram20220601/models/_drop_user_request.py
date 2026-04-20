# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DropUserRequest(DaraModel):
    def __init__(
        self,
        super_user: str = None,
        user_name: str = None,
    ):
        self.super_user = super_user
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.super_user is not None:
            result['superUser'] = self.super_user

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('superUser') is not None:
            self.super_user = m.get('superUser')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

