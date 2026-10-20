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
        # The ID of the destination category for the imported files. This is the CategoryId returned by the AddCategory operation. You can also obtain the category ID by clicking the ID icon next to the category name on the <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) > Files tab<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) > Files tab. You can set this parameter to default to use the default category created by the system.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The category type. This parameter is optional. Default value: UNSTRUCTURED. Valid values:
        # - UNSTRUCTURED: category, used for building knowledge bases.
        # 
        # <props="china">
        # 
        # > This operation does not support importing SESSION_FILE for [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction) in agent applications. Use the **AddFile** operation to upload SESSION_FILE from your local machine.
        # 
        # This parameter is required.
        self.category_type = category_type
        # The list of files to import. You can upload up to 10 files at a time.
        # > You can upload up to 10 files at a time.
        # >
        # 
        # This parameter is required.
        self.file_details_shrink = file_details_shrink
        # The name of the OSS bucket. For more information, see [Buckets](https://help.aliyun.com/document_detail/177682.html). Before you import data from OSS for the first time, you must complete the authorization as prompted in the Model Studio console and add a tag with the key bailian-datahub-access and the value read to the destination bucket. You must also authorize the OSS service-linked role as prompted in the Model Studio console (service name: datahub.sfm.aliyuncs.com).
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # The region ID of the OSS bucket. For more information about how to obtain the ID, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.oss_region_id = oss_region_id
        # Specifies whether to overwrite identical files in the category based on the OssKey. Default value: false, which means identical files are not overwritten.
        self.over_write_file_by_oss_key = over_write_file_by_oss_key
        # The list of tags associated with the file. Default value: empty, which means the file is not associated with any tags. You can specify up to 10 tags.
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

