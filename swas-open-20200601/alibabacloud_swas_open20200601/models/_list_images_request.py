# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImagesRequest(DaraModel):
    def __init__(
        self,
        image_ids: str = None,
        image_type: str = None,
        region_id: str = None,
    ):
        # The image IDs. The value can be a JSON array that consists of up to 50 image IDs. Format: `["xxx", "yyy", … "zzz"]`. Separate multiple image IDs with commas (,).
        self.image_ids = image_ids
        # The type of the images. Valid values:
        # 
        # - system: OS images
        # 
        # - app: application images
        # 
        # - custom: custom images
        self.image_type = image_type
        # The region ID of the images. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
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
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

