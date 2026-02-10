# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBaselineCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        baseline_result: List[main_models.DescribeImageBaselineCheckResultResponseBodyBaselineResult] = None,
        page_info: main_models.DescribeImageBaselineCheckResultResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the check results of image baselines.
        self.baseline_result = baseline_result
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.baseline_result:
            for v1 in self.baseline_result:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineResult'] = []
        if self.baseline_result is not None:
            for k1 in self.baseline_result:
                result['BaselineResult'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_result = []
        if m.get('BaselineResult') is not None:
            for k1 in m.get('BaselineResult'):
                temp_model = main_models.DescribeImageBaselineCheckResultResponseBodyBaselineResult()
                self.baseline_result.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageBaselineCheckResultResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageBaselineCheckResultResponseBodyPageInfo(DaraModel):
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
        # The number of entries returned per page.
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

class DescribeImageBaselineCheckResultResponseBodyBaselineResult(DaraModel):
    def __init__(
        self,
        baseline_class_alias: str = None,
        baseline_item_count: int = None,
        baseline_name_alias: str = None,
        baseline_name_key: str = None,
        baseline_name_level: str = None,
        first_scan_time: int = None,
        high_risk_item_count: int = None,
        last_scan_time: int = None,
        low_risk_item_count: int = None,
        middle_risk_item_count: int = None,
        status: int = None,
    ):
        # The key of the image baseline type.
        self.baseline_class_alias = baseline_class_alias
        # The number of baseline check items.
        self.baseline_item_count = baseline_item_count
        # The alias of the image baseline.
        self.baseline_name_alias = baseline_name_alias
        # The key of the image baseline.
        self.baseline_name_key = baseline_name_key
        # The severity of the image baseline. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.baseline_name_level = baseline_name_level
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The number of high-risk images that are affected.
        self.high_risk_item_count = high_risk_item_count
        # The timestamp generated when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The number of low-risk images that are affected.
        self.low_risk_item_count = low_risk_item_count
        # The number of medium-risk images that are affected.
        self.middle_risk_item_count = middle_risk_item_count
        # The status of the baseline risks. Valid values:
        # 
        # *   **0**: unfixed
        # *   **1**: fixed
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

        if self.baseline_item_count is not None:
            result['BaselineItemCount'] = self.baseline_item_count

        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias

        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.baseline_name_level is not None:
            result['BaselineNameLevel'] = self.baseline_name_level

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.high_risk_item_count is not None:
            result['HighRiskItemCount'] = self.high_risk_item_count

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.low_risk_item_count is not None:
            result['LowRiskItemCount'] = self.low_risk_item_count

        if self.middle_risk_item_count is not None:
            result['MiddleRiskItemCount'] = self.middle_risk_item_count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')

        if m.get('BaselineItemCount') is not None:
            self.baseline_item_count = m.get('BaselineItemCount')

        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')

        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('BaselineNameLevel') is not None:
            self.baseline_name_level = m.get('BaselineNameLevel')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('HighRiskItemCount') is not None:
            self.high_risk_item_count = m.get('HighRiskItemCount')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LowRiskItemCount') is not None:
            self.low_risk_item_count = m.get('LowRiskItemCount')

        if m.get('MiddleRiskItemCount') is not None:
            self.middle_risk_item_count = m.get('MiddleRiskItemCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

