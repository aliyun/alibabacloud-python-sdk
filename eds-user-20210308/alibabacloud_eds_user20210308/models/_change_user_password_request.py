# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeUserPasswordRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        end_user_id: str = None,
        new_password: str = None,
    ):
        self.business_channel = business_channel
        self.end_user_id = end_user_id
        self.new_password = new_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.new_password is not None:
            result['NewPassword'] = self.new_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')

        return self

