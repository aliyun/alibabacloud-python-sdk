# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ScanOssObjectV1Request(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        lang: str = None,
        object_key_list: List[str] = None,
        service_region_id: str = None,
        template_id: int = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The objects in the OSS bucket that you want to scan. You can specify up to 50 objects at a time.
        # 
        # This parameter is required.
        self.object_key_list = object_key_list
        # The ID of the region in which the OSS bucket is located.
        # 
        # This parameter is required.
        self.service_region_id = service_region_id
        # The ID of the industry-specific classification template.
        # 
        # >  You can call the **DescribeCategoryTemplateList** operation to query industry-specific classification templates. If you do not specify this parameter, the system automatically uses the main template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object_key_list is not None:
            result['ObjectKeyList'] = self.object_key_list

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ObjectKeyList') is not None:
            self.object_key_list = m.get('ObjectKeyList')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

