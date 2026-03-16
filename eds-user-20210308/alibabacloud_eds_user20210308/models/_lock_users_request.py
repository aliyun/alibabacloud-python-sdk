# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class LockUsersRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        logout_session: bool = None,
        users: List[str] = None,
    ):
        self.business_channel = business_channel
        self.logout_session = logout_session
        # The usernames of the convenience users that you want to lock.
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
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.logout_session is not None:
            result['LogoutSession'] = self.logout_session

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('LogoutSession') is not None:
            self.logout_session = m.get('LogoutSession')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

