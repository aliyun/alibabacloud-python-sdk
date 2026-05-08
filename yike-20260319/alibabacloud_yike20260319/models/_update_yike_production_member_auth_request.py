# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateYikeProductionMemberAuthRequest(DaraModel):
    def __init__(
        self,
        auth: str = None,
        production_id: str = None,
        yike_user_id: str = None,
    ):
        # This parameter is required.
        self.auth = auth
        # This parameter is required.
        self.production_id = production_id
        # This parameter is required.
        self.yike_user_id = yike_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.yike_user_id is not None:
            result['YikeUserId'] = self.yike_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('YikeUserId') is not None:
            self.yike_user_id = m.get('YikeUserId')

        return self

