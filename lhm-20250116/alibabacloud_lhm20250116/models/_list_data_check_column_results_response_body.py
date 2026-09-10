# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckColumnResultsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckColumnResultsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The page number that indicates the requested page.
        self.page_index = page_index
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListDataCheckColumnResultsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDataCheckColumnResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        actual_threshold: str = None,
        check_result: int = None,
        check_rule: str = None,
        dst_alias: str = None,
        dst_column_name: str = None,
        dst_column_type: str = None,
        dst_metric_column: str = None,
        dst_result: str = None,
        expect_threshold: str = None,
        is_consistent: int = None,
        src_alias: str = None,
        src_column_name: str = None,
        src_column_type: str = None,
        src_metric_column: str = None,
        src_result: str = None,
        step_id: int = None,
    ):
        # The actual difference.
        self.actual_threshold = actual_threshold
        # The execution result. Valid values:
        # - 0: no record.
        # - 1: passed.
        # - 2: failed.
        self.check_result = check_result
        # The comparison rule.
        self.check_rule = check_rule
        # The alias of the destination.
        self.dst_alias = dst_alias
        # The field name of the destination.
        self.dst_column_name = dst_column_name
        # The field type of the destination.
        self.dst_column_type = dst_column_type
        # The metric key of the destination.
        self.dst_metric_column = dst_metric_column
        # The result value of the destination field.
        self.dst_result = dst_result
        # The expected threshold.
        self.expect_threshold = expect_threshold
        # The validation result. Valid values:
        # - 0: inconsistent.
        # - 1: consistent.
        # - 2: manually repaired.
        self.is_consistent = is_consistent
        # The alias of the source.
        self.src_alias = src_alias
        # The field name of the source.
        self.src_column_name = src_column_name
        # The field type of the source.
        self.src_column_type = src_column_type
        # The metric key of the source.
        self.src_metric_column = src_metric_column
        # The result value of the source field.
        self.src_result = src_result
        # The step ID.
        self.step_id = step_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_threshold is not None:
            result['actualThreshold'] = self.actual_threshold

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.check_rule is not None:
            result['checkRule'] = self.check_rule

        if self.dst_alias is not None:
            result['dstAlias'] = self.dst_alias

        if self.dst_column_name is not None:
            result['dstColumnName'] = self.dst_column_name

        if self.dst_column_type is not None:
            result['dstColumnType'] = self.dst_column_type

        if self.dst_metric_column is not None:
            result['dstMetricColumn'] = self.dst_metric_column

        if self.dst_result is not None:
            result['dstResult'] = self.dst_result

        if self.expect_threshold is not None:
            result['expectThreshold'] = self.expect_threshold

        if self.is_consistent is not None:
            result['isConsistent'] = self.is_consistent

        if self.src_alias is not None:
            result['srcAlias'] = self.src_alias

        if self.src_column_name is not None:
            result['srcColumnName'] = self.src_column_name

        if self.src_column_type is not None:
            result['srcColumnType'] = self.src_column_type

        if self.src_metric_column is not None:
            result['srcMetricColumn'] = self.src_metric_column

        if self.src_result is not None:
            result['srcResult'] = self.src_result

        if self.step_id is not None:
            result['stepId'] = self.step_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualThreshold') is not None:
            self.actual_threshold = m.get('actualThreshold')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('checkRule') is not None:
            self.check_rule = m.get('checkRule')

        if m.get('dstAlias') is not None:
            self.dst_alias = m.get('dstAlias')

        if m.get('dstColumnName') is not None:
            self.dst_column_name = m.get('dstColumnName')

        if m.get('dstColumnType') is not None:
            self.dst_column_type = m.get('dstColumnType')

        if m.get('dstMetricColumn') is not None:
            self.dst_metric_column = m.get('dstMetricColumn')

        if m.get('dstResult') is not None:
            self.dst_result = m.get('dstResult')

        if m.get('expectThreshold') is not None:
            self.expect_threshold = m.get('expectThreshold')

        if m.get('isConsistent') is not None:
            self.is_consistent = m.get('isConsistent')

        if m.get('srcAlias') is not None:
            self.src_alias = m.get('srcAlias')

        if m.get('srcColumnName') is not None:
            self.src_column_name = m.get('srcColumnName')

        if m.get('srcColumnType') is not None:
            self.src_column_type = m.get('srcColumnType')

        if m.get('srcMetricColumn') is not None:
            self.src_metric_column = m.get('srcMetricColumn')

        if m.get('srcResult') is not None:
            self.src_result = m.get('srcResult')

        if m.get('stepId') is not None:
            self.step_id = m.get('stepId')

        return self

