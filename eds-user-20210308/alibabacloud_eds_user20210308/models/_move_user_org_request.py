# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MoveUserOrgRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        end_user_ids: List[str] = None,
        org_id: str = None,
    ):
        self.business_channel = business_channel
        # The user IDs.
        # 
        # This parameter is required.
        self.end_user_ids = end_user_ids
        # The organization ID.
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

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        return self

