# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SendFileRequest(DaraModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        auto_install: bool = None,
        client_token: str = None,
        file_md_5: str = None,
        source_file_path: str = None,
        target_file_name: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # The IDs of one or more cloud phone instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to automatically install the application after the file is uploaded.
        self.auto_install = auto_install
        # A client-generated token that ensures request idempotence and prevents duplicate submissions. The token can contain up to 100 characters.
        self.client_token = client_token
        self.file_md_5 = file_md_5
        # The destination path on the cloud phone.
        # 
        # > If `UploadType` is `OSS` or `OSS_BRIDGED`, `SourceFilePath` must specify a directory, for example, `/sdcard/Download/`. If `UploadType` is `DOWNLOAD_URL`, `SourceFilePath` must specify a full file path, for example, `/sdcard/Download/MyFile.txt`.
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The name for the destination file on the cloud phone.
        # 
        # > This parameter is optional and takes effect only when `UploadType` is set to `OSS` or `OSS_BRIDGED`. If you specify this parameter, the file is saved with this name in the path specified by `SourceFilePath`. If you leave this parameter empty, the source file name is used. This parameter is ignored when `UploadType` is set to `DOWNLOAD_URL`.
        self.target_file_name = target_file_name
        # The service endpoint of Object Storage Service (OSS). This parameter is required if `UploadType` is `OSS` or `OSS_BRIDGED`.
        # 
        # > If the cloud phone instance and the OSS bucket are in the same region, you can specify an internal endpoint to accelerate data transfer and avoid public data transfer costs. For example, the internal endpoint for the China (Hangzhou) region is `oss-cn-hangzhou-internal.aliyuncs.com`. For a complete list of endpoints, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        self.upload_endpoint = upload_endpoint
        # The storage type of the source file. Valid values:
        # 
        # - **OSS**: The file is stored in Object Storage Service (OSS).
        # 
        # - **DOWNLOAD_URL**: The file is accessible via a public download link.
        # 
        # - **OSS_BRIDGED**: The service first downloads the file from a public download link to an internal OSS bucket, and then distributes it to the cloud phone instances over the internal network.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # - If `UploadType` is `OSS`, this parameter specifies the URI of the source object in Object Storage Service (OSS).
        # 
        # > The URI must be in the `oss://<bucket-name>/<object-key>` format. The specified OSS bucket name must have the `cloudphone-saved-bucket-` prefix, for example, `cloudphone-saved-bucket-example`.
        # 
        # - If `UploadType` is `DOWNLOAD_URL` or `OSS_BRIDGED`, this parameter specifies the public download link of the source file.
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

        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path

        if self.target_file_name is not None:
            result['TargetFileName'] = self.target_file_name

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

        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')

        if m.get('TargetFileName') is not None:
            self.target_file_name = m.get('TargetFileName')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

