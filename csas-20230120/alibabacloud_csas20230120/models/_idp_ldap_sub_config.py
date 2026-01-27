# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpLdapSubConfig(DaraModel):
    def __init__(
        self,
        base_dn: str = None,
        group_base_dn: str = None,
        group_filter: str = None,
        group_membership_attr: str = None,
        group_name_attr: str = None,
        login_name_attr: str = None,
        server_addr: str = None,
        server_port: str = None,
        server_type: str = None,
        use_ssl: bool = None,
        user_dn: str = None,
        user_filter: str = None,
        user_password: str = None,
    ):
        self.base_dn = base_dn
        self.group_base_dn = group_base_dn
        self.group_filter = group_filter
        self.group_membership_attr = group_membership_attr
        self.group_name_attr = group_name_attr
        self.login_name_attr = login_name_attr
        self.server_addr = server_addr
        self.server_port = server_port
        self.server_type = server_type
        self.use_ssl = use_ssl
        self.user_dn = user_dn
        self.user_filter = user_filter
        self.user_password = user_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_dn is not None:
            result['BaseDn'] = self.base_dn

        if self.group_base_dn is not None:
            result['GroupBaseDn'] = self.group_base_dn

        if self.group_filter is not None:
            result['GroupFilter'] = self.group_filter

        if self.group_membership_attr is not None:
            result['GroupMembershipAttr'] = self.group_membership_attr

        if self.group_name_attr is not None:
            result['GroupNameAttr'] = self.group_name_attr

        if self.login_name_attr is not None:
            result['LoginNameAttr'] = self.login_name_attr

        if self.server_addr is not None:
            result['ServerAddr'] = self.server_addr

        if self.server_port is not None:
            result['ServerPort'] = self.server_port

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.user_dn is not None:
            result['UserDn'] = self.user_dn

        if self.user_filter is not None:
            result['UserFilter'] = self.user_filter

        if self.user_password is not None:
            result['UserPassword'] = self.user_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseDn') is not None:
            self.base_dn = m.get('BaseDn')

        if m.get('GroupBaseDn') is not None:
            self.group_base_dn = m.get('GroupBaseDn')

        if m.get('GroupFilter') is not None:
            self.group_filter = m.get('GroupFilter')

        if m.get('GroupMembershipAttr') is not None:
            self.group_membership_attr = m.get('GroupMembershipAttr')

        if m.get('GroupNameAttr') is not None:
            self.group_name_attr = m.get('GroupNameAttr')

        if m.get('LoginNameAttr') is not None:
            self.login_name_attr = m.get('LoginNameAttr')

        if m.get('ServerAddr') is not None:
            self.server_addr = m.get('ServerAddr')

        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('UserDn') is not None:
            self.user_dn = m.get('UserDn')

        if m.get('UserFilter') is not None:
            self.user_filter = m.get('UserFilter')

        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')

        return self

