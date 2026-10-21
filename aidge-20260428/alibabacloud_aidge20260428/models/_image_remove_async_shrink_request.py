# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageRemoveAsyncShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        image_url: str = None,
        mask: str = None,
        non_object_remove_elements_shrink: str = None,
        object_remove_elements_shrink: str = None,
        position: str = None,
        user_image_shrink: str = None,
        user_text_shrink: str = None,
    ):
        # The business order ID of the caller. This ID is recorded when the request is accepted and returned as-is when you query the result of the asynchronous task.
        self.biz_id = biz_id
        # The URL of the original image. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256 × 256 and 3000 × 3000 pixels, and the file size cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The specific area to erase. This parameter must be used in conjunction with the editor. The input format is Run-Length Encoding (RLE).
        # If this parameter is specified, it takes precedence and the remove_non_product_area_elements and remove_product_area_elements parameters are ignored. This parameter is optional, but you must specify at least one of the following parameters: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, and UserImage.
        # If multiple parameters are specified, the priority is as follows: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.mask = mask
        # The list of element types to remove from the image background.
        self.non_object_remove_elements_shrink = non_object_remove_elements_shrink
        # The types of elements to remove from the image subject. Valid values:
        # - 1: Transparent text blocks.
        # - 2: Specific names.
        # - 3: Text.
        # - 4: Promotional stickers.
        # You can select multiple element types. This parameter is optional, but you must specify at least one of the following parameters: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, and UserImage.
        # If multiple parameters are specified, the priority is as follows: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        # For more information about each type, see the product documentation.
        # Image subject: the core product area in the image.
        self.object_remove_elements_shrink = object_remove_elements_shrink
        # The specific area to erase. This parameter must be used in conjunction with the editor. The input format is a four-point coordinate array, such as [xx,yy,zz,dd]. This parameter is optional, but you must specify at least one of the following parameters: ObjectRemoveElements, NonObjectRemoveElements, Mask, Position, UserText, and UserImage.
        # If multiple parameters are specified, the priority is as follows: UserImage > UserText > Position > Mask > ObjectRemoveElements = NonObjectRemoveElements.
        self.position = position
        # The list of URLs for user-specified image elements to erase.
        self.user_image_shrink = user_image_shrink
        # The list of user-specified text strings to erase.
        self.user_text_shrink = user_text_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.non_object_remove_elements_shrink is not None:
            result['NonObjectRemoveElements'] = self.non_object_remove_elements_shrink

        if self.object_remove_elements_shrink is not None:
            result['ObjectRemoveElements'] = self.object_remove_elements_shrink

        if self.position is not None:
            result['Position'] = self.position

        if self.user_image_shrink is not None:
            result['UserImage'] = self.user_image_shrink

        if self.user_text_shrink is not None:
            result['UserText'] = self.user_text_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('NonObjectRemoveElements') is not None:
            self.non_object_remove_elements_shrink = m.get('NonObjectRemoveElements')

        if m.get('ObjectRemoveElements') is not None:
            self.object_remove_elements_shrink = m.get('ObjectRemoveElements')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('UserImage') is not None:
            self.user_image_shrink = m.get('UserImage')

        if m.get('UserText') is not None:
            self.user_text_shrink = m.get('UserText')

        return self

