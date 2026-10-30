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
        # The list of instances.
        # 
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # Specifies whether to automatically install the uploaded application.
        self.auto_install = auto_install
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. The token can be up to 100 characters in length.
        self.client_token = client_token
        # The MD5 value of the input file.
        self.file_md_5 = file_md_5
        # The upload path inside the cloud phone to which the file is uploaded.
        # 
        # > If UploadType is OSS or OSS_BRIDGED, the upload path SourceFilePath inside the cloud phone must be a directory, such as /sdcard/Download. If UploadType is DOWNLOAD_URL, the upload path SourceFilePath inside the cloud phone must be a file, such as /sdcard/Download/MyFile.txt.
        # >
        # 
        # This parameter is required.
        self.source_file_path = source_file_path
        # The name of the file uploaded from OSS to the cloud phone.
        # 
        # > If UploadType is OSS or OSS_BRIDGED, the TargetFileName parameter is optional. If TargetFileName is empty, the original file name is retained when the OSS file is uploaded to the cloud phone. If TargetFileName is not empty, the file name in the SourceFilePath directory on the cloud phone is set to the value of TargetFileName. If UploadType is DOWNLOAD_URL, the TargetFileName parameter does not take effect.
        # >
        self.target_file_name = target_file_name
        # The service domain name for uploading files to OSS. This parameter is required when UploadType is set to OSS or OSS_BRIDGED.
        # 
        # > If the cloud phone and the OSS bucket are in the same region, you can use an internal endpoint to accelerate the transmission speed and avoid Internet traffic fees. For example, the internal endpoint for the China (Hangzhou) region is `oss-cn-hangzhou-internal.aliyuncs.com`. For more information about the mapping between regions and endpoints, see [Regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        self.upload_endpoint = upload_endpoint
        # The storage type of the file to be uploaded.
        # 
        # - OSS: The file to be uploaded is an OSS resource.
        # - DOWNLOAD_URL: The file to be uploaded is a public download URL.
        # - OSS_BRIDGED: The file is synchronized to OSS through a public download URL and then distributed to cloud phone instances over the OSS internal network.
        # 
        # This parameter is required.
        self.upload_type = upload_type
        # - If UploadType is OSS, UploadUrl is the cloud address of the file uploaded to OSS.
        # > The OSS bucket name must start with the prefix "cloudphone-saved-bucket-", such as "cloudphone-saved-bucket-example". You must create an OSS folder as the backup directory. The format of UploadUrl is "oss://" + "Bucket name" + "/" + "Folder name" + "Uploaded file name".
        # - If UploadType is DOWNLOAD or OSS_BRIDGED, UploadUrl is the public download URL of the file.
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

