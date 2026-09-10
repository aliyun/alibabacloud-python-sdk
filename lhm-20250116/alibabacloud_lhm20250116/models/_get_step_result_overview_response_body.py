# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetStepResultOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetStepResultOverviewResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response data.
        self.data = data
        # The fault message code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed. Check errCode and errMessage for troubleshooting.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetStepResultOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetStepResultOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        check_column_count: int = None,
        dst_metric_name: str = None,
        is_consistent: int = None,
        metric_column_count: int = None,
        metric_pass_column_count: int = None,
        pass_column_count: int = None,
        result_id: str = None,
        source_pt_name: str = None,
        source_table: str = None,
        src_metric_name: str = None,
        status: int = None,
        target_pt_name: str = None,
        target_table: str = None,
    ):
        # The number of validated fields.
        self.check_column_count = check_column_count
        # The metric name of the target.
        self.dst_metric_name = dst_metric_name
        # Indicates whether the source and target are consistent. Valid values:
        # - 0: Inconsistent.
        # - 1: Consistent.
        self.is_consistent = is_consistent
        # The number of validated metrics.
        self.metric_column_count = metric_column_count
        # The number of metrics that passed validation.
        self.metric_pass_column_count = metric_pass_column_count
        # The number of fields that passed validation.
        self.pass_column_count = pass_column_count
        # The unique ID of the validation result.
        self.result_id = result_id
        # The partition name of the source.
        self.source_pt_name = source_pt_name
        # The table name of the source.
        self.source_table = source_table
        # The metric name of the source.
        self.src_metric_name = src_metric_name
        # The task status. Valid values:
        # - 0: Created.
        # - 1: Running.
        # - 2: Completed.
        # - 3: Stopped.
        # - 4: Canceled.
        self.status = status
        # The partition name of the target.
        self.target_pt_name = target_pt_name
        # The table name of the target.
        self.target_table = target_table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_column_count is not None:
            result['checkColumnCount'] = self.check_column_count

        if self.dst_metric_name is not None:
            result['dstMetricName'] = self.dst_metric_name

        if self.is_consistent is not None:
            result['isConsistent'] = self.is_consistent

        if self.metric_column_count is not None:
            result['metricColumnCount'] = self.metric_column_count

        if self.metric_pass_column_count is not None:
            result['metricPassColumnCount'] = self.metric_pass_column_count

        if self.pass_column_count is not None:
            result['passColumnCount'] = self.pass_column_count

        if self.result_id is not None:
            result['resultId'] = self.result_id

        if self.source_pt_name is not None:
            result['sourcePtName'] = self.source_pt_name

        if self.source_table is not None:
            result['sourceTable'] = self.source_table

        if self.src_metric_name is not None:
            result['srcMetricName'] = self.src_metric_name

        if self.status is not None:
            result['status'] = self.status

        if self.target_pt_name is not None:
            result['targetPtName'] = self.target_pt_name

        if self.target_table is not None:
            result['targetTable'] = self.target_table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkColumnCount') is not None:
            self.check_column_count = m.get('checkColumnCount')

        if m.get('dstMetricName') is not None:
            self.dst_metric_name = m.get('dstMetricName')

        if m.get('isConsistent') is not None:
            self.is_consistent = m.get('isConsistent')

        if m.get('metricColumnCount') is not None:
            self.metric_column_count = m.get('metricColumnCount')

        if m.get('metricPassColumnCount') is not None:
            self.metric_pass_column_count = m.get('metricPassColumnCount')

        if m.get('passColumnCount') is not None:
            self.pass_column_count = m.get('passColumnCount')

        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        if m.get('sourcePtName') is not None:
            self.source_pt_name = m.get('sourcePtName')

        if m.get('sourceTable') is not None:
            self.source_table = m.get('sourceTable')

        if m.get('srcMetricName') is not None:
            self.src_metric_name = m.get('srcMetricName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('targetPtName') is not None:
            self.target_pt_name = m.get('targetPtName')

        if m.get('targetTable') is not None:
            self.target_table = m.get('targetTable')

        return self

