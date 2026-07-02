# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOssObjectDetailV2Request(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        id: str = None,
        lang: str = None,
        object_key: str = None,
        service_region_id: str = None,
        template_id: int = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The unique ID of the OSS object.
        # 
        # > Call the [DescribeOssObjects](https://help.aliyun.com/document_detail/410152.html) operation to obtain the ID.
        self.id = id
        # The language of the content within the request and response. Default value: **en_us**. Valid values:
        # 
        # - **en_us**: Simplified Chinese
        # 
        # - **en_us**: English (US)
        self.lang = lang
        # The full name of the object stored in OSS.
        self.object_key = object_key
        # The ID of the region where the service is enabled. This is also the region where the bucket is located.
        self.service_region_id = service_region_id
        # The ID of the industry-specific template.
        # 
        # > Call the [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html) operation to obtain the ID of the industry-specific template.
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

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

