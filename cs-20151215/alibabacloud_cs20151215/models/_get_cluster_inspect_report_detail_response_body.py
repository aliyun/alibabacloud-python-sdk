# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GetClusterInspectReportDetailResponseBody(DaraModel):
    def __init__(
        self,
        check_item_results: List[main_models.GetClusterInspectReportDetailResponseBodyCheckItemResults] = None,
        end_time: str = None,
        next_token: str = None,
        report_id: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        summary: main_models.GetClusterInspectReportDetailResponseBodySummary = None,
    ):
        # The results.
        self.check_item_results = check_item_results
        # The completion time of the inspection report.
        self.end_time = end_time
        # The token that is used to display the returned tags on multiple pages.
        self.next_token = next_token
        # The ID of the inspection report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The start time of the inspection report.
        self.start_time = start_time
        # The status of the inspection report. Valid values:
        # 
        # *   completed: The inspection report is generated.
        # *   running: The inspection report is generating.
        self.status = status
        # Overview of inspection reports.
        self.summary = summary

    def validate(self):
        if self.check_item_results:
            for v1 in self.check_item_results:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['checkItemResults'] = []
        if self.check_item_results is not None:
            for k1 in self.check_item_results:
                result['checkItemResults'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item_results = []
        if m.get('checkItemResults') is not None:
            for k1 in m.get('checkItemResults'):
                temp_model = main_models.GetClusterInspectReportDetailResponseBodyCheckItemResults()
                self.check_item_results.append(temp_model.from_map(k1))

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            temp_model = main_models.GetClusterInspectReportDetailResponseBodySummary()
            self.summary = temp_model.from_map(m.get('summary'))

        return self

class GetClusterInspectReportDetailResponseBodySummary(DaraModel):
    def __init__(
        self,
        advice_count: int = None,
        code: str = None,
        error_count: int = None,
        normal_count: int = None,
        warn_count: int = None,
    ):
        # The number of check items whose inspection result is advice.
        self.advice_count = advice_count
        # Check the status code of the inspection task.
        self.code = code
        # The number of check items whose inspection result is error.
        self.error_count = error_count
        # The number of check items whose inspection result is normal.
        self.normal_count = normal_count
        # The number of check items whose inspection result is warning.
        self.warn_count = warn_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_count is not None:
            result['adviceCount'] = self.advice_count

        if self.code is not None:
            result['code'] = self.code

        if self.error_count is not None:
            result['errorCount'] = self.error_count

        if self.normal_count is not None:
            result['normalCount'] = self.normal_count

        if self.warn_count is not None:
            result['warnCount'] = self.warn_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adviceCount') is not None:
            self.advice_count = m.get('adviceCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')

        if m.get('normalCount') is not None:
            self.normal_count = m.get('normalCount')

        if m.get('warnCount') is not None:
            self.warn_count = m.get('warnCount')

        return self

class GetClusterInspectReportDetailResponseBodyCheckItemResults(DaraModel):
    def __init__(
        self,
        category: str = None,
        check_item_uid: str = None,
        description: str = None,
        fix: str = None,
        level: str = None,
        name: str = None,
        result: str = None,
        target_type: str = None,
        targets: List[str] = None,
    ):
        # The category of the inspection item. Valid values:
        # 
        # *   security: Security compliance
        # *   performance: Performance efficiency
        # *   stability: Business stability
        # *   limitation: Service limits
        # *   cost: Cost optimization
        self.category = category
        # The unique identifier of the inspection item.
        self.check_item_uid = check_item_uid
        # The description of the inspection item.
        self.description = description
        # The fixing suggestion.
        self.fix = fix
        # The level of the inspection item. Valid values:
        # 
        # *   advice: Suggestions
        # *   warning: Low severity
        # *   error: Medium severity
        # *   critical: High severity
        self.level = level
        # The name of the inspection item.
        self.name = name
        # The inspection results. Valid values:
        # 
        # *   true: The inspection item is abnormal.
        # *   false: The inspection item is normal.
        # *   disable: The inspection item is not enabled.
        self.result = result
        # The resource type of the inspection object.
        self.target_type = target_type
        # The inspection objects.
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.check_item_uid is not None:
            result['checkItemUid'] = self.check_item_uid

        if self.description is not None:
            result['description'] = self.description

        if self.fix is not None:
            result['fix'] = self.fix

        if self.level is not None:
            result['level'] = self.level

        if self.name is not None:
            result['name'] = self.name

        if self.result is not None:
            result['result'] = self.result

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.targets is not None:
            result['targets'] = self.targets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('checkItemUid') is not None:
            self.check_item_uid = m.get('checkItemUid')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fix') is not None:
            self.fix = m.get('fix')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('targets') is not None:
            self.targets = m.get('targets')

        return self

