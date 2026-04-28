# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnLinkAccountRequest(DaraModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # Additional information for the unique account identifier. For example, when the account is a phone number, this field should be filled with the area code of the phone, such as 86 for Mainland China. If not provided, it defaults to 86.
        self.extra = extra
        # Unique identifier of the account, such as a phone number
        # 
        # This parameter is required.
        self.identity = identity
        # Account type
        # 
        # mobile: Phone number
        # 
        # email: Email address
        # 
        # ding: DingTalk
        # 
        # ram: Alibaba Cloud RAM User
        # 
        # wechat: WeCom
        # 
        # ldap: LDAP account
        # 
        # custom: Custom account
        # 
        # This parameter is required.
        self.type = type
        # User identifier
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['extra'] = self.extra

        if self.identity is not None:
            result['identity'] = self.identity

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('identity') is not None:
            self.identity = m.get('identity')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

