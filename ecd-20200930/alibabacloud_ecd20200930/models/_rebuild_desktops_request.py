# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RebuildDesktopsRequest(DaraModel):
    def __init__(
        self,
        after_status: str = None,
        desktop_id: List[str] = None,
        image_id: str = None,
        language: str = None,
        operate_type: str = None,
        region_id: str = None,
    ):
        self.after_status = after_status
        # The cloud computer IDs. You can specify the IDs of 1 to 20 cloud computers.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the new image.
        self.image_id = image_id
        # The OS language. Only system images are supported, and Linux cloud computers support only English.
        # 
        # Valid values:
        # 
        # *   en-US: English
        # *   zh-HK: Traditional Chinese (Hong Kong, China)
        # *   zh-CN: Simplified Chinese
        # *   ja-JP: Japanese
        self.language = language
        # The operation type on the data disk.
        # 
        # >  This parameter is empty by default regardless of whether data disks are attached to the cloud computer.
        # 
        # *   No data disks are attached to the cloud computer:\\
        #     No operation is performed on the data disks of the cloud computer regardless of the value of this parameter.
        # 
        # *   Data disks are attached to the cloud computer:
        # 
        #     1.  The OS of the cloud computer is the same as the OS of the destination image:
        # 
        #         *   If you set the OperateType parameter to `replace`, the data in the data disks of the cloud computer is replaced.
        #         *   If you leave the OperateType parameter empty, the data in the data disks of the cloud computer is retained.
        # 
        #     2.  The OS of the cloud computer is different from the OS of the destination image:
        # 
        #         *   If you set the OperateType parameter to `replace`, the data in the data disks of the cloud computer is replaced.
        #         *   If you leave the OperateType parameter empty, the data in the data disks of the cloud computer is cleared.
        self.operate_type = operate_type
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
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
        if self.after_status is not None:
            result['AfterStatus'] = self.after_status

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.language is not None:
            result['Language'] = self.language

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterStatus') is not None:
            self.after_status = m.get('AfterStatus')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

