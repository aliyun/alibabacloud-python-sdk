# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageSharePermissionRequest(DaraModel):
    def __init__(
        self,
        aliyun_id: int = None,
        image_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliyun_id = aliyun_id
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The page number. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

