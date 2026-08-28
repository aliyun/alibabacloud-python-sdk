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
        position: str = None,
        user_image: List[str] = None,
        user_text: List[str] = None,
    ):
        # The URL of the original image. The image must be in JPG, JPEG, PNG, BMP, or WEBP format, with a resolution between 256 × 256 and 3000 × 3000 pixels, and a file size no larger than 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The specific removal area. This parameter must be used with the editor. The input format is RLE.
        # If provided, this takes priority and the remove_non_product_area_elements and remove_product_area_elements parameters are ignored. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.mask = mask
        # The elements to remove from the non-subject area of the image (1=transparent text blocks, 2=specific names, 3=text, 4=visual clutter). Multiple element types can be selected. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        # Refer to the product description for details on each type.
        self.non_object_remove_elements = non_object_remove_elements
        # The elements to remove from the image subject (1=transparent text blocks, 2=specific names, 3=text, 4=visual clutter). Multiple element types can be selected. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        # Refer to the product description for details on each type.
        # Image subject: The core product area in the image.
        self.object_remove_elements = object_remove_elements
        # The specific removal area. This parameter must be used with the editor. The input format is four-point coordinates [xx,yy,zz,dd]. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.position = position
        # The user-specified image element links to remove. Multiple image links are supported. The input format is ["https://ae01.alicdn.com/kf/S342f0070dc9f4be09a6cbed34e90dc8fs.jpg","https://ae01.alicdn.com/kf/S342f0070dc9f4be09a6cbed34e90dc8fs.jpg"]. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.user_image = user_image
        # The user-specified text to remove. Multiple text inputs are supported. The input format is ["xx","yy"]. This parameter is not required, but at least one of the following parameters must be specified: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, or UserImage.
        # When multiple parameters are specified, the priority order is: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.user_text = user_text

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

        if self.position is not None:
            result['Position'] = self.position

        if self.user_image is not None:
            result['UserImage'] = self.user_image

        if self.user_text is not None:
            result['UserText'] = self.user_text

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

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('UserImage') is not None:
            self.user_image = m.get('UserImage')

        if m.get('UserText') is not None:
            self.user_text = m.get('UserText')

        return self

