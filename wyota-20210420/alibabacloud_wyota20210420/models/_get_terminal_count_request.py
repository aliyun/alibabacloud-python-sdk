# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTerminalCountRequest(DaraModel):
    def __init__(
        self,
        client_type: int = None,
    ):
        # The terminal type. Valid values:
        # 
        # - 1: hardware terminal.
        # - 2: software terminal.
        # - 3: secure browser plug-in.
        # - 4: GuestOS application.
        # - 5: DingTalk Wuying plug-in.
        # - 6: cloud application component.
        # - 7: Cloud Hub.
        # - 8: H5.
        # 
        # Default value: 1.
        self.client_type = client_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        return self

