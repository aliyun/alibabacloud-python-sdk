# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnlockUsersRequest(DaraModel):
    def __init__(
        self,
        auto_lock_time: str = None,
        business_channel: str = None,
        users: List[str] = None,
    ):
        # The date on which the convenience users are automatically locked.
        self.auto_lock_time = auto_lock_time
        self.business_channel = business_channel
        # The usernames of the convenience users that you want to unlock.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

