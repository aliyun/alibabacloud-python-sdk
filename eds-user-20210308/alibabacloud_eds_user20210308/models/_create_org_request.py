# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrgRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        org_name: str = None,
        parent_org_id: str = None,
    ):
        self.business_channel = business_channel
        # The name of the organization.
        # 
        # This parameter is required.
        self.org_name = org_name
        # The ID of the parent organization.
        # 
        # This parameter is required.
        self.parent_org_id = parent_org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')

        return self

