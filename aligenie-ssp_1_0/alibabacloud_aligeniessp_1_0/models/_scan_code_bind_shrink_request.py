# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScanCodeBindShrinkRequest(DaraModel):
    def __init__(
        self,
        bind_req_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Input parameters for QR code scanning binding
        # 
        # This parameter is required.
        self.bind_req_shrink = bind_req_shrink
        # User identity information
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_req_shrink is not None:
            result['BindReq'] = self.bind_req_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindReq') is not None:
            self.bind_req_shrink = m.get('BindReq')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

