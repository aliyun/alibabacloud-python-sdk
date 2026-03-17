# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAclAttributeRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        region_id: str = None,
    ):
        # The ID of the ACL.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The ID of the region where the ACL is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

