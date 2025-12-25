# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterUserRequest(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        role_names: str = None,
        tid: int = None,
        uid: str = None,
        user_nick: str = None,
    ):
        # The mobile number of the user.
        self.mobile = mobile
        # The role that you want to assign to the user. Valid values:
        # 
        # *   **USER**: a regular user role
        # *   **DBA**: a database administrator (DBA) role
        # *   **ADMIN**: a DMS administrator role
        # *   **SECURITY_ADMIN**: a security administrator role
        # 
        # >  If you do not specify this parameter, the regular user role is assigned to the user by default. You can assign one or more roles to the user. Separate multiple roles with commas (,).
        self.role_names = role_names
        # The ID of the tenant.
        # 
        # >  To query ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid
        # The UID of the Alibaba Cloud account of the user that you want to register.
        # 
        # This parameter is required.
        self.uid = uid
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.role_names is not None:
            result['RoleNames'] = self.role_names

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

