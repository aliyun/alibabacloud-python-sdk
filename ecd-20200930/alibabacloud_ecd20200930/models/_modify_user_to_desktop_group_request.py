# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyUserToDesktopGroupRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        new_end_user_ids: List[str] = None,
        old_end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The IDs of the end users that you want to add. You can configure 1 to 500 IDs.
        # 
        # This parameter is required.
        self.new_end_user_ids = new_end_user_ids
        # The IDs of the end users that you want to remove. You can configure 1 to 500 IDs.
        # 
        # This parameter is required.
        self.old_end_user_ids = old_end_user_ids
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
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
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.new_end_user_ids is not None:
            result['NewEndUserIds'] = self.new_end_user_ids

        if self.old_end_user_ids is not None:
            result['OldEndUserIds'] = self.old_end_user_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('NewEndUserIds') is not None:
            self.new_end_user_ids = m.get('NewEndUserIds')

        if m.get('OldEndUserIds') is not None:
            self.old_end_user_ids = m.get('OldEndUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

