# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetOnlineDDLProgressResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        online_ddltask_detail: main_models.GetOnlineDDLProgressResponseBodyOnlineDDLTaskDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The details of the task.
        self.online_ddltask_detail = online_ddltask_detail
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.online_ddltask_detail:
            self.online_ddltask_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.online_ddltask_detail is not None:
            result['OnlineDDLTaskDetail'] = self.online_ddltask_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OnlineDDLTaskDetail') is not None:
            temp_model = main_models.GetOnlineDDLProgressResponseBodyOnlineDDLTaskDetail()
            self.online_ddltask_detail = temp_model.from_map(m.get('OnlineDDLTaskDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOnlineDDLProgressResponseBodyOnlineDDLTaskDetail(DaraModel):
    def __init__(
        self,
        clean_strategy: str = None,
        copy_chunk_mode: str = None,
        copy_chunk_size: int = None,
        copy_count: int = None,
        copy_total: int = None,
        cutover_fail_retry_times: int = None,
        cutover_lock_time_seconds: int = None,
        cutover_window_end_time: str = None,
        cutover_window_start_time: str = None,
        delay_seconds: int = None,
        job_status: str = None,
        progress_ratio: str = None,
        status_desc: str = None,
    ):
        # The cleanup policy of the original table after the cut-over. Valid values:
        # 
        # *   **DROP**: Invalid original tables are deleted.
        # *   **MOVE**: Invalid original tables are moved to the test database. You can delete the tables manually.
        # *   **NOTHING**: Invalid original tables are retained in the original database. You can delete the tables manually.
        self.clean_strategy = clean_strategy
        # The policy of full replication. Valid values:
        # 
        # *   **AUTO**: DMS dynamically adjusts the chunk size based on the performance of the database. Tables are locked for less than 1.5 seconds during a single replication operation.
        # *   **RUNNING**: DMS uses the specified value of the CopyChunkSize parameter. The valid value of the CopyChunkSize parameter ranges from 1 to 60000. If you set this parameter to RUNNING, you must specify the CopyChunkSize parameter.
        self.copy_chunk_mode = copy_chunk_mode
        # The size of each chunk that is used to replicate data. This parameter is used to specify the size of each chunk. A larger chunk size increases the replication efficiency and decreases the business performance.
        # 
        # > During full replication, the original table is divided into N small chunks and each chunk is replicated to the temporary table one by one. By default, DMS dynamically adjusts the size of each chunk.
        self.copy_chunk_size = copy_chunk_size
        # The actual amount of data replicated from the original table in the lock-free change operation.
        self.copy_count = copy_count
        # The estimated total number of rows of the data. The value is obtained from the statistical data in the information_schema database. In most cases, the estimated total number of rows is smaller than the actual number of rows in a table.
        self.copy_total = copy_total
        # The number of retries when the cut-over fails.
        self.cutover_fail_retry_times = cutover_fail_retry_times
        # The maximum period of time that a table can be locked during cut-over. Unit: seconds.
        self.cutover_lock_time_seconds = cutover_lock_time_seconds
        # The end of the time window of the cut-over operation. This value is at least 30 minutes later than the CutoverWindowStartTime parameter. Default value: 23:59:59
        self.cutover_window_end_time = cutover_window_end_time
        # The beginning of the time window of the cut-over operation. Default value: 00:00:00. This parameter controls the time window of the cut-over. Cut-over can be performed only when the cut-over conditions are met and the time is within the specified time window. If the time is not within the time window, the cut-over operation is not performed until the time reaches the beginning of the time window.
        self.cutover_window_start_time = cutover_window_start_time
        # The replay latency of DMS. Unit: seconds. The replay latency is the period of time that is taken to replay the binary logs of the table to the temporary table. The latency does not indicate the data migration latency between a primary database and a secondary database.
        self.delay_seconds = delay_seconds
        # The state of the task. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **SUCCESS**: The task is complete.
        # *   **RUNNING**: The task is being executed.
        # *   **WAITING_CUTOVER**: The task is waiting for cut-over.
        # *   **RESTARTING**: The task is restarting.
        # *   **PAUSE**: The task is suspended.
        # *   **UNSUPPORTED**: The task is not supported.
        # *   **CANCELED**: The task is canceled.
        # *   **FAIL**: The task failed.
        # *   **INTERRUPT**: The task is interrupted.
        self.job_status = job_status
        # The estimated execution progress. The actual progress is subject to the task status.
        self.progress_ratio = progress_ratio
        # The description of the task status.
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_strategy is not None:
            result['CleanStrategy'] = self.clean_strategy

        if self.copy_chunk_mode is not None:
            result['CopyChunkMode'] = self.copy_chunk_mode

        if self.copy_chunk_size is not None:
            result['CopyChunkSize'] = self.copy_chunk_size

        if self.copy_count is not None:
            result['CopyCount'] = self.copy_count

        if self.copy_total is not None:
            result['CopyTotal'] = self.copy_total

        if self.cutover_fail_retry_times is not None:
            result['CutoverFailRetryTimes'] = self.cutover_fail_retry_times

        if self.cutover_lock_time_seconds is not None:
            result['CutoverLockTimeSeconds'] = self.cutover_lock_time_seconds

        if self.cutover_window_end_time is not None:
            result['CutoverWindowEndTime'] = self.cutover_window_end_time

        if self.cutover_window_start_time is not None:
            result['CutoverWindowStartTime'] = self.cutover_window_start_time

        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.progress_ratio is not None:
            result['ProgressRatio'] = self.progress_ratio

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanStrategy') is not None:
            self.clean_strategy = m.get('CleanStrategy')

        if m.get('CopyChunkMode') is not None:
            self.copy_chunk_mode = m.get('CopyChunkMode')

        if m.get('CopyChunkSize') is not None:
            self.copy_chunk_size = m.get('CopyChunkSize')

        if m.get('CopyCount') is not None:
            self.copy_count = m.get('CopyCount')

        if m.get('CopyTotal') is not None:
            self.copy_total = m.get('CopyTotal')

        if m.get('CutoverFailRetryTimes') is not None:
            self.cutover_fail_retry_times = m.get('CutoverFailRetryTimes')

        if m.get('CutoverLockTimeSeconds') is not None:
            self.cutover_lock_time_seconds = m.get('CutoverLockTimeSeconds')

        if m.get('CutoverWindowEndTime') is not None:
            self.cutover_window_end_time = m.get('CutoverWindowEndTime')

        if m.get('CutoverWindowStartTime') is not None:
            self.cutover_window_start_time = m.get('CutoverWindowStartTime')

        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('ProgressRatio') is not None:
            self.progress_ratio = m.get('ProgressRatio')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

