# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetDataCheckTaskListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetDataCheckTaskListResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The task list.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The page number, starting from 1.
        self.page_index = page_index
        # The page size, which indicates the number of records returned per page.
        self.page_size = page_size
        # The request ID, which is used to locate and troubleshoot issues related to this call.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success. A value of false indicates failure. If the call fails, check errCode and errMessage for details.
        self.success = success
        # The total number of records that match the query conditions. This parameter is used for pagination.
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
                temp_model = main_models.GetDataCheckTaskListResponseBodyData()
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

class GetDataCheckTaskListResponseBodyData(DaraModel):
    def __init__(
        self,
        check_result: int = None,
        check_table_num: int = None,
        check_template_id: str = None,
        check_type: int = None,
        dst_ds_id: str = None,
        dst_ds_name: str = None,
        dst_ds_type: str = None,
        dst_engine_id: str = None,
        dst_engine_name: str = None,
        dst_engine_type: str = None,
        end_time: str = None,
        error_msg: str = None,
        error_table_num: int = None,
        exec_status: int = None,
        exec_time: str = None,
        execute_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_scheduled: int = None,
        last_batch_id: int = None,
        last_finished_id: int = None,
        pass_process: Dict[str, Any] = None,
        process: float = None,
        report_time: str = None,
        report_title: str = None,
        skip_table_num: int = None,
        src_ds_id: str = None,
        src_ds_name: str = None,
        src_ds_type: str = None,
        src_engine_id: str = None,
        src_engine_name: str = None,
        src_engine_type: str = None,
        start_time: str = None,
        successful_table_num: int = None,
        task_description: str = None,
        task_mode: int = None,
        task_name: str = None,
        template_name: str = None,
    ):
        # The check result. Valid values:
        # - 0: no record.
        # - 1: passed.
        # - 2: failed.
        self.check_result = check_result
        # The number of checked tables.
        self.check_table_num = check_table_num
        # The check template ID.
        self.check_template_id = check_template_id
        # The check type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        self.check_type = check_type
        # The destination data source ID.
        self.dst_ds_id = dst_ds_id
        # The destination data source name.
        self.dst_ds_name = dst_ds_name
        # The destination data source type.
        self.dst_ds_type = dst_ds_type
        # The destination check engine ID.
        self.dst_engine_id = dst_engine_id
        # The destination check engine name.
        self.dst_engine_name = dst_engine_name
        # The destination check engine type.
        self.dst_engine_type = dst_engine_type
        # The end time.
        self.end_time = end_time
        # The error message.
        self.error_msg = error_msg
        # The number of error tables.
        self.error_table_num = error_table_num
        # The execution status. Valid values:
        # - 0: pending.
        # - 1: running.
        # - 2: stopped.
        # - 3: failed.
        # - 4: completed.
        self.exec_status = exec_status
        # The execution duration.
        self.exec_time = exec_time
        # The execution type. Valid values:
        # - 0: immediate execution.
        # - 1: scheduled execution.
        self.execute_type = execute_type
        # The creation time.
        self.gmt_create = gmt_create
        # The last modified time.
        self.gmt_modified = gmt_modified
        # The task ID.
        self.id = id
        # Indicates whether scheduling is enabled. Valid values:
        # - 0: Disabled.
        # - 1: Enabled.
        self.is_scheduled = is_scheduled
        # The latest batch ID.
        self.last_batch_id = last_batch_id
        # The latest completed batch ID.
        self.last_finished_id = last_finished_id
        # The check pass rate.
        self.pass_process = pass_process
        # The execution progress (0-1).
        self.process = process
        # The report time.
        self.report_time = report_time
        # The report title.
        self.report_title = report_title
        # The number of skipped tables.
        self.skip_table_num = skip_table_num
        # The source data source ID.
        self.src_ds_id = src_ds_id
        # The source data source name.
        self.src_ds_name = src_ds_name
        # The source data source type.
        self.src_ds_type = src_ds_type
        # The source check engine ID.
        self.src_engine_id = src_engine_id
        # The source check engine name.
        self.src_engine_name = src_engine_name
        # The source check engine type.
        self.src_engine_type = src_engine_type
        # The start time.
        self.start_time = start_time
        # The number of successful tables.
        self.successful_table_num = successful_table_num
        # The task description.
        self.task_description = task_description
        # The creation mode. Valid values:
        # - 0: table-by-table fine-grained mode.
        # - 1: same-schema batch mode.
        self.task_mode = task_mode
        # The task name.
        self.task_name = task_name
        # The check template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.check_table_num is not None:
            result['checkTableNum'] = self.check_table_num

        if self.check_template_id is not None:
            result['checkTemplateId'] = self.check_template_id

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.dst_ds_id is not None:
            result['dstDsId'] = self.dst_ds_id

        if self.dst_ds_name is not None:
            result['dstDsName'] = self.dst_ds_name

        if self.dst_ds_type is not None:
            result['dstDsType'] = self.dst_ds_type

        if self.dst_engine_id is not None:
            result['dstEngineId'] = self.dst_engine_id

        if self.dst_engine_name is not None:
            result['dstEngineName'] = self.dst_engine_name

        if self.dst_engine_type is not None:
            result['dstEngineType'] = self.dst_engine_type

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

        if self.execute_type is not None:
            result['executeType'] = self.execute_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled

        if self.last_batch_id is not None:
            result['lastBatchId'] = self.last_batch_id

        if self.last_finished_id is not None:
            result['lastFinishedId'] = self.last_finished_id

        if self.pass_process is not None:
            result['passProcess'] = self.pass_process

        if self.process is not None:
            result['process'] = self.process

        if self.report_time is not None:
            result['reportTime'] = self.report_time

        if self.report_title is not None:
            result['reportTitle'] = self.report_title

        if self.skip_table_num is not None:
            result['skipTableNum'] = self.skip_table_num

        if self.src_ds_id is not None:
            result['srcDsId'] = self.src_ds_id

        if self.src_ds_name is not None:
            result['srcDsName'] = self.src_ds_name

        if self.src_ds_type is not None:
            result['srcDsType'] = self.src_ds_type

        if self.src_engine_id is not None:
            result['srcEngineId'] = self.src_engine_id

        if self.src_engine_name is not None:
            result['srcEngineName'] = self.src_engine_name

        if self.src_engine_type is not None:
            result['srcEngineType'] = self.src_engine_type

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.successful_table_num is not None:
            result['successfulTableNum'] = self.successful_table_num

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.template_name is not None:
            result['templateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('checkTableNum') is not None:
            self.check_table_num = m.get('checkTableNum')

        if m.get('checkTemplateId') is not None:
            self.check_template_id = m.get('checkTemplateId')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('dstDsId') is not None:
            self.dst_ds_id = m.get('dstDsId')

        if m.get('dstDsName') is not None:
            self.dst_ds_name = m.get('dstDsName')

        if m.get('dstDsType') is not None:
            self.dst_ds_type = m.get('dstDsType')

        if m.get('dstEngineId') is not None:
            self.dst_engine_id = m.get('dstEngineId')

        if m.get('dstEngineName') is not None:
            self.dst_engine_name = m.get('dstEngineName')

        if m.get('dstEngineType') is not None:
            self.dst_engine_type = m.get('dstEngineType')

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

        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')

        if m.get('lastBatchId') is not None:
            self.last_batch_id = m.get('lastBatchId')

        if m.get('lastFinishedId') is not None:
            self.last_finished_id = m.get('lastFinishedId')

        if m.get('passProcess') is not None:
            self.pass_process = m.get('passProcess')

        if m.get('process') is not None:
            self.process = m.get('process')

        if m.get('reportTime') is not None:
            self.report_time = m.get('reportTime')

        if m.get('reportTitle') is not None:
            self.report_title = m.get('reportTitle')

        if m.get('skipTableNum') is not None:
            self.skip_table_num = m.get('skipTableNum')

        if m.get('srcDsId') is not None:
            self.src_ds_id = m.get('srcDsId')

        if m.get('srcDsName') is not None:
            self.src_ds_name = m.get('srcDsName')

        if m.get('srcDsType') is not None:
            self.src_ds_type = m.get('srcDsType')

        if m.get('srcEngineId') is not None:
            self.src_engine_id = m.get('srcEngineId')

        if m.get('srcEngineName') is not None:
            self.src_engine_name = m.get('srcEngineName')

        if m.get('srcEngineType') is not None:
            self.src_engine_type = m.get('srcEngineType')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('successfulTableNum') is not None:
            self.successful_table_num = m.get('successfulTableNum')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        return self

