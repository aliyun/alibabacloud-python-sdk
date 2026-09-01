# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileDetectRequest(DaraModel):
    def __init__(
        self,
        decompress: bool = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        download_url: str = None,
        hash_key: str = None,
        oss_key: str = None,
        source_ip: str = None,
        type: int = None,
    ):
        # Specifies whether to identify and decompress compressed files. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.decompress = decompress
        # The maximum number of files to decompress. Maximum value: 1000.
        # 
        # This parameter is required when Decompress is set to true.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression layers when compressed files are nested within a compressed package. Maximum value: 5.
        # 
        # This parameter is required when Decompress is set to true.
        self.decompress_max_layer = decompress_max_layer
        # The download URL of the file. You can pass in a file download URL (public URL) to directly trigger file detection without uploading the file in advance.
        self.download_url = download_url
        # The unique identifier of the file. This parameter is required and must be the MD5 or SHA-256 of the file.
        self.hash_key = hash_key
        # The storage key of the file in the OSS bucket.
        # 
        # If you push the file for detection by using DownloadUrl, this parameter is optional. This parameter is obtained from the [CreateFileDetectUploadUrl](~~CreateFileDetectUploadUrl~~) operation.
        self.oss_key = oss_key
        # The IP address of the access source.
        self.source_ip = source_ip
        # The type of file to detect. Valid values:
        # 
        # - **0**: malicious file detection
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.decompress is not None:
            result['Decompress'] = self.decompress

        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count

        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Decompress') is not None:
            self.decompress = m.get('Decompress')

        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')

        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

