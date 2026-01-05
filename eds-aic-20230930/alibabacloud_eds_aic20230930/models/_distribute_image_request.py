# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DistributeImageRequest(DaraModel):
    def __init__(
        self,
        distribute_region_list: List[str] = None,
        image_id: str = None,
    ):
        # The regions to which you want to distribute an image.
        # 
        # This parameter is required.
        self.distribute_region_list = distribute_region_list
        # The ID of the image that you want to distribute.
        # 
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_region_list is not None:
            result['DistributeRegionList'] = self.distribute_region_list

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeRegionList') is not None:
            self.distribute_region_list = m.get('DistributeRegionList')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        return self

