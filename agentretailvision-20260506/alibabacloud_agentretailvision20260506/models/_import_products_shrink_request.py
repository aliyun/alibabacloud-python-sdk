# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportProductsShrinkRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        extra_images_shrink: str = None,
        image_title: str = None,
        item_unique_id: str = None,
        main_image_shrink: str = None,
        multi_view_images_shrink: str = None,
    ):
        self.device_id = device_id
        self.extra_images_shrink = extra_images_shrink
        self.image_title = image_title
        self.item_unique_id = item_unique_id
        self.main_image_shrink = main_image_shrink
        self.multi_view_images_shrink = multi_view_images_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.extra_images_shrink is not None:
            result['ExtraImages'] = self.extra_images_shrink

        if self.image_title is not None:
            result['ImageTitle'] = self.image_title

        if self.item_unique_id is not None:
            result['ItemUniqueId'] = self.item_unique_id

        if self.main_image_shrink is not None:
            result['MainImage'] = self.main_image_shrink

        if self.multi_view_images_shrink is not None:
            result['MultiViewImages'] = self.multi_view_images_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('ExtraImages') is not None:
            self.extra_images_shrink = m.get('ExtraImages')

        if m.get('ImageTitle') is not None:
            self.image_title = m.get('ImageTitle')

        if m.get('ItemUniqueId') is not None:
            self.item_unique_id = m.get('ItemUniqueId')

        if m.get('MainImage') is not None:
            self.main_image_shrink = m.get('MainImage')

        if m.get('MultiViewImages') is not None:
            self.multi_view_images_shrink = m.get('MultiViewImages')

        return self

