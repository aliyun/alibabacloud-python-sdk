# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFaceUserIdByCustomUserIdRequest(DaraModel):
    def __init__(
        self,
        custom_user_id: str = None,
        isolation_id: str = None,
    ):
        # The user ID in the caller system.
        # 
        # This parameter is required.
        self.custom_user_id = custom_user_id
        # The isolation ID.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        return self

