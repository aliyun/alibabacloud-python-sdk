# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[main_models.DescribeTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The details about the tag keys.
        self.tag_keys = tag_keys
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tag_keys:
            for v1 in self.tag_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k1 in self.tag_keys:
                result['TagKeys'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k1 in m.get('TagKeys'):
                temp_model = main_models.DescribeTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTagKeysResponseBodyTagKeys(DaraModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        # The number of Anti-DDoS Proxy (Chinese Mainland) instances to which the tag key is added.
        self.tag_count = tag_count
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

