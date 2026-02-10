# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoginSwitchConfigRequest(DaraModel):
    def __init__(
        self,
        item: str = None,
        status: int = None,
    ):
        # The type of the logon security settings that you want to enable or disable. Valid values:
        # 
        # *   **login_common_ip**: unapproved logon IP addresses
        # *   **login_common_time**: unapproved logon time ranges
        # *   **login_common_account**: unapproved logon accounts
        # 
        # This parameter is required.
        self.item = item
        # Specifies whether to enable the logon security settings. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

