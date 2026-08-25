# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListServerIdeImagesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        paging_info: main_models.ListServerIdeImagesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The maximum number of records returned in this response.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListServerIdeImagesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListServerIdeImagesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        images: List[main_models.ListServerIdeImagesResponseBodyPagingInfoImages] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of images available for personal development environments.
        self.images = images
        # The current page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records that match the filter conditions.
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ListServerIdeImagesResponseBodyPagingInfoImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServerIdeImagesResponseBodyPagingInfoImages(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        image_url: str = None,
        status: str = None,
    ):
        # The image ID used by the instance.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image URL.
        self.image_url = image_url
        # The image status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

