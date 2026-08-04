# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncCreateAgAccountRequest(DaraModel):
    def __init__(
        self,
        login_email: str = None,
        maser_account_info: str = None,
        mpk: str = None,
    ):
        # This parameter is required.
        self.login_email = login_email
        # This parameter is required.
        self.maser_account_info = maser_account_info
        # This parameter is required.
        self.mpk = mpk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email

        if self.maser_account_info is not None:
            result['MaserAccountInfo'] = self.maser_account_info

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')

        if m.get('MaserAccountInfo') is not None:
            self.maser_account_info = m.get('MaserAccountInfo')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        return self

