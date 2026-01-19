# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveAccessControlListEntryRequest(DaraModel):
    def __init__(
        self,
        acl_entrys: str = None,
        acl_id: str = None,
        security_token: str = None,
    ):
        self.acl_entrys = acl_entrys
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

