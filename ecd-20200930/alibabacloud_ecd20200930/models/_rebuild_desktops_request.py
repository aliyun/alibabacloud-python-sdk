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
        # The target status of the cloud computer after the rebuild is complete.
        self.after_status = after_status
        # The cloud computer ID. You can specify 1 to 20 IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The ID of the new image to use after the change.
        self.image_id = image_id
        # The operating system language. Currently, only system images are supported, and Linux computers only support English.
        self.language = language
        # The operation type for the data cloud disk.
        # 
        # > Regardless of whether the cloud computer has a data cloud disk, no field value is passed in by default when you call this operation.
        # 
        # - If the cloud computer has no data cloud disk:  
        #         No data cloud disk operation is performed regardless of the field value passed in.
        # - If the cloud computer has a data cloud disk:
        #     1. When the operating system of the cloud computer is the same as that of the target image:
        #         - If the field value is `replace`, the data cloud disk of the cloud computer is replaced.
        #         - If no field value is passed in, the original data cloud disk of the cloud computer is retained.
        #     2. When the operating system of the cloud computer is different from that of the target image:
        #         - If the field value is `replace`, the data cloud disk of the cloud computer is replaced.
        #         - If no field value is passed in, the data cloud disk of the cloud computer is cleared.
        self.operate_type = operate_type
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the list of regions supported by Elastic Desktop Service.
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

