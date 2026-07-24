# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListImagesFromLibResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        http_status_code: int = None,
        items: List[main_models.ListImagesFromLibResponseBodyItems] = None,
        msg: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code, which is consistent with the HTTP status code.
        self.code = code
        # The current page number.
        self.current_page = current_page
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The data on the current page.
        self.items = items
        # The further description of the error code.
        self.msg = msg
        # The number of entries per page.
        self.page_size = page_size
        # The backend-assigned ID that uniquely identifies a request. This ID can be used for troubleshooting.
        self.request_id = request_id
        # The success flag.
        self.success = success
        # The total number of images.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListImagesFromLibResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListImagesFromLibResponseBodyItems(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        image_id: str = None,
        image_url: str = None,
        thumbnail_url: str = None,
    ):
        # The creation time. Format: YYYY-MM-DD HH:mm:ss.
        self.gmt_create = gmt_create
        # The image ID.
        self.image_id = image_id
        # The URL of the image.
        self.image_url = image_url
        # The URL of the thumbnail.
        self.thumbnail_url = thumbnail_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        return self

