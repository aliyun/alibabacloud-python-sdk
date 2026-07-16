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
        # Specifies whether to decompress the archive for detection. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        # 
        # > This parameter is not supported when `Type` is set to `6`.
        self.decompress = decompress
        # The maximum number of files that can be decompressed from an archive. The maximum value is 1000.
        # 
        # This parameter is required if you set `Decompress` to `true`.
        # 
        # > This parameter is not supported when `Type` is set to `6`.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression layers for nested archives. The maximum value is 5.
        # 
        # This parameter is required if you set `Decompress` to `true`.
        # 
        # > This parameter is not supported when `Type` is set to `6`.
        self.decompress_max_layer = decompress_max_layer
        # The download link for the file. You can provide a public URL to trigger file detection without uploading the file.
        # 
        # > Skill archives can be submitted only by providing a download link. Therefore, this parameter is required when `Type` is set to `6`.
        self.download_url = download_url
        # The unique identifier of the file.
        # 
        # This parameter is required if `Type` is `0`. Its value must be the MD5 or SHA-256 hash of the file.
        # 
        # If you set `Type` to `6`, you do not need to specify this parameter. The operation returns the file\\"s unique identifier in the response.
        self.hash_key = hash_key
        # The storage key of the file in an Object Storage Service (OSS) bucket.
        # 
        # If you submit the file by using the `DownloadUrl` parameter, you can leave this parameter empty. To obtain the value of this parameter, call the [CreateFileDetectUploadUrl](~~CreateFileDetectUploadUrl~~) operation.
        # 
        # > This parameter is not supported when `Type` is set to `6`.
        self.oss_key = oss_key
        # The IP address of the source.
        self.source_ip = source_ip
        # The type of the file to detect. Valid values:
        # 
        # - **0**: Malicious file detection
        # 
        # - **6**: Skill archive detection
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

