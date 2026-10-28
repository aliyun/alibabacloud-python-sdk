# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccountInfoRequest(DaraModel):
    def __init__(
        self,
        account_nickname: str = None,
        customer_bd: str = None,
        remark: str = None,
        uid: int = None,
    ):
        # The nickname of the sub-account. For enterprise customers, this is the company name. For T2 partners, this is the partner name.
        self.account_nickname = account_nickname
        # The customer business manager. Maximum length: 50 characters.
        self.customer_bd = customer_bd
        # The description of the sub-account.
        self.remark = remark
        # The UID of the sub-account.
        # 
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname

        if self.customer_bd is not None:
            result['CustomerBd'] = self.customer_bd

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')

        if m.get('CustomerBd') is not None:
            self.customer_bd = m.get('CustomerBd')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

