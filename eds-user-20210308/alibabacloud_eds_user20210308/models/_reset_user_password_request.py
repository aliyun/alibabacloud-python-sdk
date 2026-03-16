# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResetUserPasswordRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        notify_type: int = None,
        users: List[str] = None,
    ):
        self.business_channel = business_channel
        # The method to notify the user after the password is reset.
        # 
        # > Alibaba Cloud accounts of the international site do not support sending notification through text messages.
        self.notify_type = notify_type
        # The names of the convenience users whose passwords you want to reset.
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

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

