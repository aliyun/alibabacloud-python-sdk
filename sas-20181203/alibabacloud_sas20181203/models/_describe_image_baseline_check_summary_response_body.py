# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBaselineCheckSummaryResponseBody(DaraModel):
    def __init__(
        self,
        baseline_result_summary: List[main_models.DescribeImageBaselineCheckSummaryResponseBodyBaselineResultSummary] = None,
        page_info: main_models.DescribeImageBaselineCheckSummaryResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the check results of image baselines.
        self.baseline_result_summary = baseline_result_summary
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.baseline_result_summary:
            for v1 in self.baseline_result_summary:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineResultSummary'] = []
        if self.baseline_result_summary is not None:
            for k1 in self.baseline_result_summary:
                result['BaselineResultSummary'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_result_summary = []
        if m.get('BaselineResultSummary') is not None:
            for k1 in m.get('BaselineResultSummary'):
                temp_model = main_models.DescribeImageBaselineCheckSummaryResponseBodyBaselineResultSummary()
                self.baseline_result_summary.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageBaselineCheckSummaryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageBaselineCheckSummaryResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageBaselineCheckSummaryResponseBodyBaselineResultSummary(DaraModel):
    def __init__(
        self,
        baseline_class_alias: str = None,
        baseline_class_key: str = None,
        baseline_name_alias: str = None,
        baseline_name_key: str = None,
        baseline_name_level: str = None,
        first_scan_time: int = None,
        high_risk_image: int = None,
        last_scan_time: int = None,
        low_risk_image: int = None,
        middle_risk_image: int = None,
        status: int = None,
    ):
        # The category of the baseline.
        self.baseline_class_alias = baseline_class_alias
        # The keyword of the baseline category.
        self.baseline_class_key = baseline_class_key
        # The name of the baseline.
        self.baseline_name_alias = baseline_name_alias
        # The keyword of the baseline name.
        self.baseline_name_key = baseline_name_key
        # The severity of the image baseline. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.baseline_name_level = baseline_name_level
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The number of images on which **high** baseline risks are detected.
        self.high_risk_image = high_risk_image
        # The timestamp generated when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The number of images on which **low** baseline risks are detected.
        self.low_risk_image = low_risk_image
        # The number of images on which **medium** baseline risks are detected.
        self.middle_risk_image = middle_risk_image
        # The status of the baseline risks. Valid values:
        # 
        # *   **0**: unfixed
        # *   **1**: fixed
        # *   **2**: pending verification
        # *   **3**: fixing failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_class_alias is not None:
            result['BaselineClassAlias'] = self.baseline_class_alias

        if self.baseline_class_key is not None:
            result['BaselineClassKey'] = self.baseline_class_key

        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias

        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.baseline_name_level is not None:
            result['BaselineNameLevel'] = self.baseline_name_level

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.high_risk_image is not None:
            result['HighRiskImage'] = self.high_risk_image

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.low_risk_image is not None:
            result['LowRiskImage'] = self.low_risk_image

        if self.middle_risk_image is not None:
            result['MiddleRiskImage'] = self.middle_risk_image

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')

        if m.get('BaselineClassKey') is not None:
            self.baseline_class_key = m.get('BaselineClassKey')

        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')

        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('BaselineNameLevel') is not None:
            self.baseline_name_level = m.get('BaselineNameLevel')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('HighRiskImage') is not None:
            self.high_risk_image = m.get('HighRiskImage')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LowRiskImage') is not None:
            self.low_risk_image = m.get('LowRiskImage')

        if m.get('MiddleRiskImage') is not None:
            self.middle_risk_image = m.get('MiddleRiskImage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

