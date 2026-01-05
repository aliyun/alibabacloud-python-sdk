# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAclRelationsRequest(DaraModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
    ):
        # The access control list (ACL) IDs. You can query at most five ACLs in each call.
        # 
        # This parameter is required.
        self.acl_ids = acl_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        return self

