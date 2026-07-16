# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FetchFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        client_token: str = None,
        source_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # A list of cloud phone instance IDs.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # A client-generated token, up to 100 characters long, that ensures the idempotency of the request.
        self.client_token = client_token
        # The path of the file or folder to fetch from the cloud phone.
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The endpoint for uploading files to OSS.
        # 
        # > If the cloud phone and the destination OSS bucket are in the same region, you can use an internal endpoint to accelerate the transfer and avoid public network charges. For example, in the China (Hangzhou) region, use `oss-cn-hangzhou-internal.aliyuncs.com`. For a complete list of endpoints, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.upload_endpoint = upload_endpoint
        # The type of storage service for the fetched file.
        # 
        # > Currently, only Object Storage Service (OSS) is supported.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # The destination URL in OSS.
        # 
        # > The destination bucket name must be prefixed with `cloudphone-saved-bucket-`. For example, `cloudphone-saved-bucket-example`. You must also create a folder in the bucket to serve as the destination directory. The `UploadUrl` must follow the format: `oss://<bucket_name>/<folder_name>`.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

