# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableInstanceAccessControlRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_type: str = None,
        address_ipversion: str = None,
        instance_id: str = None,
        security_token: str = None,
    ):
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The ACL type. Valid values:
        # 
        # *   black: blacklist
        # *   white: whitelist
        # 
        # This parameter is required.
        self.acl_type = acl_type
        # The IP version. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

