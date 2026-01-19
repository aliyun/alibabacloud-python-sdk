# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccessControlListRequest(DaraModel):
    def __init__(
        self,
        acl_name: str = None,
        address_ipversion: str = None,
        security_token: str = None,
    ):
        # The name of the ACL. The name must be 1 to 30 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores (_). The name must be unique within the region.
        # 
        # This parameter is required.
        self.acl_name = acl_name
        # The IP protocol version of the ACL. Valid values:
        # 
        # *   **IPv4**
        # *   **IPv6**
        self.address_ipversion = address_ipversion
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

