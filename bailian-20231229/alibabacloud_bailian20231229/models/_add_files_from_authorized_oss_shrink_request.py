# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFilesFromAuthorizedOssShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        file_details_shrink: str = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        over_write_file_by_oss_key: bool = None,
        tags_shrink: str = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.category_type = category_type
        # This parameter is required.
        self.file_details_shrink = file_details_shrink
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # This parameter is required.
        self.oss_region_id = oss_region_id
        self.over_write_file_by_oss_key = over_write_file_by_oss_key
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.file_details_shrink is not None:
            result['FileDetails'] = self.file_details_shrink

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        if self.over_write_file_by_oss_key is not None:
            result['OverWriteFileByOssKey'] = self.over_write_file_by_oss_key

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('FileDetails') is not None:
            self.file_details_shrink = m.get('FileDetails')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        if m.get('OverWriteFileByOssKey') is not None:
            self.over_write_file_by_oss_key = m.get('OverWriteFileByOssKey')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

