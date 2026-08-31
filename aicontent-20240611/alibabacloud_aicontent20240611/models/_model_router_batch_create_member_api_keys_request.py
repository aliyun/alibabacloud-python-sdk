# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelRouterBatchCreateMemberApiKeysRequest(DaraModel):
    def __init__(
        self,
        expire_at: str = None,
        name: str = None,
        user_ids: List[int] = None,
    ):
        # The expiration time in RFC 3339 format. This parameter is optional. If not specified, the key is permanently valid.
        self.expire_at = expire_at
        # The key name. This parameter is optional.
        self.name = name
        # The list of member user IDs.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.name is not None:
            result['name'] = self.name

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        return self

