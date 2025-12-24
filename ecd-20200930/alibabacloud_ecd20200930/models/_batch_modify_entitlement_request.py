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
        # The IDs of the cloud computers for which you want to modify end users.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The IDs of the users.
        self.end_user_id = end_user_id
        # The number of cloud computers allocated to each user.
        self.max_desktop_per_user = max_desktop_per_user
        # The number of users assigned to each cloud computer.
        self.max_user_per_desktop = max_user_per_desktop
        # Whether to preview the assign results instead of actually assigning cloud computers.
        self.preview = preview
        # The ID of the region. Call the DescribeRegions operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The disproportional assignment policy. Valid values:
        # 
        # AVERAGE: The system preferentially guarantees that each user is assigned with at least a cloud computer. If the number of selected cloud computers cannot be proportionally assigned to the selected users, ensure that each user is assigned a cloud computer.
        # 
        # CENTRAL: The system preferentially assigns the designated number of cloud computers to each user. If the number of selected cloud computers cannot be proportionally assigned to the selected users, ensure that each user is assigned the specified number of cloud computers.
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

