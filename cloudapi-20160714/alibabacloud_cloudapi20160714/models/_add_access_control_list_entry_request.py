# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAccessControlListEntryRequest(DaraModel):
    def __init__(
        self,
        acl_entrys: str = None,
        acl_id: str = None,
        security_token: str = None,
    ):
        # The ACL settings.
        # 
        # *   entry: the entries that you want to add to the ACL. You can add CIDR blocks. Separate multiple CIDR blocks with commas (,).
        # *   comment: the description of the ACL.
        # 
        # > You can add at most 50 IP addresses or CIDR blocks to an ACL in each call. If the IP address or CIDR block that you want to add to an ACL already exists, the IP address or CIDR block is not added. The entries that you add must be CIDR blocks.
        self.acl_entrys = acl_entrys
        # The ID of the access control list (ACL).
        # 
        # This parameter is required.
        self.acl_id = acl_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntrys') is not None:
            self.acl_entrys = m.get('AclEntrys')

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

