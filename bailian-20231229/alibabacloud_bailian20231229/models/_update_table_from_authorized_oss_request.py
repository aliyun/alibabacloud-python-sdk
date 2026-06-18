# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTableFromAuthorizedOssRequest(DaraModel):
    def __init__(
        self,
        oss_bucket: str = None,
        oss_key: str = None,
        oss_region_id: str = None,
        update_mode: str = None,
    ):
        # Name of the OSS bucket. For details, see [bucket](https://help.aliyun.com/document_detail/177682.html).
        # 
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # Object key of the file in the OSS bucket. For details, see [object naming](https://help.aliyun.com/document_detail/273129.html).
        # 
        # This parameter is required.
        self.oss_key = oss_key
        # Region ID of the OSS bucket. For details, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.oss_region_id = oss_region_id
        # Update mode. Valid values: APPEND and OVERWRITE.
        # 
        # This parameter is required.
        self.update_mode = update_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        if self.update_mode is not None:
            result['UpdateMode'] = self.update_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        if m.get('UpdateMode') is not None:
            self.update_mode = m.get('UpdateMode')

        return self

