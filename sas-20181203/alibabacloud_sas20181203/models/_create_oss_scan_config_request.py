# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOssScanConfigRequest(DaraModel):
    def __init__(
        self,
        all_key_prefix: bool = None,
        auto_add: int = None,
        bucket_name_list: List[str] = None,
        client_token: str = None,
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
        source: str = None,
        start_time: str = None,
    ):
        # Specifies whether to match all prefixes. If this parameter is set to true, the KeyPrefixList parameter does not take effect.
        self.all_key_prefix = all_key_prefix
        # Specifies whether OSS buckets are automatically added to this policy. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.auto_add = auto_add
        # The list of bucket names.
        self.bucket_name_list = bucket_name_list
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The maximum number of files to decompress. Minimum value: 1. Maximum value: 1000. When the maximum number of decompressed files is exceeded, the decompression operation stops. The detection of files that have already been decompressed is not affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression layers when multiple levels of nested compressed files exist. Minimum value: 1. Maximum value: 5. When the maximum number of decompression layers is exceeded, the decompression operation stops. The detection of files that have already been decompressed is not affected.
        self.decompress_max_layer = decompress_max_layer
        # The list of decryption types.
        self.decryption_list = decryption_list
        # Specifies whether to enable the policy. Valid values:
        # - **1**: Enabled.
        # - **0**: Disabled.
        self.enable = enable
        # The scan stop time, in the HH:mm:ss format.
        self.end_time = end_time
        # The file prefix list.
        self.key_prefix_list = key_prefix_list
        # The list of file suffixes to scan.
        self.key_suffix_list = key_suffix_list
        # Specifies that only files whose last modification time is after the specified timestamp are scanned. Unit: milliseconds.
        self.last_modified_start_time = last_modified_start_time
        # The policy name.
        self.name = name
        # Specifies whether to enable real-time incremental detection. If this parameter is set to true, the ScanDayList, StartTime, and EndTime parameters do not take effect.
        self.real_time_incr = real_time_incr
        # The scan schedule. The number represents the day of the week.
        self.scan_day_list = scan_day_list
        # The business source. Valid values:
        # - **OSS**: OSS.
        # - **NAS**: NAS.
        self.source = source
        # The scan start time, in the HH:mm:ss format.
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

        if self.auto_add is not None:
            result['AutoAdd'] = self.auto_add

        if self.bucket_name_list is not None:
            result['BucketNameList'] = self.bucket_name_list

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')

        if m.get('AutoAdd') is not None:
            self.auto_add = m.get('AutoAdd')

        if m.get('BucketNameList') is not None:
            self.bucket_name_list = m.get('BucketNameList')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

