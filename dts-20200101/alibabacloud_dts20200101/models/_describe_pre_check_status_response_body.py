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
        # Display list of evaluation tasks
        self.analysis_job_progress = analysis_job_progress
        # The task code that indicates the type of the subtask. Valid values:
        # 
        # *   **01**: precheck.
        # *   **02**: schema migration or initial schema synchronization.
        # *   **03**: full data migration or initial full data synchronization.
        # *   **04**: incremental data migration or synchronization.
        self.code = code
        # Number of failed evaluation items
        self.error_analysis_item = error_analysis_item
        # The total number of subtask failures.
        self.error_item = error_item
        # Network-wide inspection results.
        self.full_net_check_job_status = full_net_check_job_status
        # The status code that is returned.
        self.http_status_code = http_status_code
        # The ID of the data migration or synchronization task.
        self.job_id = job_id
        # The name of the subtask.
        self.job_name = job_name
        # The subtasks and the progress of each subtask.
        self.job_progress = job_progress
        # Network diagnosis result
        self.network_diagnosis_result = network_diagnosis_result
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The status of the subtask. Valid values:
        # 
        # *   **NotStarted**: The subtask is not started.
        # *   **Suspending**: The subtask is paused.
        # *   **Checking**: The subtask is being checked.
        # *   **Migrating**: The subtask is in progress. Data is being migrated.
        # *   **Failed**: The subtask failed.
        # *   **Catched**: The subtask is in progress. Incremental data is being migrated or synchronized.
        # *   **Finished**: The subtask is complete.
        self.state = state
        # The information about the distributed subtasks.
        self.sub_distributed_job_status = sub_distributed_job_status
        # Indicates whether the request is successful.
        self.success = success
        # The total number of subtasks.
        self.total = total
        # The total number of entries that are returned.
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
        # The task code that indicates the type of the subtask. Valid values:
        # 
        # *   **01**: precheck.
        # *   **02**: schema migration or initial schema synchronization.
        # *   **03**: full data migration or initial full data synchronization.
        # *   **04**: incremental data migration or synchronization.
        self.code = code
        # The number of subtasks that failed.
        self.error_item = error_item
        # The subtask ID.
        self.job_id = job_id
        # The name of distributed subtasks associated with the subtask.
        self.job_name = job_name
        # The subtasks and the progress of each subtask.
        self.job_progress = job_progress
        # The status of the subtask. Valid values:
        # 
        # *   **NotStarted**: The subtask is not started.
        # *   **Suspending**: The subtask is paused.
        # *   **Checking**: The subtask is being checked.
        # *   **Migrating**: The subtask is in progress. Data is being migrated.
        # *   **Failed**: The subtask failed.
        # *   **Catched**: The subtask is in progress. Incremental data is being migrated or synchronized.
        # *   **Finished**: The subtask is complete.
        self.state = state
        # The total number of entries that are returned.
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
        # The time when the subtask was started. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.boot_time = boot_time
        # Indicates whether the subtask can be ignored if it fails. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_skip = can_skip
        # The number of the subtasks that are running.
        self.current = current
        # The DDL statements.
        self.ddl_sql = ddl_sql
        # The latency of incremental data migration or synchronization.
        self.delay_seconds = delay_seconds
        # The name of the database to which the object in the destination instance belongs.
        self.dest_schema = dest_schema
        # This parameter will be removed in the future.
        self.diff_row = diff_row
        # The error details of the subtask failure.
        self.err_detail = err_detail
        # The error message of the subtask failure.
        self.err_msg = err_msg
        # The time when the subtask was complete. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.finish_time = finish_time
        # The ID of the entry in the metadatabase.
        self.id = id
        # Indicates whether DTS ignores the subtask and proceeds with the next subtask. Valid values:
        # 
        # *   **N**: no.
        # *   **Y**: yes.
        self.ignore_flag = ignore_flag
        # The name of the subtask.
        self.item = item
        # The subtask ID.
        self.job_id = job_id
        # The operations logs of errors.
        self.logs = logs
        # The name of the subtask.
        self.names = names
        # The serial number of the subtask.
        self.order_num = order_num
        # This parameter will be removed in the future.
        self.parent_obj = parent_obj
        # The method to fix a precheck failure.
        self.repair_method = repair_method
        # Indicates whether the subtask was ignored. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.skip = skip
        # The name of the database to which the object in the source instance belongs.
        self.source_schema = source_schema
        # The status of the subtask. Valid values:
        # 
        # *   **NotStarted**: The subtask is not started.
        # *   **Suspending**: The subtask is paused.
        # *   **Checking**: The subtask is being checked.
        # *   **Migrating**: The subtask is in progress. Data is being migrated.
        # *   **Failed**: The subtask failed.
        # *   **Catched**: The subtask is in progress. Incremental data is being migrated or synchronized.
        # *   **Finished**: The subtask is complete.
        self.state = state
        # The sub-item progress of the subtask.
        # 
        # > If \\*\\*[]\\*\\* is returned, the subtask has no sub-item.
        self.sub = sub
        # The names of the objects that are migrated or synchronized.
        self.target_names = target_names
        # The total number of subtasks.
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
        # The record of errors.
        self.err_data = err_data
        # The error message.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The level of logs.
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
        # Network diagnostic report
        self.diagnosis = diagnosis
        # Diagnose model version.
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
        # Document address for China region.
        self.cn_doc_url = cn_doc_url
        # Diagnostic code.
        self.code = code
        # Access point, the return values are: - **source**: source end. - **destination**: destination end. - **unknown**: unknown.
        self.endpoint_type = endpoint_type
        # Overseas region document address.
        self.international_doc_url = international_doc_url
        # Reserved field for diagnostic results, default is empty.
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
        # The time when the subtask was started. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC.
        self.boot_time = boot_time
        # Indicates whether the subtask can be ignored if it fails.
        self.can_skip = can_skip
        # The number of the subtasks that are running.
        self.current = current
        # The DDL statements.
        self.ddl_sql = ddl_sql
        # The latency of incremental data migration or synchronization.
        # 
        # > If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        self.delay_seconds = delay_seconds
        # The name of the database to which the object in the destination instance belongs.
        self.dest_schema = dest_schema
        # This parameter will be removed in the future.
        self.diff_row = diff_row
        # The error details of the subtask failure.
        self.err_detail = err_detail
        # The error message of the subtask failure.
        self.err_msg = err_msg
        # The time when the subtask was complete. The time is displayed in the yyyy-MM-ddTHH:mm:ssZ format in UTC.
        self.finish_time = finish_time
        # The ID of the entry in the metadatabase.
        self.id = id
        # Indicates whether DTS ignores the subtask and proceeds with the next subtask. Valid values:
        # 
        # *   **N**: no.
        # *   **Y**: yes.
        self.ignore_flag = ignore_flag
        # The shortened name of the subtask.
        self.item = item
        # The subtask ID.
        self.job_id = job_id
        # The logs of subtask failures.
        self.logs = logs
        # The name of the subtask.
        self.names = names
        # The serial number of the subtask.
        self.order_num = order_num
        # This parameter will be removed in the future.
        self.parent_obj = parent_obj
        # The method to fix the subtask failure.
        self.repair_method = repair_method
        # Indicates whether the subtask is ignored if it fails. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.skip = skip
        # The name of the database to which the object in the source instance belongs.
        self.source_schema = source_schema
        # The status of the subtask. Valid values:
        # 
        # *   **NotStarted**: The subtask is not started.
        # *   **Checking**: The subtask is being checked.
        # *   **Migrating**: The subtask is in progress. Data is being migrated.
        # *   **Failed**: The subtask failed.
        # *   **Warning**: The subtask encounters an exception.
        # *   **Success**: The subtask is complete.
        self.state = state
        # The sub-item progress of the subtask.
        # 
        # > If \\*\\*[]\\*\\* is returned, the subtask has no sub-items.
        self.sub = sub
        # The names of the objects that are migrated or synchronized.
        self.target_names = target_names
        # The total number of sub-items of the subtask.
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
        # The error message that is returned when an error occurs on the subtask.
        self.err_msg = err_msg
        # The error type.
        self.err_type = err_type
        # The level of logs.
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
        # Task code, **01** represents pre-check.
        self.code = code
        # ID of the region to which the target network segment belongs.
        self.dest_region = dest_region
        # Destination network segment.
        self.dest_region_cidr = dest_region_cidr
        # The access method of the target instance, with return values as follows: - **ALIYUN**: Access method is **cloud instance**. - **OTHER**: Access method is **public IP**. - **ECS**: Access method is **ECS self-built database**. - **EXPRESS**: Access method is **Express Connect / VPN Gateway / Smart Gateway**. - **CEN**: Access method is **Cloud Enterprise Network (CEN)**. - **DG**: Access method is **Database Gateway (DG)**.
        self.destination_endpoint_type = destination_endpoint_type
        # Number of pre-check failed items
        self.error_item = error_item
        # The region ID of the instance\\"s running node.
        self.host_region = host_region
        # Task ID.
        self.job_id = job_id
        # Task name.
        self.job_name = job_name
        # A list of specific items for the task and their execution progress.
        self.job_progress = job_progress
        # The access method of the source instance, with return values as follows: - **ALIYUN**: Access method is **cloud instance**. - **OTHER**: Access method is **public IP**. - **ECS**: Access method is **ECS self-built database**. - **EXPRESS**: Access method is **dedicated line/VPN gateway/smart gateway**. - **CEN**: Access method is **Cloud Enterprise Network CEN**. - **DG**: Access method is **Database Gateway DG**.
        self.source_endpoint_type = source_endpoint_type
        # ID of the region to which the source network segment belongs.
        self.src_region = src_region
        # Source network segment.
        self.src_region_cidr = src_region_cidr
        # Check result, the return value is: - **Failed**: Failure. - **Success**: Completed.
        self.state = state
        # Total number of items in the project.
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
        # The specific project start time, formatted as <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        self.boot_time = boot_time
        # Whether DTS supports skipping a project after it fails. Return values: * **true**: Yes * **false**: No
        self.can_skip = can_skip
        # The number of currently running tasks.
        self.current = current
        # The DDL operation to be executed.
        self.ddl_sql = ddl_sql
        # Task delay time
        self.delay_seconds = delay_seconds
        # Name of the database to which the migration objects in the target instance belong.
        self.dest_schema = dest_schema
        # This parameter will be deprecated.
        self.diff_row = diff_row
        # Details of the error when a specific project fails.
        self.err_detail = err_detail
        # Error message prompt when a specific project encounters an error.
        self.err_msg = err_msg
        # Task completion time, formatted as yyyy-MM-ddTHH:mm:ssZ (UTC time).
        self.finish_time = finish_time
        # The ID of the record in the metadata database.
        self.id = id
        # Whether to directly ignore this specific item and move to the next one. Return values:
        # - **N**: No. - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # Specific project name.
        self.item = item
        # Task ID.
        self.job_id = job_id
        # Error execution log information.
        self.logs = logs
        # Specific project name.
        self.names = names
        # Project number.
        self.order_num = order_num
        # This parameter will be deprecated.
        self.parent_obj = parent_obj
        # The corresponding remediation method when the pre-check fails.
        self.repair_method = repair_method
        # After this specific item fails, do you set to skip this item. Return values: * **true**: Yes * **false**: No
        self.skip = skip
        # Name of the database to which the migration objects in the source instance belong.
        self.source_schema = source_schema
        # Check result, the return value is: - **Failed**: Failure. - **Success**: Completed.
        self.state = state
        # Progress of sub-projects under a specific project. > If it returns <b>[]</b>, it indicates there are no sub-projects.
        self.sub = sub
        # Name of the target object
        self.target_names = target_names
        # The total number of projects.
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
        # Error record.
        self.err_data = err_data
        # Specific error message.
        self.err_msg = err_msg
        # Type of error.
        self.err_type = err_type
        # The level of the log.
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
        # The specific project start time, formatted as <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        self.boot_time = boot_time
        # Whether to support skipping this sub-item.
        self.can_skip = can_skip
        # The number of currently running subtasks.
        self.current = current
        # The DDL operation to be executed.
        self.ddl_sql = ddl_sql
        # Task delay time
        self.delay_seconds = delay_seconds
        # Name of the database to which the migration objects in the target instance belong.
        self.dest_schema = dest_schema
        # This parameter will be deprecated.
        self.diff_row = diff_row
        # Error details when the project encounters an error.
        self.err_detail = err_detail
        # Specific error message.
        self.err_msg = err_msg
        # The end time of the evaluation task, formatted as <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        self.finish_time = finish_time
        # The ID of this evaluation item in the database.
        self.id = id
        # Whether to directly ignore this specific item and move to the next one. Return values:
        # - **N**: No. - **Y**: Yes.
        self.ignore_flag = ignore_flag
        # Name of the evaluation item
        self.item = item
        # The ID of the evaluation task.
        self.job_id = job_id
        # Sub-assessment item.
        self.logs = logs
        # Name of the evaluation item
        self.names = names
        # The number of the evaluation item.
        self.order_num = order_num
        # This parameter will be deprecated.
        self.parent_obj = parent_obj
        # Remediation method for the evaluation item.
        self.repair_method = repair_method
        # If this evaluation item fails, whether you set to skip this item. Return values: * **true**: Yes * **false**: No
        self.skip = skip
        # Name of the database to which the migration objects in the source instance belong.
        self.source_schema = source_schema
        # The result of the evaluation, with return values being: - **Failed**: Failure. - **Success**: Success.
        self.state = state
        # Progress of sub-projects under a specific project. > If it returns <b>[]</b>, it indicates there are no sub-projects.
        self.sub = sub
        # Name of the target object
        self.target_names = target_names
        # The total number of specific items in the sub-task.
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
        # Error message
        self.err_data = err_data
        # Error message from DTS when a specific project encounters an error.
        self.err_msg = err_msg
        # Error type.
        self.err_type = err_type
        # The level of the log.
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

