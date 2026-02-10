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
    ):
        # Specifies whether to match the prefixes of all objects.
        self.all_key_prefix = all_key_prefix
        # The names of the buckets.
        # 
        # This parameter is required.
        self.bucket_name_list = bucket_name_list
        # The maximum number of objects that can be extracted during decompression. Valid values: 1 to 1000. If the maximum number of objects that can be extracted is reached, the decompression operation immediately ends and the detection of extracted objects is not affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression levels when multi-level packages are decompressed. Valid values: 1 to 5. If the maximum number of decompression levels is reached, the decompression operation immediately ends and the detection of extracted objects is not affected.
        self.decompress_max_layer = decompress_max_layer
        # The decryption methods.
        self.decryption_list = decryption_list
        # The suffixes of the objects that you do not want to check.
        self.exclude_key_suffix_list = exclude_key_suffix_list
        # The prefixes of the objects.
        self.key_prefix_list = key_prefix_list
        # The suffixes of the objects that you want to check.
        self.key_suffix_list = key_suffix_list
        # The timestamp when the object was last modified. The time must be later than the timestamp that you specify. Unit: milliseconds.
        self.last_modified_start_time = last_modified_start_time
        # The check mode. Valid values:
        # 
        # *   **1**: checks all objects in the bucket.
        # *   **2**: checks only new objects in the bucket.
        # 
        # This parameter is required.
        self.scan_mode = scan_mode

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

        return self

