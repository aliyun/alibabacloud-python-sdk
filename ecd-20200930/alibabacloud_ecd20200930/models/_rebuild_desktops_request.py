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
        # The IDs of the cloud computers to rebuild. You can specify 1 to 20 IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the new image.
        self.image_id = image_id
        # The operating system language. This parameter applies only to system images. For Linux cloud computers, only English is supported.
        self.language = language
        # Specifies how to handle the data disk.
        # 
        # > This parameter is optional.
        # 
        # - If a cloud computer does not have a data disk, this parameter is ignored.<br>
        # 
        # - If a cloud computer has a data disk:
        # 
        #   1. If the new image has the same operating system as the original one:
        # 
        #      - If you set this parameter to `replace`, the data disk is replaced.
        # 
        #      - If you do not specify this parameter, the data disk is retained.
        # 
        #   2. If the new image has a different operating system:
        # 
        #      - If you set this parameter to `replace`, the data disk is replaced.
        # 
        #      - If you do not specify this parameter, the data disk is erased.
        self.operate_type = operate_type
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to find the regions where Elastic Desktop Service is available.
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

