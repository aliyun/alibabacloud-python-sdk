# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelRouterBatchRenewMemberApiKeysRequest(DaraModel):
    def __init__(
        self,
        expire_at: str = None,
        user_ids: List[int] = None,
    ):
        # The new expiration time in RFC 3339 format. The time must be later than the current time. If this parameter is not provided or is set to null, the API keys remain permanently valid. This parameter only modifies the validity period and does not change the enabled or disabled status.
        self.expire_at = expire_at
        # The list of member user IDs. This operation renews all undeleted API keys of these members in the specified department.
        # 
        # This parameter is required.
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

        if self.user_ids is not None:
            result['userIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')

        return self

