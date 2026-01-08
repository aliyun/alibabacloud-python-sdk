# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyControlPolicyPriorityRequest(DaraModel):
    def __init__(
        self,
        acl_uuid: str = None,
        order: str = None,
    ):
        # The UUID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The priority of the access control policy.
        # 
        # This parameter is required.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.order is not None:
            result['Order'] = self.order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        return self

