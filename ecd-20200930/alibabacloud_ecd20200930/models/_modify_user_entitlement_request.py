# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyUserEntitlementRequest(DaraModel):
    def __init__(
        self,
        authorize_desktop_id: List[str] = None,
        end_user_id: List[str] = None,
        region_id: str = None,
        revoke_desktop_id: List[str] = None,
    ):
        # The IDs of the cloud computers to which you want to add end users.
        self.authorize_desktop_id = authorize_desktop_id
        # The ID of the users.
        self.end_user_id = end_user_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the cloud computers whose end users you want to remove.
        self.revoke_desktop_id = revoke_desktop_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorize_desktop_id is not None:
            result['AuthorizeDesktopId'] = self.authorize_desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.revoke_desktop_id is not None:
            result['RevokeDesktopId'] = self.revoke_desktop_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeDesktopId') is not None:
            self.authorize_desktop_id = m.get('AuthorizeDesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RevokeDesktopId') is not None:
            self.revoke_desktop_id = m.get('RevokeDesktopId')

        return self

