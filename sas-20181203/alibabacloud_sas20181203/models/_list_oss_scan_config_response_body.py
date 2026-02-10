# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOssScanConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOssScanConfigResponseBodyData] = None,
        page_info: main_models.ListOssScanConfigResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOssScanConfigResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListOssScanConfigResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOssScanConfigResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOssScanConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        all_key_prefix: bool = None,
        bucket_count: int = None,
        bucket_name_list: List[str] = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        id: int = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        last_update_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        # Indicates whether the prefixes of all objects are matched.
        self.all_key_prefix = all_key_prefix
        # The number of buckets.
        self.bucket_count = bucket_count
        # The names of the buckets.
        self.bucket_name_list = bucket_name_list
        # The maximum number of objects that can be extracted during decompression. Valid values: 1 to 1000. If the maximum number of objects that can be extracted is reached, the decompression operation immediately ends and the detection of extracted objects is not affected.
        self.decompress_max_file_count = decompress_max_file_count
        # The maximum number of decompression levels when multi-level packages are decompressed. Valid values: 1 to 5. If the maximum number of decompression levels is reached, the decompression operation immediately ends and the detection of extracted objects is not affected.
        self.decompress_max_layer = decompress_max_layer
        # The decryption methods.
        self.decryption_list = decryption_list
        # Indicates whether the policy is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable
        # The time when the scan ends. The time is in the HH:mm:ss format.
        self.end_time = end_time
        # The configuration ID.
        self.id = id
        # The prefixes of the objects that are scanned.
        self.key_prefix_list = key_prefix_list
        # The suffixes of the objects that are scanned.
        self.key_suffix_list = key_suffix_list
        # The timestamp when the object was last modified. The time must be later than the timestamp that you specify. Unit: milliseconds.
        self.last_modified_start_time = last_modified_start_time
        # The timestamp when the configuration was last modified.
        self.last_update_time = last_update_time
        # The configuration name.
        self.name = name
        # Whether to enable real-time incremental detection. When this parameter is set to true, the parameters ScanDayList, StartTime, and EndTime are not effective.
        self.real_time_incr = real_time_incr
        # The days on which the scan is executed in a week.
        self.scan_day_list = scan_day_list
        # The time when the scan starts. The time is in the HH:mm:ss format.
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

        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count

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

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

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

        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')

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

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RealTimeIncr') is not None:
            self.real_time_incr = m.get('RealTimeIncr')

        if m.get('ScanDayList') is not None:
            self.scan_day_list = m.get('ScanDayList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

