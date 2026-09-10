# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckReportResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckReportResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
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
                temp_model = main_models.ListDataCheckReportResponseBodyData()
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

class ListDataCheckReportResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        check_colum_count: int = None,
        check_result: int = None,
        compare_row_count: int = None,
        completion_rate: str = None,
        diff_rate: str = None,
        dst_compare_column: str = None,
        dst_hint: str = None,
        dst_metric_name: str = None,
        dst_sql_list: List[str] = None,
        error_msg: str = None,
        exec_time: str = None,
        exp_diff_count: str = None,
        finish_time: str = None,
        is_skipped: int = None,
        job_id: str = None,
        job_status: int = None,
        metric_colum_count: int = None,
        metric_pass_colum_count: int = None,
        only_dst_count: int = None,
        only_src_count: int = None,
        pass_colum_count: int = None,
        real_diff_count: int = None,
        real_same_count: int = None,
        result_id: str = None,
        source_column: str = None,
        source_count: str = None,
        source_data_source: str = None,
        source_error: str = None,
        source_group_clause: str = None,
        source_partition: str = None,
        source_table: str = None,
        source_type: str = None,
        source_where_clause: str = None,
        src_compare_column: str = None,
        src_hint: str = None,
        src_metric_name: str = None,
        src_sql_list: List[str] = None,
        target_column: str = None,
        target_count: str = None,
        target_data_source: str = None,
        target_error: str = None,
        target_group_clause: str = None,
        target_partition: str = None,
        target_table: str = None,
        target_type: str = None,
        target_where_clause: str = None,
        task_config_id: int = None,
        template_name: str = None,
        threshold: float = None,
        total_count_threshold: str = None,
    ):
        self.batch_id = batch_id
        self.check_colum_count = check_colum_count
        self.check_result = check_result
        self.compare_row_count = compare_row_count
        self.completion_rate = completion_rate
        self.diff_rate = diff_rate
        self.dst_compare_column = dst_compare_column
        self.dst_hint = dst_hint
        self.dst_metric_name = dst_metric_name
        self.dst_sql_list = dst_sql_list
        self.error_msg = error_msg
        self.exec_time = exec_time
        self.exp_diff_count = exp_diff_count
        self.finish_time = finish_time
        self.is_skipped = is_skipped
        self.job_id = job_id
        self.job_status = job_status
        self.metric_colum_count = metric_colum_count
        self.metric_pass_colum_count = metric_pass_colum_count
        self.only_dst_count = only_dst_count
        self.only_src_count = only_src_count
        self.pass_colum_count = pass_colum_count
        self.real_diff_count = real_diff_count
        self.real_same_count = real_same_count
        self.result_id = result_id
        self.source_column = source_column
        self.source_count = source_count
        self.source_data_source = source_data_source
        self.source_error = source_error
        self.source_group_clause = source_group_clause
        self.source_partition = source_partition
        self.source_table = source_table
        self.source_type = source_type
        self.source_where_clause = source_where_clause
        self.src_compare_column = src_compare_column
        self.src_hint = src_hint
        self.src_metric_name = src_metric_name
        self.src_sql_list = src_sql_list
        self.target_column = target_column
        self.target_count = target_count
        self.target_data_source = target_data_source
        self.target_error = target_error
        self.target_group_clause = target_group_clause
        self.target_partition = target_partition
        self.target_table = target_table
        self.target_type = target_type
        self.target_where_clause = target_where_clause
        self.task_config_id = task_config_id
        self.template_name = template_name
        self.threshold = threshold
        self.total_count_threshold = total_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.check_colum_count is not None:
            result['checkColumCount'] = self.check_colum_count

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.compare_row_count is not None:
            result['compareRowCount'] = self.compare_row_count

        if self.completion_rate is not None:
            result['completionRate'] = self.completion_rate

        if self.diff_rate is not None:
            result['diffRate'] = self.diff_rate

        if self.dst_compare_column is not None:
            result['dstCompareColumn'] = self.dst_compare_column

        if self.dst_hint is not None:
            result['dstHint'] = self.dst_hint

        if self.dst_metric_name is not None:
            result['dstMetricName'] = self.dst_metric_name

        if self.dst_sql_list is not None:
            result['dstSqlList'] = self.dst_sql_list

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.exec_time is not None:
            result['execTime'] = self.exec_time

        if self.exp_diff_count is not None:
            result['expDiffCount'] = self.exp_diff_count

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.is_skipped is not None:
            result['isSkipped'] = self.is_skipped

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.metric_colum_count is not None:
            result['metricColumCount'] = self.metric_colum_count

        if self.metric_pass_colum_count is not None:
            result['metricPassColumCount'] = self.metric_pass_colum_count

        if self.only_dst_count is not None:
            result['onlyDstCount'] = self.only_dst_count

        if self.only_src_count is not None:
            result['onlySrcCount'] = self.only_src_count

        if self.pass_colum_count is not None:
            result['passColumCount'] = self.pass_colum_count

        if self.real_diff_count is not None:
            result['realDiffCount'] = self.real_diff_count

        if self.real_same_count is not None:
            result['realSameCount'] = self.real_same_count

        if self.result_id is not None:
            result['resultId'] = self.result_id

        if self.source_column is not None:
            result['sourceColumn'] = self.source_column

        if self.source_count is not None:
            result['sourceCount'] = self.source_count

        if self.source_data_source is not None:
            result['sourceDataSource'] = self.source_data_source

        if self.source_error is not None:
            result['sourceError'] = self.source_error

        if self.source_group_clause is not None:
            result['sourceGroupClause'] = self.source_group_clause

        if self.source_partition is not None:
            result['sourcePartition'] = self.source_partition

        if self.source_table is not None:
            result['sourceTable'] = self.source_table

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.source_where_clause is not None:
            result['sourceWhereClause'] = self.source_where_clause

        if self.src_compare_column is not None:
            result['srcCompareColumn'] = self.src_compare_column

        if self.src_hint is not None:
            result['srcHint'] = self.src_hint

        if self.src_metric_name is not None:
            result['srcMetricName'] = self.src_metric_name

        if self.src_sql_list is not None:
            result['srcSqlList'] = self.src_sql_list

        if self.target_column is not None:
            result['targetColumn'] = self.target_column

        if self.target_count is not None:
            result['targetCount'] = self.target_count

        if self.target_data_source is not None:
            result['targetDataSource'] = self.target_data_source

        if self.target_error is not None:
            result['targetError'] = self.target_error

        if self.target_group_clause is not None:
            result['targetGroupClause'] = self.target_group_clause

        if self.target_partition is not None:
            result['targetPartition'] = self.target_partition

        if self.target_table is not None:
            result['targetTable'] = self.target_table

        if self.target_type is not None:
            result['targetType'] = self.target_type

        if self.target_where_clause is not None:
            result['targetWhereClause'] = self.target_where_clause

        if self.task_config_id is not None:
            result['taskConfigId'] = self.task_config_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('checkColumCount') is not None:
            self.check_colum_count = m.get('checkColumCount')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('compareRowCount') is not None:
            self.compare_row_count = m.get('compareRowCount')

        if m.get('completionRate') is not None:
            self.completion_rate = m.get('completionRate')

        if m.get('diffRate') is not None:
            self.diff_rate = m.get('diffRate')

        if m.get('dstCompareColumn') is not None:
            self.dst_compare_column = m.get('dstCompareColumn')

        if m.get('dstHint') is not None:
            self.dst_hint = m.get('dstHint')

        if m.get('dstMetricName') is not None:
            self.dst_metric_name = m.get('dstMetricName')

        if m.get('dstSqlList') is not None:
            self.dst_sql_list = m.get('dstSqlList')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('execTime') is not None:
            self.exec_time = m.get('execTime')

        if m.get('expDiffCount') is not None:
            self.exp_diff_count = m.get('expDiffCount')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('isSkipped') is not None:
            self.is_skipped = m.get('isSkipped')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('metricColumCount') is not None:
            self.metric_colum_count = m.get('metricColumCount')

        if m.get('metricPassColumCount') is not None:
            self.metric_pass_colum_count = m.get('metricPassColumCount')

        if m.get('onlyDstCount') is not None:
            self.only_dst_count = m.get('onlyDstCount')

        if m.get('onlySrcCount') is not None:
            self.only_src_count = m.get('onlySrcCount')

        if m.get('passColumCount') is not None:
            self.pass_colum_count = m.get('passColumCount')

        if m.get('realDiffCount') is not None:
            self.real_diff_count = m.get('realDiffCount')

        if m.get('realSameCount') is not None:
            self.real_same_count = m.get('realSameCount')

        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        if m.get('sourceColumn') is not None:
            self.source_column = m.get('sourceColumn')

        if m.get('sourceCount') is not None:
            self.source_count = m.get('sourceCount')

        if m.get('sourceDataSource') is not None:
            self.source_data_source = m.get('sourceDataSource')

        if m.get('sourceError') is not None:
            self.source_error = m.get('sourceError')

        if m.get('sourceGroupClause') is not None:
            self.source_group_clause = m.get('sourceGroupClause')

        if m.get('sourcePartition') is not None:
            self.source_partition = m.get('sourcePartition')

        if m.get('sourceTable') is not None:
            self.source_table = m.get('sourceTable')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('sourceWhereClause') is not None:
            self.source_where_clause = m.get('sourceWhereClause')

        if m.get('srcCompareColumn') is not None:
            self.src_compare_column = m.get('srcCompareColumn')

        if m.get('srcHint') is not None:
            self.src_hint = m.get('srcHint')

        if m.get('srcMetricName') is not None:
            self.src_metric_name = m.get('srcMetricName')

        if m.get('srcSqlList') is not None:
            self.src_sql_list = m.get('srcSqlList')

        if m.get('targetColumn') is not None:
            self.target_column = m.get('targetColumn')

        if m.get('targetCount') is not None:
            self.target_count = m.get('targetCount')

        if m.get('targetDataSource') is not None:
            self.target_data_source = m.get('targetDataSource')

        if m.get('targetError') is not None:
            self.target_error = m.get('targetError')

        if m.get('targetGroupClause') is not None:
            self.target_group_clause = m.get('targetGroupClause')

        if m.get('targetPartition') is not None:
            self.target_partition = m.get('targetPartition')

        if m.get('targetTable') is not None:
            self.target_table = m.get('targetTable')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        if m.get('targetWhereClause') is not None:
            self.target_where_clause = m.get('targetWhereClause')

        if m.get('taskConfigId') is not None:
            self.task_config_id = m.get('taskConfigId')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        return self

