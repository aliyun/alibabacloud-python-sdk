# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentretailvision20260506 import models as main_models
from darabonba.model import DaraModel

class ImportProductsRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        extra_images: List[str] = None,
        image_title: str = None,
        item_unique_id: str = None,
        main_image: List[str] = None,
        multi_view_images: List[main_models.ImportProductsRequestMultiViewImages] = None,
    ):
        # The device ID. This ID is used to establish an association between the device and product vectors.
        self.device_id = device_id
        # The list of additional image URLs that can be provided.
        self.extra_images = extra_images
        # The product title.
        self.image_title = image_title
        # The product ID assigned by the business party. This ID must be unique within the same business party.
        self.item_unique_id = item_unique_id
        # The list of main product image URLs. At least one URL is required.
        self.main_image = main_image
        # The list of multi-angle product images.
        self.multi_view_images = multi_view_images

    def validate(self):
        if self.multi_view_images:
            for v1 in self.multi_view_images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.extra_images is not None:
            result['ExtraImages'] = self.extra_images

        if self.image_title is not None:
            result['ImageTitle'] = self.image_title

        if self.item_unique_id is not None:
            result['ItemUniqueId'] = self.item_unique_id

        if self.main_image is not None:
            result['MainImage'] = self.main_image

        result['MultiViewImages'] = []
        if self.multi_view_images is not None:
            for k1 in self.multi_view_images:
                result['MultiViewImages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('ExtraImages') is not None:
            self.extra_images = m.get('ExtraImages')

        if m.get('ImageTitle') is not None:
            self.image_title = m.get('ImageTitle')

        if m.get('ItemUniqueId') is not None:
            self.item_unique_id = m.get('ItemUniqueId')

        if m.get('MainImage') is not None:
            self.main_image = m.get('MainImage')

        self.multi_view_images = []
        if m.get('MultiViewImages') is not None:
            for k1 in m.get('MultiViewImages'):
                temp_model = main_models.ImportProductsRequestMultiViewImages()
                self.multi_view_images.append(temp_model.from_map(k1))

        return self

class ImportProductsRequestMultiViewImages(DaraModel):
    def __init__(
        self,
        angle: str = None,
        url: str = None,
    ):
        # The digital human angle. Valid values:
        # 
        # - 0: front view, which is the default angle
        # - 1: left side at 30 degrees
        # - 2: right side at 30 degrees
        # 
        # For a preview of each angle, refer to [3D Digital Human Video Synthesis User Guide](https://help.aliyun.com/document_detail/447834.html#a989eb5075t9y).
        self.angle = angle
        # The task URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['Angle'] = self.angle

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

