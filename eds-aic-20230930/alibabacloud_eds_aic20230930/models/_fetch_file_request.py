# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FetchFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        source_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # The IDs of the cloud phone instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # The path to the file that you want to pull from the cloud phone instance.
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The endpoint of the OSS bucket in which you want to store the pulled file.
        # 
        # >  Set the value to an internal endpoint when the cloud phone instance and the OSS bucket are in the same region to improve upload speed without incurring public traffic fees. Sample endpoint: `oss-cn-hangzhou-internal.aliyuncs.com`. For more information, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.upload_endpoint = upload_endpoint
        # The type of the storage service.
        # 
        # >  Currently, only OSS is supported.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # The OSS URL of the pulled file.
        # 
        # >  The OSS bucket name must start with "cloudphone-saved-bucket-", for example, "cloudphone-saved-bucket-example". You must also create an OSS directory to store the backup data. Set the value for UploadUrl in this format: oss://\\<BucketName>/\\<OSSDirectoryName>.
        # 
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list

        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path

        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')

        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

