# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLDAPConfigRequest(DaraModel):
    def __init__(
        self,
        bind_dn: str = None,
        file_system_id: str = None,
        search_base: str = None,
        uri: str = None,
    ):
        # The LDAP entry.
        self.bind_dn = bind_dn
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The LDAP search base.
        # 
        # This parameter is required.
        self.search_base = search_base
        # The LDAP service address.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.search_base is not None:
            result['SearchBase'] = self.search_base

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

