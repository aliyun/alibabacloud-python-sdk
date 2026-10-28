# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchModifyEntitlementRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        end_user_id: List[str] = None,
        max_desktop_per_user: int = None,
        max_user_per_desktop: int = None,
        preview: bool = None,
        region_id: str = None,
        strategy: str = None,
    ):
        # The IDs of the cloud desktops for which you want to modify the authorized users.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The user IDs, which are the usernames.
        self.end_user_id = end_user_id
        # The number of cloud desktops assigned to each user.
        self.max_desktop_per_user = max_desktop_per_user
        # The number of users assigned to each cloud desktop.
        self.max_user_per_desktop = max_user_per_desktop
        # Specifies whether to preview the assignment. A preview does not perform the actual assignment.
        self.preview = preview
        # The region ID. You can call DescribeRegions to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The policy used when proportional matching is not possible. Valid values:
        # 
        # - AVERAGE: Prioritizes assigning cloud desktops to each user. When the number of selected cloud desktops and users cannot be matched proportionally, cloud desktops are assigned to each user first.
        # - CENTRAL: Prioritizes assigning a specified number of cloud desktops to users. When the number of selected cloud desktops and users cannot be matched proportionally, the specified number of cloud desktops are assigned to users first.
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.max_desktop_per_user is not None:
            result['MaxDesktopPerUser'] = self.max_desktop_per_user

        if self.max_user_per_desktop is not None:
            result['MaxUserPerDesktop'] = self.max_user_per_desktop

        if self.preview is not None:
            result['Preview'] = self.preview

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MaxDesktopPerUser') is not None:
            self.max_desktop_per_user = m.get('MaxDesktopPerUser')

        if m.get('MaxUserPerDesktop') is not None:
            self.max_user_per_desktop = m.get('MaxUserPerDesktop')

        if m.get('Preview') is not None:
            self.preview = m.get('Preview')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

