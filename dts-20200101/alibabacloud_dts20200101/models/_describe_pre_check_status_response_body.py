# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePreCheckStatusResponseBody(DaraModel):
    def __init__(
        self,
        analysis_job_progress: List[main_models.DescribePreCheckStatusResponseBodyAnalysisJobProgress] = None,
        code: str = None,
        error_analysis_item: int = None,
        error_item: int = None,
        full_net_check_job_status: List[main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatus] = None,
        http_status_code: int = None,
        job_id: str = None,
        job_name: str = None,
        job_progress: List[main_models.DescribePreCheckStatusResponseBodyJobProgress] = None,
        network_diagnosis_result: main_models.DescribePreCheckStatusResponseBodyNetworkDiagnosisResult = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        state: str = None,
        sub_distributed_job_status: List[main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatus] = None,
        success: bool = None,
        total: int = None,
        total_record_count: int = None,
    ):
        # The list of evaluation tasks.
        self.analysis_job_progress = analysis_job_progress
        # The task code, which represents the queried subtask. Valid values:
        # - **01**: Precheck.
        # - **02**: Schema migration or initialization.
        # - **03**: Full data migration or initialization.
        # - **04**: Incremental migration or synchronization.
        self.code = code
        # The number of items that failed the evaluation.
        self.error_analysis_item = error_analysis_item
        # The number of specific items that caused the subtask to fail.
        self.error_item = error_item
        # The check result for all CIDR blocks.
        self.full_net_check_job_status = full_net_check_job_status
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the migration or synchronization task.
        self.job_id = job_id
        # The name of the queried subtask.
        self.job_name = job_name
        # The list of specific items and the execution progress of each item for the subtask.
        self.job_progress = job_progress
        # The network diagnosis result.
        self.network_diagnosis_result = network_diagnosis_result
        # The page number. Valid values: an integer greater than **0** and less than or equal to the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The maximum number of records that can be displayed on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The execution status of the subtask. Valid values:
        # - **NotStarted**: Not started.
        # - **Suspending**: Suspending.
        # - **Checking**: Checking.
        # - **Migrating**: Migrating.
        # - **Failed**: Failed.
        # - **Catched**: Incremental migration or synchronization in progress.
        # - **Finished**: Finished.
        self.state = state
        # The details of the distributed subtask.
        self.sub_distributed_job_status = sub_distributed_job_status
        # Indicates whether the request is successful.
        self.success = success
        # The total number of subtasks.
        self.total = total
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.analysis_job_progress:
            for v1 in self.analysis_job_progress:
                 if v1:
                    v1.validate()
        if self.full_net_check_job_status:
            for v1 in self.full_net_check_job_status:
                 if v1:
                    v1.validate()
        if self.job_progress:
            for v1 in self.job_progress:
                 if v1:
                    v1.validate()
        if self.network_diagnosis_result:
            self.network_diagnosis_result.validate()
        if self.sub_distributed_job_status:
            for v1 in self.sub_distributed_job_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnalysisJobProgress'] = []
        if self.analysis_job_progress is not None:
            for k1 in self.analysis_job_progress:
                result['AnalysisJobProgress'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.error_analysis_item is not None:
            result['ErrorAnalysisItem'] = self.error_analysis_item

        if self.error_item is not None:
            result['ErrorItem'] = self.error_item

        result['FullNetCheckJobStatus'] = []
        if self.full_net_check_job_status is not None:
            for k1 in self.full_net_check_job_status:
                result['FullNetCheckJobStatus'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        result['JobProgress'] = []
        if self.job_progress is not None:
            for k1 in self.job_progress:
                result['JobProgress'].append(k1.to_map() if k1 else None)

        if self.network_diagnosis_result is not None:
            result['NetworkDiagnosisResult'] = self.network_diagnosis_result.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        result['SubDistributedJobStatus'] = []
        if self.sub_distributed_job_status is not None:
            for k1 in self.sub_distributed_job_status:
                result['SubDistributedJobStatus'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis_job_progress = []
        if m.get('AnalysisJobProgress') is not None:
            for k1 in m.get('AnalysisJobProgress'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyAnalysisJobProgress()
                self.analysis_job_progress.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorAnalysisItem') is not None:
            self.error_analysis_item = m.get('ErrorAnalysisItem')

        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')

        self.full_net_check_job_status = []
        if m.get('FullNetCheckJobStatus') is not None:
            for k1 in m.get('FullNetCheckJobStatus'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatus()
                self.full_net_check_job_status.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k1 in m.get('JobProgress'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyJobProgress()
                self.job_progress.append(temp_model.from_map(k1))

        if m.get('NetworkDiagnosisResult') is not None:
            temp_model = main_models.DescribePreCheckStatusResponseBodyNetworkDiagnosisResult()
            self.network_diagnosis_result = temp_model.from_map(m.get('NetworkDiagnosisResult'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.sub_distributed_job_status = []
        if m.get('SubDistributedJobStatus') is not None:
            for k1 in m.get('SubDistributedJobStatus'):
                temp_model = main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatus()
                self.sub_distributed_job_status.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePreCheckStatusResponseBodySubDistributedJobStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_item: int = None,
        job_id: str = None,
        job_name: str = None,
        job_progress: List[main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress] = None,
        state: str = None,
        total: int = None,
    ):
        # The task code, which indicates the type of the queried subtask. Valid values:
        # 
        # - **01**: Precheck.
        # - **02**: Schema migration or initial schema synchronization.
        # - **03**: Full data migration or initial full data synchronization.
        # - **04**: Incremental data migration or incremental data synchronization.
        self.code = code
        # The number of failed tasks.
        self.error_item = error_item
        # The job ID.
        self.job_id = job_id
        # The name of the distributed subtask associated with the task.
        self.job_name = job_name
        # The list of specific items and the execution progress of each item for the subtask.
        self.job_progress = job_progress
        # The execution status of the subtask. Valid values:
        # - **NotStarted**: Not started.
        # - **Suspending**: Suspending.
        # - **Checking**: Checking.
        # - **Migrating**: Migrating.
        # - **Failed**: Failed.
        # - **Catched**: Incremental migration or synchronization in progress.
        # - **Finished**: Finished.
        self.state = state
        # The total number of returned records.
        self.total = total

    def validate(self):
        if self.job_progress:
            for v1 in self.job_progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_item is not None:
            result['ErrorItem'] = self.error_item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        result['JobProgress'] = []
        if self.job_progress is not None:
            for k1 in self.job_progress:
                result['JobProgress'].append(k1.to_map() if k1 else None)

        if self.state is not None:
            result['State'] = self.state

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k1 in m.get('JobProgress'):
                temp_model = main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress()
                self.job_progress.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        current: str = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        # The start time of the specific item, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.boot_time = boot_time
        # Indicates whether DTS supports skipping the item after it fails. Valid values:
        # * **true**: Yes.
        # * **false**: No.
        self.can_skip = can_skip
        # The number of currently running subtasks.
        self.current = current
        # The executed DDL operation.
        self.ddl_sql = ddl_sql
        # The incremental data migration or synchronization latency.
        self.delay_seconds = delay_seconds
        # The name of the database to which the migrated object belongs in the destination instance.
        self.dest_schema = dest_schema
        # This parameter will be deprecated soon.
        self.diff_row = diff_row
        # The error details when the specific item fails.
        self.err_detail = err_detail
        # The error message when the specific item fails.
        self.err_msg = err_msg
        # The completion time. The time follows the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The ID of the record in the metadatabase.
        self.id = id
        # Indicates whether the specific item is directly ignored to proceed to the next specific item. Valid values:
        # - **N**: No.
        # - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # The name of the specific item.
        self.item = item
        # The job ID.
        self.job_id = job_id
        # The execution log information for errors.
        self.logs = logs
        # The name of the specific item.
        self.names = names
        # The item number.
        self.order_num = order_num
        # This parameter will be deprecated soon.
        self.parent_obj = parent_obj
        # The solution to a precheck failure.
        self.repair_method = repair_method
        # Indicates whether the task is skipped. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.skip = skip
        # The name of the database to which the migrated object belongs in the source instance.
        self.source_schema = source_schema
        # The execution status of the subtask. Valid values:
        # - **NotStarted**: Not started.
        # - **Suspending**: Suspending.
        # - **Checking**: Checking.
        # - **Migrating**: Migrating.
        # - **Failed**: Failed.
        # - **Catched**: Incremental migration or synchronization in progress.
        # - **Finished**: Finished.
        self.state = state
        # The progress of the sub-items of the specific item.
        # > If <b>[]</b> is returned, no sub-items exist.
        self.sub = sub
        # The names of the destination objects.
        self.target_names = target_names
        # The total number of items.
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip

        if self.current is not None:
            result['Current'] = self.current

        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema

        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row

        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag

        if self.item is not None:
            result['Item'] = self.item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.names is not None:
            result['Names'] = self.names

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj

        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema

        if self.state is not None:
            result['State'] = self.state

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.target_names is not None:
            result['TargetNames'] = self.target_names

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')

        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')

        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs(DaraModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        # The error record.
        self.err_data = err_data
        # The specific error message.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The log level.
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_data is not None:
            result['ErrData'] = self.err_data

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.err_type is not None:
            result['ErrType'] = self.err_type

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        return self

class DescribePreCheckStatusResponseBodyNetworkDiagnosisResult(DaraModel):
    def __init__(
        self,
        diagnosis: List[main_models.DescribePreCheckStatusResponseBodyNetworkDiagnosisResultDiagnosis] = None,
        model_version: str = None,
    ):
        # The network diagnostic report.
        self.diagnosis = diagnosis
        # The version of the diagnosis model.
        self.model_version = model_version

    def validate(self):
        if self.diagnosis:
            for v1 in self.diagnosis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Diagnosis'] = []
        if self.diagnosis is not None:
            for k1 in self.diagnosis:
                result['Diagnosis'].append(k1.to_map() if k1 else None)

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnosis = []
        if m.get('Diagnosis') is not None:
            for k1 in m.get('Diagnosis'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyNetworkDiagnosisResultDiagnosis()
                self.diagnosis.append(temp_model.from_map(k1))

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        return self

class DescribePreCheckStatusResponseBodyNetworkDiagnosisResultDiagnosis(DaraModel):
    def __init__(
        self,
        cn_doc_url: str = None,
        code: str = None,
        endpoint_type: str = None,
        international_doc_url: str = None,
        result: str = None,
    ):
        # The documentation URL for the China site.
        self.cn_doc_url = cn_doc_url
        # The diagnosis code.
        self.code = code
        # The endpoint type. Valid values:
        # - **source**: The source endpoint.
        # - **destination**: The destination endpoint.
        # - **unknown**: Unknown.
        self.endpoint_type = endpoint_type
        # The documentation URL for regions outside China.
        self.international_doc_url = international_doc_url
        # The reserved field for the diagnosis result. Default value: empty.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_doc_url is not None:
            result['CnDocUrl'] = self.cn_doc_url

        if self.code is not None:
            result['Code'] = self.code

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.international_doc_url is not None:
            result['InternationalDocUrl'] = self.international_doc_url

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnDocUrl') is not None:
            self.cn_doc_url = m.get('CnDocUrl')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('InternationalDocUrl') is not None:
            self.international_doc_url = m.get('InternationalDocUrl')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class DescribePreCheckStatusResponseBodyJobProgress(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        current: str = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[main_models.DescribePreCheckStatusResponseBodyJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        # The start time of the specific item, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.boot_time = boot_time
        # Indicates whether DTS supports skipping the specific item after it fails.
        self.can_skip = can_skip
        # The number of currently running subtasks.
        self.current = current
        # The executed DDL operation.
        self.ddl_sql = ddl_sql
        # The incremental migration or synchronization latency.
        self.delay_seconds = delay_seconds
        # The name of the database to which the migrated object belongs in the destination instance.
        self.dest_schema = dest_schema
        # This parameter will be deprecated soon.
        self.diff_row = diff_row
        # The error details when the specific item fails.
        self.err_detail = err_detail
        # The error message when the specific item fails.
        self.err_msg = err_msg
        # The completion time of the specific item, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>ZZ format (UTC).
        self.finish_time = finish_time
        # The ID recorded in the metadatabase.
        self.id = id
        # Indicates whether the specific item is directly ignored to proceed to the next specific item. Valid values:
        # - **N**: No.
        # - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # The short name of the specific item.
        self.item = item
        # The ID of the subtask.
        self.job_id = job_id
        # The execution logs of the specific error.
        self.logs = logs
        # The name of the specific item.
        self.names = names
        # The item number.
        self.order_num = order_num
        # This parameter will be deprecated soon.
        self.parent_obj = parent_obj
        # The solution if the specific item fails.
        self.repair_method = repair_method
        # Indicates whether the specific item is configured to be skipped after it fails. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.skip = skip
        # The name of the database to which the migrated object belongs in the source instance.
        self.source_schema = source_schema
        # The execution progress status of the specific item. Valid values:
        # - **NotStarted**: Not started.
        # - **Checking**: Checking.
        # - **Migrating**: Migrating.
        # - **Failed**: Failed.
        # - **Warning**: Warning.
        # - **Success**: Successful.
        self.state = state
        # The progress of the sub-items of the specific item.
        # > If <b>[]</b> is returned, no sub-items exist.
        self.sub = sub
        # The names of the objects to be migrated or synchronized.
        self.target_names = target_names
        # The total number of specific items for the subtask.
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip

        if self.current is not None:
            result['Current'] = self.current

        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema

        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row

        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag

        if self.item is not None:
            result['Item'] = self.item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.names is not None:
            result['Names'] = self.names

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj

        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema

        if self.state is not None:
            result['State'] = self.state

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.target_names is not None:
            result['TargetNames'] = self.target_names

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')

        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')

        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyJobProgressLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodyJobProgressLogs(DaraModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        # The error message.
        self.err_data = err_data
        # The DTS error message when the specific item fails.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The log level.
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_data is not None:
            result['ErrData'] = self.err_data

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.err_type is not None:
            result['ErrType'] = self.err_type

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        return self

class DescribePreCheckStatusResponseBodyFullNetCheckJobStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        dest_region: str = None,
        dest_region_cidr: str = None,
        destination_endpoint_type: str = None,
        error_item: int = None,
        host_region: str = None,
        job_id: str = None,
        job_name: str = None,
        job_progress: List[main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgress] = None,
        source_endpoint_type: str = None,
        src_region: str = None,
        src_region_cidr: str = None,
        state: str = None,
        total: int = None,
    ):
        # The task code. A value of **01** indicates a precheck.
        self.code = code
        # The region ID of the destination CIDR block.
        self.dest_region = dest_region
        # The destination CIDR block.
        self.dest_region_cidr = dest_region_cidr
        # The connection method of the destination instance. Valid values:
        # - **ALIYUN**: Alibaba Cloud instance.
        # - **OTHER**: Public IP address.
        # - **ECS**: Self-managed database hosted on ECS.
        # - **EXPRESS**: Express Connect circuit, VPN gateway, or Smart Access Gateway.
        # - **CEN**: Cloud Enterprise Network (CEN).
        # - **DG**: Database Gateway.
        self.destination_endpoint_type = destination_endpoint_type
        # The number of items that failed the precheck.
        self.error_item = error_item
        # The region ID of the node where the instance runs.
        self.host_region = host_region
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The list of specific items and the execution progress of each item for the task.
        self.job_progress = job_progress
        # The connection method of the source instance. Valid values:
        # - **ALIYUN**: Alibaba Cloud instance.
        # - **OTHER**: Public IP address.
        # - **ECS**: Self-managed database hosted on ECS.
        # - **EXPRESS**: Express Connect circuit, VPN gateway, or Smart Access Gateway.
        # - **CEN**: Cloud Enterprise Network (CEN).
        # - **DG**: Database Gateway.
        self.source_endpoint_type = source_endpoint_type
        # The region ID of the source CIDR block.
        self.src_region = src_region
        # The source CIDR block.
        self.src_region_cidr = src_region_cidr
        # The check result. Valid values:
        # - **Failed**: The check failed.
        # - **Success**: The check succeeded.
        self.state = state
        # The total number of items.
        self.total = total

    def validate(self):
        if self.job_progress:
            for v1 in self.job_progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_region_cidr is not None:
            result['DestRegionCidr'] = self.dest_region_cidr

        if self.destination_endpoint_type is not None:
            result['DestinationEndpointType'] = self.destination_endpoint_type

        if self.error_item is not None:
            result['ErrorItem'] = self.error_item

        if self.host_region is not None:
            result['HostRegion'] = self.host_region

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        result['JobProgress'] = []
        if self.job_progress is not None:
            for k1 in self.job_progress:
                result['JobProgress'].append(k1.to_map() if k1 else None)

        if self.source_endpoint_type is not None:
            result['SourceEndpointType'] = self.source_endpoint_type

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_region_cidr is not None:
            result['SrcRegionCidr'] = self.src_region_cidr

        if self.state is not None:
            result['State'] = self.state

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestRegionCidr') is not None:
            self.dest_region_cidr = m.get('DestRegionCidr')

        if m.get('DestinationEndpointType') is not None:
            self.destination_endpoint_type = m.get('DestinationEndpointType')

        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')

        if m.get('HostRegion') is not None:
            self.host_region = m.get('HostRegion')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k1 in m.get('JobProgress'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgress()
                self.job_progress.append(temp_model.from_map(k1))

        if m.get('SourceEndpointType') is not None:
            self.source_endpoint_type = m.get('SourceEndpointType')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcRegionCidr') is not None:
            self.src_region_cidr = m.get('SrcRegionCidr')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgress(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        current: str = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        # The start time of the specific item, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.boot_time = boot_time
        # Indicates whether DTS supports skipping the item after it fails. Valid values:
        # * **true**: Yes.
        # * **false**: No.
        self.can_skip = can_skip
        # The number of currently running tasks.
        self.current = current
        # The executed DDL operation.
        self.ddl_sql = ddl_sql
        # The task latency.
        self.delay_seconds = delay_seconds
        # The name of the database to which the migrated object belongs in the destination instance.
        self.dest_schema = dest_schema
        # This parameter will be deprecated soon.
        self.diff_row = diff_row
        # The error details when the specific item fails.
        self.err_detail = err_detail
        # The error message when the specific item fails.
        self.err_msg = err_msg
        # The task completion time. The time follows the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.finish_time = finish_time
        # The ID of the record in the metadatabase.
        self.id = id
        # Indicates whether the specific item is directly ignored to proceed to the next specific item. Valid values:
        # - **N**: No.
        # - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # The name of the specific item.
        self.item = item
        # The job ID.
        self.job_id = job_id
        # The execution log information for errors.
        self.logs = logs
        # The name of the specific item.
        self.names = names
        # The item number.
        self.order_num = order_num
        # This parameter will be deprecated soon.
        self.parent_obj = parent_obj
        # The solution to a precheck failure.
        self.repair_method = repair_method
        # Indicates whether the specific item is configured to be skipped after it fails. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.skip = skip
        # The name of the database to which the migrated object belongs in the source instance.
        self.source_schema = source_schema
        # The check result. Valid values:
        # - **Failed**: The check failed.
        # - **Success**: The check succeeded.
        self.state = state
        # The progress of the sub-items of the specific item.
        # > If <b>[]</b> is returned, no sub-items exist.
        self.sub = sub
        # The names of the destination objects.
        self.target_names = target_names
        # The total number of items.
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip

        if self.current is not None:
            result['Current'] = self.current

        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema

        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row

        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag

        if self.item is not None:
            result['Item'] = self.item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.names is not None:
            result['Names'] = self.names

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj

        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema

        if self.state is not None:
            result['State'] = self.state

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.target_names is not None:
            result['TargetNames'] = self.target_names

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')

        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')

        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgressLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodyFullNetCheckJobStatusJobProgressLogs(DaraModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        # The error record.
        self.err_data = err_data
        # The specific error message.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The log level.
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_data is not None:
            result['ErrData'] = self.err_data

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.err_type is not None:
            result['ErrType'] = self.err_type

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        return self

class DescribePreCheckStatusResponseBodyAnalysisJobProgress(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        can_skip: bool = None,
        current: str = None,
        ddl_sql: str = None,
        delay_seconds: int = None,
        dest_schema: str = None,
        diff_row: int = None,
        err_detail: str = None,
        err_msg: str = None,
        finish_time: str = None,
        id: str = None,
        ignore_flag: str = None,
        item: str = None,
        job_id: str = None,
        logs: List[main_models.DescribePreCheckStatusResponseBodyAnalysisJobProgressLogs] = None,
        names: str = None,
        order_num: int = None,
        parent_obj: str = None,
        repair_method: str = None,
        skip: bool = None,
        source_schema: str = None,
        state: str = None,
        sub: str = None,
        target_names: str = None,
        total: int = None,
    ):
        # The start time of the specific item, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.boot_time = boot_time
        # Indicates whether the sub-item can be skipped.
        self.can_skip = can_skip
        # The number of currently running subtasks.
        self.current = current
        # The executed DDL operation.
        self.ddl_sql = ddl_sql
        # The task latency.
        self.delay_seconds = delay_seconds
        # The name of the database to which the migrated object belongs in the destination instance.
        self.dest_schema = dest_schema
        # This parameter will be deprecated soon.
        self.diff_row = diff_row
        # The error details when the item fails.
        self.err_detail = err_detail
        # The specific error message.
        self.err_msg = err_msg
        # The end time of the evaluation task, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.finish_time = finish_time
        # The ID of the evaluation item in the database.
        self.id = id
        # Indicates whether the specific item is directly ignored to proceed to the next specific item. Valid values:
        # - **N**: No.
        # - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # The name of the evaluation item.
        self.item = item
        # The ID of the evaluation task.
        self.job_id = job_id
        # The sub-evaluation items.
        self.logs = logs
        # The name of the evaluation item.
        self.names = names
        # The number of the evaluation item.
        self.order_num = order_num
        # This parameter will be deprecated soon.
        self.parent_obj = parent_obj
        # The solution for the evaluation item.
        self.repair_method = repair_method
        # Indicates whether the evaluation item is configured to be skipped after it fails. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.skip = skip
        # The name of the database to which the migrated object belongs in the source instance.
        self.source_schema = source_schema
        # The result of the evaluation item. Valid values:
        # - **Failed**: Failed.
        # - **Success**: Successful.
        self.state = state
        # The progress of the sub-items of the specific item.
        # > If <b>[]</b> is returned, no sub-items exist.
        self.sub = sub
        # The names of the destination objects.
        self.target_names = target_names
        # The total number of specific items for the subtask.
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip

        if self.current is not None:
            result['Current'] = self.current

        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema

        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row

        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag

        if self.item is not None:
            result['Item'] = self.item

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.names is not None:
            result['Names'] = self.names

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj

        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema

        if self.state is not None:
            result['State'] = self.state

        if self.sub is not None:
            result['Sub'] = self.sub

        if self.target_names is not None:
            result['TargetNames'] = self.target_names

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')

        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')

        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribePreCheckStatusResponseBodyAnalysisJobProgressLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Sub') is not None:
            self.sub = m.get('Sub')

        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribePreCheckStatusResponseBodyAnalysisJobProgressLogs(DaraModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        err_type: str = None,
        log_level: str = None,
    ):
        # The error message.
        self.err_data = err_data
        # The DTS error message when the specific item fails.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The log level.
        self.log_level = log_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_data is not None:
            result['ErrData'] = self.err_data

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.err_type is not None:
            result['ErrType'] = self.err_type

        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')

        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        return self

