# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResetDesktopsRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        desktop_id: List[str] = None,
        image_id: str = None,
        last_retry_time: int = None,
        pay_type: str = None,
        region_id: str = None,
        reset_scope: str = None,
        reset_type: str = None,
    ):
        # The ID of the cloud computer share.
        # 
        # *   If you specify `DesktopId`, ignore `DesktopGroupId`.
        # *   If you leave `DesktopId` empty, the system obtains the IDs of all cloud computers within the share specified by `DesktopGroupId`.``
        self.desktop_group_id = desktop_group_id
        # The IDs of the cloud computer shares.
        self.desktop_group_ids = desktop_group_ids
        # The IDs of the cloud computers. You can specify the IDs of 1 to 100 cloud computers.
        self.desktop_id = desktop_id
        # The ID of the image.
        self.image_id = image_id
        self.last_retry_time = last_retry_time
        # The billing method of the cloud computer share.
        # 
        # >  This parameter takes effect when you reset a cloud computer share. If you leave this parameter empty, all cloud computers in that share are reset.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.pay_type = pay_type
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/436773.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reset scope. You can configure this parameter to reset the image or cloud computer.
        # 
        # Valid values:
        # 
        # *   ALL (default): resets the image and cloud computer.
        # *   IMAGE: resets only the image.
        self.reset_scope = reset_scope
        # The disk reset type.
        # 
        # Valid values:
        # 
        # *   0: does not reset disks.
        # *   1: resets only the system disk.
        # *   2: resets only the user disk.
        # *   3: resets the system disk and the user disk.
        # 
        # This parameter is required.
        self.reset_type = reset_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.last_retry_time is not None:
            result['LastRetryTime'] = self.last_retry_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_scope is not None:
            result['ResetScope'] = self.reset_scope

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LastRetryTime') is not None:
            self.last_retry_time = m.get('LastRetryTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetScope') is not None:
            self.reset_scope = m.get('ResetScope')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        return self

