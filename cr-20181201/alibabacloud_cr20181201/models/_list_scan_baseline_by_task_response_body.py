# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListScanBaselineByTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        scan_baselines: List[main_models.ListScanBaselineByTaskResponseBodyScanBaselines] = None,
        total_count: int = None,
    ):
        # The return code.
        self.code = code
        # Indicates whether the API call is successful. Valid values:
        # 
        # - `true`: The API call is successful.
        # - `false`: The API call failed.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The baseline list.
        self.scan_baselines = scan_baselines
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.scan_baselines:
            for v1 in self.scan_baselines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScanBaselines'] = []
        if self.scan_baselines is not None:
            for k1 in self.scan_baselines:
                result['ScanBaselines'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scan_baselines = []
        if m.get('ScanBaselines') is not None:
            for k1 in m.get('ScanBaselines'):
                temp_model = main_models.ListScanBaselineByTaskResponseBodyScanBaselines()
                self.scan_baselines.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScanBaselineByTaskResponseBodyScanBaselines(DaraModel):
    def __init__(
        self,
        baseline_class_alias: str = None,
        baseline_detail_advice: str = None,
        baseline_detail_description: str = None,
        baseline_detail_prompt: str = None,
        baseline_item_count: int = None,
        baseline_name_alias: str = None,
        baseline_name_key: str = None,
        baseline_name_level: str = None,
        create_time: int = None,
        first_scan_time: int = None,
        high_risk_item_count: int = None,
        low_risk_item_count: int = None,
        middle_risk_item_count: int = None,
        scan_task_id: str = None,
        update_time: int = None,
    ):
        # The baseline check category.
        self.baseline_class_alias = baseline_class_alias
        # The baseline check remediation suggestion.
        self.baseline_detail_advice = baseline_detail_advice
        # The baseline description.
        self.baseline_detail_description = baseline_detail_description
        # The baseline check path and content.
        self.baseline_detail_prompt = baseline_detail_prompt
        # The number of baseline check items.
        self.baseline_item_count = baseline_item_count
        # The baseline check name.
        self.baseline_name_alias = baseline_name_alias
        # The baseline name key.
        self.baseline_name_key = baseline_name_key
        # The baseline check risk level.
        self.baseline_name_level = baseline_name_level
        # The creation time, in UNIX timestamp format. Unit: milliseconds.
        self.create_time = create_time
        # The time of the first scan.
        self.first_scan_time = first_scan_time
        # The number of high-risk items.
        self.high_risk_item_count = high_risk_item_count
        # The number of low-risk items.
        self.low_risk_item_count = low_risk_item_count
        # The number of medium-risk items.
        self.middle_risk_item_count = middle_risk_item_count
        # The image scan task ID.
        self.scan_task_id = scan_task_id
        # The update time, in UNIX timestamp format. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_class_alias is not None:
            result['BaselineClassAlias'] = self.baseline_class_alias

        if self.baseline_detail_advice is not None:
            result['BaselineDetailAdvice'] = self.baseline_detail_advice

        if self.baseline_detail_description is not None:
            result['BaselineDetailDescription'] = self.baseline_detail_description

        if self.baseline_detail_prompt is not None:
            result['BaselineDetailPrompt'] = self.baseline_detail_prompt

        if self.baseline_item_count is not None:
            result['BaselineItemCount'] = self.baseline_item_count

        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias

        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.baseline_name_level is not None:
            result['BaselineNameLevel'] = self.baseline_name_level

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.high_risk_item_count is not None:
            result['HighRiskItemCount'] = self.high_risk_item_count

        if self.low_risk_item_count is not None:
            result['LowRiskItemCount'] = self.low_risk_item_count

        if self.middle_risk_item_count is not None:
            result['MiddleRiskItemCount'] = self.middle_risk_item_count

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')

        if m.get('BaselineDetailAdvice') is not None:
            self.baseline_detail_advice = m.get('BaselineDetailAdvice')

        if m.get('BaselineDetailDescription') is not None:
            self.baseline_detail_description = m.get('BaselineDetailDescription')

        if m.get('BaselineDetailPrompt') is not None:
            self.baseline_detail_prompt = m.get('BaselineDetailPrompt')

        if m.get('BaselineItemCount') is not None:
            self.baseline_item_count = m.get('BaselineItemCount')

        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')

        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('BaselineNameLevel') is not None:
            self.baseline_name_level = m.get('BaselineNameLevel')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('HighRiskItemCount') is not None:
            self.high_risk_item_count = m.get('HighRiskItemCount')

        if m.get('LowRiskItemCount') is not None:
            self.low_risk_item_count = m.get('LowRiskItemCount')

        if m.get('MiddleRiskItemCount') is not None:
            self.middle_risk_item_count = m.get('MiddleRiskItemCount')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

