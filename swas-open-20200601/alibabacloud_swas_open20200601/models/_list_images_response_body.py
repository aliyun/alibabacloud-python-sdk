# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListImagesResponseBodyImages] = None,
        request_id: str = None,
    ):
        # Details of the queried images.
        self.images = images
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        platform: str = None,
    ):
        # The description of the image.
        self.description = description
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The type of the image. Valid values:
        # 
        # - system
        # 
        # - app
        # 
        # - custom
        self.image_type = image_type
        # The operating system type of the image. Valid values:
        # 
        # - Linux
        # 
        # - Windows
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.platform is not None:
            result['Platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        return self

