# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchSetDesktopManagerRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        is_desktop_manager: str = None,
        users: List[str] = None,
    ):
        self.business_channel = business_channel
        # Whether the convenience account has the local administrator permissions on cloud computers.
        # 
        # Valid values:
        # 
        # *   0: no
        # *   1 (default): yes
        self.is_desktop_manager = is_desktop_manager
        # The convenience accounts.
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

        if self.is_desktop_manager is not None:
            result['IsDesktopManager'] = self.is_desktop_manager

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('IsDesktopManager') is not None:
            self.is_desktop_manager = m.get('IsDesktopManager')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

