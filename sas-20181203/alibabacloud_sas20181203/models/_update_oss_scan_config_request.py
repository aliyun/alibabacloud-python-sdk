# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateOssScanConfigRequest(DaraModel):
    def __init__(
        self,
        all_key_prefix: bool = None,
        bucket_name_list: List[str] = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        id: str = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        # Specifies whether to match the prefixes of all objects.
        self.all_key_prefix = all_key_prefix
        # The names of the buckets.
        self.bucket_name_list = bucket_name_list
        # The maximum number of objects that can be extracted from a package. Valid values: 1 to 1000. If the value is reached, the decompression operation immediately finishes. The detection of extracted objects is not affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression levels when multi-level packages are decompressed. Valid values: 1 to 5. If the value is reached, the decompression operation immediately finishes. The detection of extracted objects is not affected.
        self.decompress_max_layer = decompress_max_layer
        # The decryption methods.
        self.decryption_list = decryption_list
        # Specifies whether to enable the bucket check policy. Valid values:
        # 
        # *   **1**: enables the bucket check policy.
        # *   **0**: disables the bucket check policy.
        self.enable = enable
        # The end time of the check. Specify the time in the HH:mm:ss format.
        self.end_time = end_time
        # The policy ID.
        self.id = id
        # The prefixes of the objects.
        self.key_prefix_list = key_prefix_list
        # The suffixes of the objects that you want to check.
        self.key_suffix_list = key_suffix_list
        # The timestamp. The objects whose last modification time is later than the specified value are detected. Unit: milliseconds.
        self.last_modified_start_time = last_modified_start_time
        # The policy name.
        self.name = name
        # Whether to enable real-time incremental detection. When this parameter is set to true, the parameters ScanDayList, StartTime, and EndTime are not effective.
        self.real_time_incr = real_time_incr
        # The time when the check is performed. The value specifies the days of the week.
        self.scan_day_list = scan_day_list
        # The start time of the check. Specify the time in the HH:mm:ss format.
        self.start_time = start_time

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

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list

        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list

        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time

        if self.name is not None:
            result['Name'] = self.name

        if self.real_time_incr is not None:
            result['RealTimeIncr'] = self.real_time_incr

        if self.scan_day_list is not None:
            result['ScanDayList'] = self.scan_day_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')

        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')

        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RealTimeIncr') is not None:
            self.real_time_incr = m.get('RealTimeIncr')

        if m.get('ScanDayList') is not None:
            self.scan_day_list = m.get('ScanDayList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

