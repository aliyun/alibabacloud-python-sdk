# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_acc20240402 import models as main_models
from darabonba.model import DaraModel

class ListImageCachesResponseBody(DaraModel):
    def __init__(
        self,
        image_caches: List[main_models.ListImageCachesResponseBodyImageCaches] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.image_caches = image_caches
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.image_caches:
            for v1 in self.image_caches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageCaches'] = []
        if self.image_caches is not None:
            for k1 in self.image_caches:
                result['ImageCaches'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_caches = []
        if m.get('ImageCaches') is not None:
            for k1 in m.get('ImageCaches'):
                temp_model = main_models.ListImageCachesResponseBodyImageCaches()
                self.image_caches.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListImageCachesResponseBodyImageCaches(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        images: List[str] = None,
        ready_time: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.image_cache_id = image_cache_id
        self.image_cache_name = image_cache_name
        self.images = images
        self.ready_time = ready_time
        self.resource_group_id = resource_group_id
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id

        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name

        if self.images is not None:
            result['Images'] = self.images

        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')

        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

