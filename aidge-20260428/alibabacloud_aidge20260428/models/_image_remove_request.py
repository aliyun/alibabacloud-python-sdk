# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ImageRemoveRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        mask: str = None,
        non_object_remove_elements: List[int] = None,
        object_remove_elements: List[int] = None,
    ):
        # The URL of the image to process. This parameter is mutually exclusive with ImageBase64. You must specify one of them.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The specific erasure region in RLE format. If this parameter is specified, it takes priority and the remove parameters are ignored.
        self.mask = mask
        # The elements to remove from the non-subject area of the image. Valid values:
        # - 1: transparent text block
        # - 2: specific name
        # - 3: text
        # - 4: image blemish
        # 
        # You can specify multiple values.
        self.non_object_remove_elements = non_object_remove_elements
        # The elements to remove from the image subject area. Valid values:
        # - 1: transparent text block
        # - 2: specific name
        # - 3: text
        # - 4: image blemish
        # 
        # You can specify multiple values.
        self.object_remove_elements = object_remove_elements

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.non_object_remove_elements is not None:
            result['NonObjectRemoveElements'] = self.non_object_remove_elements

        if self.object_remove_elements is not None:
            result['ObjectRemoveElements'] = self.object_remove_elements

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('NonObjectRemoveElements') is not None:
            self.non_object_remove_elements = m.get('NonObjectRemoveElements')

        if m.get('ObjectRemoveElements') is not None:
            self.object_remove_elements = m.get('ObjectRemoveElements')

        return self

