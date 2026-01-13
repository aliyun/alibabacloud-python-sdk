# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListImagesRequest(DaraModel):
    def __init__(
        self,
        image_category: str = None,
        image_ids: List[str] = None,
        image_names: List[str] = None,
        image_type: str = None,
        mode: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The source of the image. Valid values:
        # 
        # *   Public: public images provided by Alibaba Cloud.
        # *   Custom: the custom image that you added.
        self.image_category = image_category
        # The array of image IDs.
        self.image_ids = image_ids
        # The array of image names.
        self.image_names = image_names
        # The type of the images. Valid values:
        # 
        # *   VM: virtual machine image.
        # *   Container: the container image.
        # 
        # Default value: VM
        self.image_type = image_type
        # The query mode. Valid values:
        # 
        # *   List: queries the list of all corresponding image versions.
        # *   Merge: merges images to query the latest version list.
        self.mode = mode
        # The number of the page to return.\\
        # Default value: 1.
        self.page_number = page_number
        # The number of pieces per page.\\
        # Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.image_names is not None:
            result['ImageNames'] = self.image_names

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

