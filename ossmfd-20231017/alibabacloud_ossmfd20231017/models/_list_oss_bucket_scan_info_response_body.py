# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ossmfd20231017 import models as main_models
from darabonba.model import DaraModel

class ListOssBucketScanInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOssBucketScanInfoResponseBodyData] = None,
        page_info: main_models.ListOssBucketScanInfoResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
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
        self.current_page = current_page
        self.page_size = page_size
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
        self.bucket_name = bucket_name
        self.config_status = config_status
        self.decompress_status = decompress_status
        self.high_risk = high_risk
        self.last_scan_end_time = last_scan_end_time
        self.last_scan_time = last_scan_time
        self.low_risk = low_risk
        self.medium_risk = medium_risk
        self.message = message
        self.region_id = region_id
        self.scan_object = scan_object
        self.scanned = scanned
        self.status = status
        self.storage_class = storage_class
        self.support = support
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

