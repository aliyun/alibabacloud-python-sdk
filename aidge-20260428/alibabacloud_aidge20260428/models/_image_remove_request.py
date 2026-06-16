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
        # URL of the image to be processed (mutually exclusive with ImageBase64)
        # 
        # This parameter is required.
        self.image_url = image_url
        # Specific removal area in RLE format. If provided, this takes priority and the remove parameters are ignored
        self.mask = mask
        # Elements to remove from the non-subject area of the image (1=transparent text blocks; 2=specific names; 3=text; 4=blemishes). Multiple selections allowed
        self.non_object_remove_elements = non_object_remove_elements
        # Elements to remove from the image subject (1=transparent text blocks; 2=specific names; 3=text; 4=blemishes). Multiple selections allowed
        # 
        # This parameter is required.
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

