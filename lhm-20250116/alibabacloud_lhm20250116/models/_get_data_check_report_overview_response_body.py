# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetDataCheckReportOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataCheckReportOverviewResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response data.
        self.data = data
        # The fault information code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The request ID. This value uniquely identifies the call. Provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.GetDataCheckReportOverviewResponseBodyData()
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

class GetDataCheckReportOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        check_column_count: int = None,
        check_pt_count: int = None,
        check_result: int = None,
        check_row_count: int = None,
        check_row_pass_count: int = None,
        check_row_pass_export: str = None,
        check_sql_num: int = None,
        check_table_num: int = None,
        check_template_id: str = None,
        check_template_name: str = None,
        check_type: int = None,
        dst_ds_name: str = None,
        dst_ds_type: str = None,
        error_table_num: int = None,
        pass_column_count: int = None,
        pass_column_rate: float = None,
        pass_process: float = None,
        pass_process_export: str = None,
        pass_pt_num: int = None,
        pass_pt_process_export: str = None,
        pass_table_num: int = None,
        pt_pass_process: float = None,
        report_generate_message: str = None,
        report_status: int = None,
        report_time: str = None,
        report_title: str = None,
        skip_pt_num: int = None,
        skip_table_num: int = None,
        src_ds_name: str = None,
        src_ds_type: str = None,
        task_create_time: str = None,
        task_id: int = None,
        task_modify_time: str = None,
        task_name: str = None,
    ):
        # The ID of the validation job (batch).
        self.batch_id = batch_id
        # The number of validated fields.
        self.check_column_count = check_column_count
        # The number of validated partitions.
        self.check_pt_count = check_pt_count
        # The validation result. Valid values:
        # - 0: No record.
        # - 1: Passed.
        # - 2: Failed.
        self.check_result = check_result
        # The number of validated data rows.
        self.check_row_count = check_row_count
        # The number of rows that passed validation.
        self.check_row_pass_count = check_row_pass_count
        # The row pass rate for the export report. This value is calculated by dividing the number of passed rows by the total number of validated rows. The value is returned as a percentage string with two decimal places.
        self.check_row_pass_export = check_row_pass_export
        # The number of validation SQL statements.
        self.check_sql_num = check_sql_num
        # The number of validated tables.
        self.check_table_num = check_table_num
        # The validation template name. This field is available only for metric validation.
        self.check_template_id = check_template_id
        # The validation template name. This field is available only for metric validation.
        self.check_template_name = check_template_name
        # The validation type. Valid values:
        # - 0: data volume comparison.
        # - 1: metric comparison.
        # - 2: weak content comparison.
        self.check_type = check_type
        # The name of the destination datasource.
        self.dst_ds_name = dst_ds_name
        # The type of the destination datasource.
        self.dst_ds_type = dst_ds_type
        # The number of tables with errors.
        self.error_table_num = error_table_num
        # The number of fields that passed validation.
        self.pass_column_count = pass_column_count
        # The number of metrics that passed validation.
        self.pass_column_rate = pass_column_rate
        # The pass rate.
        self.pass_process = pass_process
        # The pass rate for the export report. This value is calculated by dividing the number of passed tables by the total number of validated tables. The value is returned as a percentage string with two decimal places (for example, 100.00%). A hyphen (-) is returned when no validated table data exists.
        self.pass_process_export = pass_process_export
        # The number of partitions that passed validation.
        self.pass_pt_num = pass_pt_num
        # The partition pass rate for the export report. This value is calculated by dividing the number of passed partitions by the total number of validated partitions. The value is returned as a percentage string with four decimal places. A hyphen (-) is returned when no partition data exists.
        self.pass_pt_process_export = pass_pt_process_export
        # The number of tables that passed validation.
        self.pass_table_num = pass_table_num
        # The partition pass rate.
        self.pt_pass_process = pt_pass_process
        # The report generation message.
        self.report_generate_message = report_generate_message
        # The validation report status. Valid values:
        # - 0: Not generated.
        # - 1: Generating.
        # - 2: Generated.
        self.report_status = report_status
        # The time when the report was generated.
        self.report_time = report_time
        # The title of the validation report.
        self.report_title = report_title
        # The number of skipped partitions.
        self.skip_pt_num = skip_pt_num
        # The number of skipped tables.
        self.skip_table_num = skip_table_num
        # The name of the source datasource.
        self.src_ds_name = src_ds_name
        # The type of the source datasource.
        self.src_ds_type = src_ds_type
        # The time when the task was created.
        self.task_create_time = task_create_time
        # The task ID.
        self.task_id = task_id
        # The time when the task was last modified.
        self.task_modify_time = task_modify_time
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.check_column_count is not None:
            result['checkColumnCount'] = self.check_column_count

        if self.check_pt_count is not None:
            result['checkPtCount'] = self.check_pt_count

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.check_row_count is not None:
            result['checkRowCount'] = self.check_row_count

        if self.check_row_pass_count is not None:
            result['checkRowPassCount'] = self.check_row_pass_count

        if self.check_row_pass_export is not None:
            result['checkRowPassExport'] = self.check_row_pass_export

        if self.check_sql_num is not None:
            result['checkSqlNum'] = self.check_sql_num

        if self.check_table_num is not None:
            result['checkTableNum'] = self.check_table_num

        if self.check_template_id is not None:
            result['checkTemplateId'] = self.check_template_id

        if self.check_template_name is not None:
            result['checkTemplateName'] = self.check_template_name

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.dst_ds_name is not None:
            result['dstDsName'] = self.dst_ds_name

        if self.dst_ds_type is not None:
            result['dstDsType'] = self.dst_ds_type

        if self.error_table_num is not None:
            result['errorTableNum'] = self.error_table_num

        if self.pass_column_count is not None:
            result['passColumnCount'] = self.pass_column_count

        if self.pass_column_rate is not None:
            result['passColumnRate'] = self.pass_column_rate

        if self.pass_process is not None:
            result['passProcess'] = self.pass_process

        if self.pass_process_export is not None:
            result['passProcessExport'] = self.pass_process_export

        if self.pass_pt_num is not None:
            result['passPtNum'] = self.pass_pt_num

        if self.pass_pt_process_export is not None:
            result['passPtProcessExport'] = self.pass_pt_process_export

        if self.pass_table_num is not None:
            result['passTableNum'] = self.pass_table_num

        if self.pt_pass_process is not None:
            result['ptPassProcess'] = self.pt_pass_process

        if self.report_generate_message is not None:
            result['reportGenerateMessage'] = self.report_generate_message

        if self.report_status is not None:
            result['reportStatus'] = self.report_status

        if self.report_time is not None:
            result['reportTime'] = self.report_time

        if self.report_title is not None:
            result['reportTitle'] = self.report_title

        if self.skip_pt_num is not None:
            result['skipPtNum'] = self.skip_pt_num

        if self.skip_table_num is not None:
            result['skipTableNum'] = self.skip_table_num

        if self.src_ds_name is not None:
            result['srcDsName'] = self.src_ds_name

        if self.src_ds_type is not None:
            result['srcDsType'] = self.src_ds_type

        if self.task_create_time is not None:
            result['taskCreateTime'] = self.task_create_time

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_modify_time is not None:
            result['taskModifyTime'] = self.task_modify_time

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('checkColumnCount') is not None:
            self.check_column_count = m.get('checkColumnCount')

        if m.get('checkPtCount') is not None:
            self.check_pt_count = m.get('checkPtCount')

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('checkRowCount') is not None:
            self.check_row_count = m.get('checkRowCount')

        if m.get('checkRowPassCount') is not None:
            self.check_row_pass_count = m.get('checkRowPassCount')

        if m.get('checkRowPassExport') is not None:
            self.check_row_pass_export = m.get('checkRowPassExport')

        if m.get('checkSqlNum') is not None:
            self.check_sql_num = m.get('checkSqlNum')

        if m.get('checkTableNum') is not None:
            self.check_table_num = m.get('checkTableNum')

        if m.get('checkTemplateId') is not None:
            self.check_template_id = m.get('checkTemplateId')

        if m.get('checkTemplateName') is not None:
            self.check_template_name = m.get('checkTemplateName')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('dstDsName') is not None:
            self.dst_ds_name = m.get('dstDsName')

        if m.get('dstDsType') is not None:
            self.dst_ds_type = m.get('dstDsType')

        if m.get('errorTableNum') is not None:
            self.error_table_num = m.get('errorTableNum')

        if m.get('passColumnCount') is not None:
            self.pass_column_count = m.get('passColumnCount')

        if m.get('passColumnRate') is not None:
            self.pass_column_rate = m.get('passColumnRate')

        if m.get('passProcess') is not None:
            self.pass_process = m.get('passProcess')

        if m.get('passProcessExport') is not None:
            self.pass_process_export = m.get('passProcessExport')

        if m.get('passPtNum') is not None:
            self.pass_pt_num = m.get('passPtNum')

        if m.get('passPtProcessExport') is not None:
            self.pass_pt_process_export = m.get('passPtProcessExport')

        if m.get('passTableNum') is not None:
            self.pass_table_num = m.get('passTableNum')

        if m.get('ptPassProcess') is not None:
            self.pt_pass_process = m.get('ptPassProcess')

        if m.get('reportGenerateMessage') is not None:
            self.report_generate_message = m.get('reportGenerateMessage')

        if m.get('reportStatus') is not None:
            self.report_status = m.get('reportStatus')

        if m.get('reportTime') is not None:
            self.report_time = m.get('reportTime')

        if m.get('reportTitle') is not None:
            self.report_title = m.get('reportTitle')

        if m.get('skipPtNum') is not None:
            self.skip_pt_num = m.get('skipPtNum')

        if m.get('skipTableNum') is not None:
            self.skip_table_num = m.get('skipTableNum')

        if m.get('srcDsName') is not None:
            self.src_ds_name = m.get('srcDsName')

        if m.get('srcDsType') is not None:
            self.src_ds_type = m.get('srcDsType')

        if m.get('taskCreateTime') is not None:
            self.task_create_time = m.get('taskCreateTime')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskModifyTime') is not None:
            self.task_modify_time = m.get('taskModifyTime')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

