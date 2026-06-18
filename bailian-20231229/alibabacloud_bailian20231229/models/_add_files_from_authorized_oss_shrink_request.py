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
        # Specifies the target category for file import. This is the `CategoryId` returned by the AddCategory operation. You can also obtain the category ID from the <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) - Files tab<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) - Files tab by clicking the ID icon next to the category name. You can also pass in default, which uses the system-created "Default Category".
        # 
        # This parameter is required.
        self.category_id = category_id
        # Category type. Optional. The default value is UNSTRUCTURED. Valid values:
        # - UNSTRUCTURED: Category used for building knowledge base scenarios.
        # 
        # <props="china">
        # 
        # > This operation does not support importing SESSION_FILE used for agent application [session interaction](https://help.aliyun.com/zh/model-studio/user-guide/file-interaction). Please use the **AddFile** operation to upload SESSION_FILE from local.
        # 
        # This parameter is required.
        self.category_type = category_type
        # The list of files to import. Up to 10 files can be uploaded at a time.
        # > Up to 10 files can be uploaded at a time.
        # >
        # 
        # This parameter is required.
        self.file_details_shrink = file_details_shrink
        # The OSS Bucket name. For details, see [Buckets](https://help.aliyun.com/document_detail/177682.html).
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # The region ID of the OSS Bucket. For how to obtain it, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.oss_region_id = oss_region_id
        # Whether to overwrite the same file in the category by OssKey. The default value is false, meaning no overwrite.
        self.over_write_file_by_oss_key = over_write_file_by_oss_key
        # The list of tags associated with the file. The default is empty, meaning the file is not associated with any tags. Up to 10 tags can be passed in.
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

