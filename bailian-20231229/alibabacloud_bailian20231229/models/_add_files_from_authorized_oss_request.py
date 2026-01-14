# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddFilesFromAuthorizedOssRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        file_details: List[main_models.AddFilesFromAuthorizedOssRequestFileDetails] = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        over_write_file_by_oss_key: bool = None,
        tags: List[str] = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.category_type = category_type
        # This parameter is required.
        self.file_details = file_details
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # This parameter is required.
        self.oss_region_id = oss_region_id
        self.over_write_file_by_oss_key = over_write_file_by_oss_key
        self.tags = tags

    def validate(self):
        if self.file_details:
            for v1 in self.file_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        result['FileDetails'] = []
        if self.file_details is not None:
            for k1 in self.file_details:
                result['FileDetails'].append(k1.to_map() if k1 else None)

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        if self.over_write_file_by_oss_key is not None:
            result['OverWriteFileByOssKey'] = self.over_write_file_by_oss_key

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        self.file_details = []
        if m.get('FileDetails') is not None:
            for k1 in m.get('FileDetails'):
                temp_model = main_models.AddFilesFromAuthorizedOssRequestFileDetails()
                self.file_details.append(temp_model.from_map(k1))

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        if m.get('OverWriteFileByOssKey') is not None:
            self.over_write_file_by_oss_key = m.get('OverWriteFileByOssKey')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class AddFilesFromAuthorizedOssRequestFileDetails(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        oss_key: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        return self

