# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RamAccount(DaraModel):
    def __init__(
        self,
        bindable: bool = None,
        display_name: str = None,
        uid: str = None,
        user_name: str = None,
    ):
        # Specifies whether the RamAccount can be bound to other resources.
        self.bindable = bindable
        # The display name for the RamAccount, which appears in the console.
        self.display_name = display_name
        # The unique identifier for the RamAccount.
        self.uid = uid
        # The user name for the RamAccount.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bindable is not None:
            result['bindable'] = self.bindable

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.uid is not None:
            result['uid'] = self.uid

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindable') is not None:
            self.bindable = m.get('bindable')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

