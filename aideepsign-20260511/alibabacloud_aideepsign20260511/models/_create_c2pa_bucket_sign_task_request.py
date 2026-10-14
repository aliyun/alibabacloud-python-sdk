# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateC2paBucketSignTaskRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_region_id: str = None,
        software_agent: str = None,
        source_prefix: str = None,
        source_type: str = None,
    ):
        # The name of the user OSS bucket. You must authorize the service-linked role AliyunServiceRoleForAIDeepSign to access the bucket in advance.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The region of the user OSS bucket. It must be consistent with the actual region of the bucket.
        # 
        # This parameter is required.
        self.bucket_region_id = bucket_region_id
        # The optional name of the software that generated the content. This parameter is not supported in the current version.
        self.software_agent = software_agent
        # The source object prefix. It must be `ai-deepsign/` or its subdirectory. The service recursively processes objects under this prefix.
        # 
        # This parameter is required.
        self.source_prefix = source_prefix
        # The optional content source type. This parameter is not supported in the current version.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.bucket_region_id is not None:
            result['BucketRegionId'] = self.bucket_region_id

        if self.software_agent is not None:
            result['SoftwareAgent'] = self.software_agent

        if self.source_prefix is not None:
            result['SourcePrefix'] = self.source_prefix

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('BucketRegionId') is not None:
            self.bucket_region_id = m.get('BucketRegionId')

        if m.get('SoftwareAgent') is not None:
            self.software_agent = m.get('SoftwareAgent')

        if m.get('SourcePrefix') is not None:
            self.source_prefix = m.get('SourcePrefix')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

