# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteImagesRequest(DaraModel):
    def __init__(
        self,
        delete_cascaded_bundle: bool = None,
        image_id: List[str] = None,
        region_id: str = None,
    ):
        # Specifies whether to delete the associated template.
        self.delete_cascaded_bundle = delete_cascaded_bundle
        # The image IDs. You can specify 1 to 100 image IDs.
        # 
        # This parameter is required.
        self.image_id = image_id
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
        if self.delete_cascaded_bundle is not None:
            result['DeleteCascadedBundle'] = self.delete_cascaded_bundle

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteCascadedBundle') is not None:
            self.delete_cascaded_bundle = m.get('DeleteCascadedBundle')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

