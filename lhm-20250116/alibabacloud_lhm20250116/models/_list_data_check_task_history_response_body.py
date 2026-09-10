# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckTaskHistoryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckTaskHistoryResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The data list returned by the operation. For the element structure, see the child field descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which is the number of records returned per page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for troubleshooting.
        self.success = success
        # The total number of records that match the query conditions. This value is used for pagination.
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
                temp_model = main_models.ListDataCheckTaskHistoryResponseBodyData()
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

class ListDataCheckTaskHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        biz: str = None,
        check_result: int = None,
        check_table_num: int = None,
        concurrency: int = None,
        creator: str = None,
        cron_exp: str = None,
        end_time: str = None,
        error_msg: str = None,
        error_table_num: int = None,
        exec_status: int = None,
        exec_time: str = None,
        extra: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        operator: str = None,
        origin_batch_id: int = None,
        pass_process: float = None,
        pass_process_export: str = None,
        progress: float = None,
        report_time: str = None,
        report_title: str = None,
        schedule_id: int = None,
        seq_id: str = None,
        skip_table_num: int = None,
        start_time: str = None,
        successful_table_num: int = None,
    ):
        # The batch ID.
        self.batch_id = batch_id
        # The business field.
        self.biz = biz
        # The execution result. Valid values: no record, passed, or not passed.
        self.check_result = check_result
        # The number of checked tables.
        self.check_table_num = check_table_num
        # The concurrency of the batch.
        self.concurrency = concurrency
        # The creator.
        self.creator = creator
        # The scheduling cycle expression.
        self.cron_exp = cron_exp
        # The end time, in the format of YYYY-MM-DD HH:MM:SS.
        self.end_time = end_time
        # The error message.
        self.error_msg = error_msg
        # The number of error tables.
        self.error_table_num = error_table_num
        # The execution status. Valid values: pending, running, stopped, failed, or completed.
        self.exec_status = exec_status
        # The execution duration, in the format of HH:MM:SS.
        self.exec_time = exec_time
        # The reserved field.
        self.extra = extra
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The updater.
        self.operator = operator
        # The original batch ID.
        self.origin_batch_id = origin_batch_id
        # The check pass rate.
        self.pass_process = pass_process
        # The pass rate (export report field), calculated by dividing the number of passed tables by the total number of checked tables. The value is returned as a string with a percent sign and two decimal places (for example, 100.00%). If no checked table data exists, the value is -.
        self.pass_process_export = pass_process_export
        # The task progress.
        self.progress = progress
        # The check report time, which is the completion time of the last job.
        self.report_time = report_time
        # The check report title.
        self.report_title = report_title
        # The scheduled task ID.
        self.schedule_id = schedule_id
        # The task number.
        self.seq_id = seq_id
        # The number of skipped tables.
        self.skip_table_num = skip_table_num
        # The start time, in the format of YYYY-MM-DD HH:MM:SS.
        self.start_time = start_time
        # The number of successful tables.
        self.successful_table_num = successful_table_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.biz is not None:
            result['biz'] = self.biz

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.check_table_num is not None:
            result['checkTableNum'] = self.check_table_num

        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.creator is not None:
            result['creator'] = self.creator

        if self.cron_exp is not None:
            result['cronExp'] = self.cron_exp

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.error_table_num is not None:
            result['errorTableNum'] = self.error_table_num

        if self.exec_status is not None:
            result['execStatus'] = self.exec_status

        if self.exec_time is not None:
            result['execTime'] = self.exec_time

        if self.extra is not None:
            result['extra'] = self.extra

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.operator is not None:
            result['operator'] = self.operator

        if self.origin_batch_id is not None:
            result['originBatchId'] = self.origin_batch_id

        if self.pass_process is not None:
            result['passProcess'] = self.pass_process

        if self.pass_process_export is not None:
            result['passProcessExport'] = self.pass_process_export

        if self.progress is not None:
            result['progress'] = self.progress

        if self.report_time is not None:
            result['reportTime'] = self.report_time

        if self.report_title is not None:
            result['reportTitle'] = self.report_title

        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id

        if self.seq_id is not None:
            result['seqId'] = self.seq_id

        if self.skip_table_num is not None:
            result['skipTableNum'] = self.skip_table_num

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.successful_table_num is not None:
            result['successfulTableNum'] = self.successful_table_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('biz') is not None:
            self.biz = m.get('biz')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('checkTableNum') is not None:
            self.check_table_num = m.get('checkTableNum')

        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('cronExp') is not None:
            self.cron_exp = m.get('cronExp')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('errorTableNum') is not None:
            self.error_table_num = m.get('errorTableNum')

        if m.get('execStatus') is not None:
            self.exec_status = m.get('execStatus')

        if m.get('execTime') is not None:
            self.exec_time = m.get('execTime')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('originBatchId') is not None:
            self.origin_batch_id = m.get('originBatchId')

        if m.get('passProcess') is not None:
            self.pass_process = m.get('passProcess')

        if m.get('passProcessExport') is not None:
            self.pass_process_export = m.get('passProcessExport')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('reportTime') is not None:
            self.report_time = m.get('reportTime')

        if m.get('reportTitle') is not None:
            self.report_title = m.get('reportTitle')

        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')

        if m.get('seqId') is not None:
            self.seq_id = m.get('seqId')

        if m.get('skipTableNum') is not None:
            self.skip_table_num = m.get('skipTableNum')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('successfulTableNum') is not None:
            self.successful_table_num = m.get('successfulTableNum')

        return self

