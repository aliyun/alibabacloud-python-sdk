# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartqAuthTransferRequest(DaraModel):
    def __init__(
        self,
        origin_user_id: str = None,
        target_user_ids: str = None,
    ):
        # Source user ID.
        # 
        # This parameter is required.
        self.origin_user_id = origin_user_id
        # Target user ID array, separated by English commas.
        # >Warning: The number of user IDs cannot exceed 100.
        # 
        # This parameter is required.
        self.target_user_ids = target_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_user_id is not None:
            result['OriginUserId'] = self.origin_user_id

        if self.target_user_ids is not None:
            result['TargetUserIds'] = self.target_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginUserId') is not None:
            self.origin_user_id = m.get('OriginUserId')

        if m.get('TargetUserIds') is not None:
            self.target_user_ids = m.get('TargetUserIds')

        return self

