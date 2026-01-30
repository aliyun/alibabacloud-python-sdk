# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOssScanConfigRequest(DaraModel):
    def __init__(
        self,
        all_key_prefix: str = None,
        bucket_name: str = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        self.all_key_prefix = all_key_prefix
        # This parameter is required.
        self.bucket_name = bucket_name
        self.decompress_max_file_count = decompress_max_file_count
        self.decompress_max_layer = decompress_max_layer
        self.decryption_list = decryption_list
        # This parameter is required.
        self.enable = enable
        self.end_time = end_time
        self.key_prefix_list = key_prefix_list
        self.key_suffix_list = key_suffix_list
        self.last_modified_start_time = last_modified_start_time
        self.name = name
        self.real_time_incr = real_time_incr
        self.scan_day_list = scan_day_list
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

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

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

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

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

