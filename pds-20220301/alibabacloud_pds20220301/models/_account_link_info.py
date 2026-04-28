# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountLinkInfo(DaraModel):
    def __init__(
        self,
        authentication_type: str = None,
        created_at: int = None,
        display_name: str = None,
        domain_id: str = None,
        extra: str = None,
        identity: str = None,
        last_login_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        # The type of the account. Valid values:
        # 
        # *   mobile: mobile number
        # *   email: email address
        # *   ding: DingTalk account
        # *   ram: Alibaba Cloud Resource Access Management (RAM) user
        # *   wechat: WeCom account
        # *   ldap: Lightweight Directory Access Protocol (LDAP) account
        # *   custom: custom account
        self.authentication_type = authentication_type
        # The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The display name of the account. For example, the unique identifier of an LDAP account is its UID, but the account display name can be the job number or other information.
        self.display_name = display_name
        # The domain ID.
        self.domain_id = domain_id
        # The additional information about the account. If the account type is a mobile number, the value of this parameter indicates the country code. For example, the country code in the Chinese mainland is 86 and a value of 86 is returned only if authentication_type is set to mobile.
        self.extra = extra
        # The unique identifier of the account.
        self.identity = identity
        self.last_login_time = last_login_time
        self.status = status
        # The user ID of the account.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.extra is not None:
            result['extra'] = self.extra

        if self.identity is not None:
            result['identity'] = self.identity

        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time

        if self.status is not None:
            result['status'] = self.status

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('identity') is not None:
            self.identity = m.get('identity')

        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

