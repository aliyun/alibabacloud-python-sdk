# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListRenderingImagesResponseBodyImages] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The session list.
        self.images = images
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of matched sessions.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListRenderingImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        name: str = None,
        publish_time: str = None,
    ):
        # The image description.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.name = name
        # The publish time.
        self.publish_time = publish_time

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

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        return self

