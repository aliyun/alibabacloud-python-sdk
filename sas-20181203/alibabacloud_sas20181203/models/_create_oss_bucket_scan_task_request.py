# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOssBucketScanTaskRequest(DaraModel):
    def __init__(
        self,
        all_key_prefix: bool = None,
        bucket_name_list: List[str] = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        exclude_key_suffix_list: List[str] = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        scan_mode: int = None,
        source: str = None,
    ):
        # Specifies whether to match all prefixes. If this parameter is set to true, the KeyPrefixList parameter does not take effect.
        self.all_key_prefix = all_key_prefix
        # The list of bucket names.
        # 
        # This parameter is required.
        self.bucket_name_list = bucket_name_list
        # The maximum number of files to decompress. The minimum value is 1 and the maximum value is 1000. When the maximum number of decompressed files is exceeded, the decompression operation ends immediately. The detection of files that have already been decompressed is not affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression layers when multiple levels of compressed packages are nested. The minimum value is 1 and the maximum value is 5. When the maximum number of decompression layers is exceeded, the decompression operation ends immediately. The detection of files that have already been decompressed is not affected.
        self.decompress_max_layer = decompress_max_layer
        # The list of decryption types.
        self.decryption_list = decryption_list
        # The list of file suffixes to exclude from detection.
        self.exclude_key_suffix_list = exclude_key_suffix_list
        # The prefix list of files.
        self.key_prefix_list = key_prefix_list
        # The list of file suffixes.
        self.key_suffix_list = key_suffix_list
        # Specifies that only files whose last modification time is after the specified timestamp are detected. Unit: milliseconds.
        self.last_modified_start_time = last_modified_start_time
        # The detection mode. Valid values:
        # 
        # - **1**: Full file detection.
        # 
        # - **2**: Incremental file detection.
        # 
        # This parameter is required.
        self.scan_mode = scan_mode
        # The business source. Valid values:
        # - **OSS**: OSS
        # - **NAS**: NAS
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_key_prefix is not None:
            result['AllKeyPrefix'] = self.all_key_prefix

        if self.bucket_name_list is not None:
            result['BucketNameList'] = self.bucket_name_list

        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count

        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer

        if self.decryption_list is not None:
            result['DecryptionList'] = self.decryption_list

        if self.exclude_key_suffix_list is not None:
            result['ExcludeKeySuffixList'] = self.exclude_key_suffix_list

        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list

        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list

        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')

        if m.get('BucketNameList') is not None:
            self.bucket_name_list = m.get('BucketNameList')

        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')

        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')

        if m.get('DecryptionList') is not None:
            self.decryption_list = m.get('DecryptionList')

        if m.get('ExcludeKeySuffixList') is not None:
            self.exclude_key_suffix_list = m.get('ExcludeKeySuffixList')

        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')

        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')

        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

