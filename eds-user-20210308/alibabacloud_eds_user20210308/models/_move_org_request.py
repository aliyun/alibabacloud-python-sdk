# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveOrgRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        new_parent_org_id: str = None,
        org_id: str = None,
    ):
        self.business_channel = business_channel
        # The ID of the parent organization.
        # 
        # This parameter is required.
        self.new_parent_org_id = new_parent_org_id
        # The ID of the organization that you want to move.
        # 
        # This parameter is required.
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.new_parent_org_id is not None:
            result['NewParentOrgId'] = self.new_parent_org_id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('NewParentOrgId') is not None:
            self.new_parent_org_id = m.get('NewParentOrgId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        return self

