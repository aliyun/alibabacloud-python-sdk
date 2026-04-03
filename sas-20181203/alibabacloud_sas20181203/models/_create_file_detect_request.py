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
        # Whether to decompress or not. Valid values:
        # 
        # - true: To decompress.
        # - false: Not to decompress.
        self.decompress = decompress
        # The maximum number of files for decompression. The minimum value is 1, and the maximum value is 1000. If the decompression level exceeds the maximum, the decompression operation will be terminated, but the detection of decompressed files will not be affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum level of decompression when dealing with nested compressed files with multiple levels. The minimum value is 1, and the maximum value is 5. If the decompression level exceeds the maximum, the decompression operation will be terminated, but the detection of decompressed files will not be affected.
        self.decompress_max_layer = decompress_max_layer
        # The URL that is used to download the file. You can specify this parameter to trigger file detection without the need to upload the file in advance.
        self.download_url = download_url
        # The identifier of the file. Only MD5 hash values are supported.
        self.hash_key = hash_key
        # The key of the file that is stored in the Object Storage Service (OSS) bucket. You can call the [CreateFileDetectUploadUrl](~~CreateFileDetectUploadUrl~~) operation to query the keys of files.
        self.oss_key = oss_key
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the file. Valid values:
        # 
        # *   **0**: unknown files
        # *   **1**: binary files
        # *   **2**: webshell files
        # *   **4**: script files
        # 
        # >  If you do not know the type of the file, set this parameter to 0.
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

