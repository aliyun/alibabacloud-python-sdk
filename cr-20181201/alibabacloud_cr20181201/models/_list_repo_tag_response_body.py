# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoTagResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        images: List[main_models.ListRepoTagResponseBodyImages] = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The return value.
        self.code = code
        # The images.
        self.images = images
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.code is not None:
            result['Code'] = self.code

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListRepoTagResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoTagResponseBodyImages(DaraModel):
    def __init__(
        self,
        digest: str = None,
        image_create: str = None,
        image_id: str = None,
        image_size: int = None,
        image_update: str = None,
        status: str = None,
        tag: str = None,
    ):
        # The digest of the image.
        self.digest = digest
        # The time when the image was created.
        self.image_create = image_create
        # The ID of the image.
        self.image_id = image_id
        # The size of the image.
        self.image_size = image_size
        # The time when the image was last updated.
        self.image_update = image_update
        # The status of the image.
        self.status = status
        # The tag of the image.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.image_create is not None:
            result['ImageCreate'] = self.image_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

