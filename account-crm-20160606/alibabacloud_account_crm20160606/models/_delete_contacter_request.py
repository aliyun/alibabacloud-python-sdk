# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContacterRequest(DaraModel):
    def __init__(
        self,
        contacter_id: int = None,
        user_id: int = None,
    ):
        # This parameter is required.
        self.contacter_id = contacter_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacter_id is not None:
            result['ContacterId'] = self.contacter_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContacterId') is not None:
            self.contacter_id = m.get('ContacterId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

