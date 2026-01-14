# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserByMobileAccountRequest(DaraModel):
    def __init__(
        self,
        mobile_type: str = None,
        mobile_user_id: str = None,
    ):
        # This parameter is required.
        self.mobile_type = mobile_type
        # This parameter is required.
        self.mobile_user_id = mobile_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile_type is not None:
            result['MobileType'] = self.mobile_type

        if self.mobile_user_id is not None:
            result['MobileUserId'] = self.mobile_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileType') is not None:
            self.mobile_type = m.get('MobileType')

        if m.get('MobileUserId') is not None:
            self.mobile_user_id = m.get('MobileUserId')

        return self

