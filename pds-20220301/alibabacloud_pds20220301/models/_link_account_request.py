# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LinkAccountRequest(DaraModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # The additional information about the unique identifier of the account. For example, if type is set to mobile, set the value of extra to a country code. For example, a value of 86 specifies a mobile number in the Chinese mainland. If you do not specify this parameter, 86 is used by default.
        self.extra = extra
        # The unique identifier of the account, such as a mobile number.
        # 
        # This parameter is required.
        self.identity = identity
        # The account type. Valid values:
        # 
        # *   mobile: a mobile number.
        # *   email: an email address.
        # *   ding: a DingTalk account.
        # *   ram: an Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: a WeCom account.
        # *   ldap: a Lightweight Directory Access Protocol (LDAP) account.
        # *   custom: a custom account.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the user with which you want to associate an account.
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

