# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangePasswordRequest(DaraModel):
    def __init__(
        self,
        new_password: str = None,
        old_password: str = None,
    ):
        # This parameter is required.
        self.new_password = new_password
        # This parameter is required.
        self.old_password = old_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_password is not None:
            result['NewPassword'] = self.new_password

        if self.old_password is not None:
            result['OldPassword'] = self.old_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')

        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')

        return self

