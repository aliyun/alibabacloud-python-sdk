# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetImageRequest(DaraModel):
    def __init__(
        self,
        additional_region_ids: List[str] = None,
        image_category: str = None,
        image_id: str = None,
        image_type: str = None,
    ):
        self.additional_region_ids = additional_region_ids
        # The source of the image. Valid values:
        # 
        # *   Public: public images provided by Alibaba Cloud.
        # *   Custom: the custom image that you added.
        self.image_category = image_category
        # The image ID.
        self.image_id = image_id
        # The type of the images. Valid values:
        # 
        # *   VM: virtual machine image.
        # *   Container: the container image.
        # 
        # Default value: VM
        self.image_type = image_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_region_ids is not None:
            result['AdditionalRegionIds'] = self.additional_region_ids

        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalRegionIds') is not None:
            self.additional_region_ids = m.get('AdditionalRegionIds')

        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        return self

