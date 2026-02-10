# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOssBucketScanInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOssBucketScanInfoResponseBodyData] = None,
        page_info: main_models.ListOssBucketScanInfoResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The page information.
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
                temp_model = main_models.ListOssBucketScanInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListOssBucketScanInfoResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOssBucketScanInfoResponseBodyPageInfo(DaraModel):
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

class ListOssBucketScanInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        config_status: int = None,
        decompress_status: int = None,
        high_risk: int = None,
        last_scan_end_time: int = None,
        last_scan_time: int = None,
        low_risk: int = None,
        medium_risk: int = None,
        message: str = None,
        region_id: str = None,
        scan_object: int = None,
        scanned: bool = None,
        status: int = None,
        storage_class: str = None,
        support: bool = None,
        total_object: int = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # Configuration status, valid values:
        # 
        # - **0**: No Configuration.
        # - **1**: Not Open.
        # - **2**: Open.
        self.config_status = config_status
        # Bucket decompression configuration status, valid values:
        # - **0**: Decompression not configured.
        # - **1**: Decompression configured.
        self.decompress_status = decompress_status
        # The number of high-risk objects.
        self.high_risk = high_risk
        # The time when the most recent check ended. Unit: milliseconds.
        self.last_scan_end_time = last_scan_end_time
        # The time when the bucket was last checked. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The number of low-risk objects.
        self.low_risk = low_risk
        # The number of medium-risk objects.
        self.medium_risk = medium_risk
        # The reason why the bucket cannot be checked.
        self.message = message
        # The region ID.
        self.region_id = region_id
        # The number of objects that are checked.
        self.scan_object = scan_object
        # Indicates whether the bucket is checked. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.scanned = scanned
        # The check status of the bucket. Valid values:
        # 
        # *   **1**: The bucket is not checked.
        # *   **2**: All objects in the bucket are being checked.
        # *   **3**: Only new objects are being checked.
        # *   **4**: The bucket is checked.
        self.status = status
        # The storage class of the bucket. Valid values:
        # 
        # *   **Standard**
        # *   **IA**
        # *   **Archive**
        # *   **ColdArchive**
        self.storage_class = storage_class
        # Indicates whether the bucket can be checked. Valid values:
        # 
        # *   true
        # *   false
        self.support = support
        # The total number of objects in the bucket.
        self.total_object = total_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.decompress_status is not None:
            result['DecompressStatus'] = self.decompress_status

        if self.high_risk is not None:
            result['HighRisk'] = self.high_risk

        if self.last_scan_end_time is not None:
            result['LastScanEndTime'] = self.last_scan_end_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.low_risk is not None:
            result['LowRisk'] = self.low_risk

        if self.medium_risk is not None:
            result['MediumRisk'] = self.medium_risk

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scan_object is not None:
            result['ScanObject'] = self.scan_object

        if self.scanned is not None:
            result['Scanned'] = self.scanned

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.support is not None:
            result['Support'] = self.support

        if self.total_object is not None:
            result['TotalObject'] = self.total_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('DecompressStatus') is not None:
            self.decompress_status = m.get('DecompressStatus')

        if m.get('HighRisk') is not None:
            self.high_risk = m.get('HighRisk')

        if m.get('LastScanEndTime') is not None:
            self.last_scan_end_time = m.get('LastScanEndTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LowRisk') is not None:
            self.low_risk = m.get('LowRisk')

        if m.get('MediumRisk') is not None:
            self.medium_risk = m.get('MediumRisk')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScanObject') is not None:
            self.scan_object = m.get('ScanObject')

        if m.get('Scanned') is not None:
            self.scanned = m.get('Scanned')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('Support') is not None:
            self.support = m.get('Support')

        if m.get('TotalObject') is not None:
            self.total_object = m.get('TotalObject')

        return self

