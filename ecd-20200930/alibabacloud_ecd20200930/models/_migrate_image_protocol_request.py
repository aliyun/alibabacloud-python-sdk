# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MigrateImageProtocolRequest(DaraModel):
    def __init__(
        self,
        image_id: List[str] = None,
        region_id: str = None,
        target_protocol_type: str = None,
    ):
        # The image IDs.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The protocol to which you want to update the image protocols. Set the value to ASP.
        self.target_protocol_type = target_protocol_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_protocol_type is not None:
            result['TargetProtocolType'] = self.target_protocol_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetProtocolType') is not None:
            self.target_protocol_type = m.get('TargetProtocolType')

        return self

