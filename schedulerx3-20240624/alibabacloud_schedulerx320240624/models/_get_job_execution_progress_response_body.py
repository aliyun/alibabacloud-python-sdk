# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetJobExecutionProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetJobExecutionProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetJobExecutionProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobExecutionProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        job_description: str = None,
        root_progress: main_models.GetJobExecutionProgressResponseBodyDataRootProgress = None,
        sharding_progress: List[main_models.GetJobExecutionProgressResponseBodyDataShardingProgress] = None,
        start_time: str = None,
        task_progress: List[main_models.GetJobExecutionProgressResponseBodyDataTaskProgress] = None,
        total_progress: main_models.GetJobExecutionProgressResponseBodyDataTotalProgress = None,
        worker_progress: List[main_models.GetJobExecutionProgressResponseBodyDataWorkerProgress] = None,
    ):
        self.end_time = end_time
        self.job_description = job_description
        self.root_progress = root_progress
        self.sharding_progress = sharding_progress
        self.start_time = start_time
        self.task_progress = task_progress
        self.total_progress = total_progress
        self.worker_progress = worker_progress

    def validate(self):
        if self.root_progress:
            self.root_progress.validate()
        if self.sharding_progress:
            for v1 in self.sharding_progress:
                 if v1:
                    v1.validate()
        if self.task_progress:
            for v1 in self.task_progress:
                 if v1:
                    v1.validate()
        if self.total_progress:
            self.total_progress.validate()
        if self.worker_progress:
            for v1 in self.worker_progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.root_progress is not None:
            result['RootProgress'] = self.root_progress.to_map()

        result['ShardingProgress'] = []
        if self.sharding_progress is not None:
            for k1 in self.sharding_progress:
                result['ShardingProgress'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['TaskProgress'] = []
        if self.task_progress is not None:
            for k1 in self.task_progress:
                result['TaskProgress'].append(k1.to_map() if k1 else None)

        if self.total_progress is not None:
            result['TotalProgress'] = self.total_progress.to_map()

        result['WorkerProgress'] = []
        if self.worker_progress is not None:
            for k1 in self.worker_progress:
                result['WorkerProgress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('RootProgress') is not None:
            temp_model = main_models.GetJobExecutionProgressResponseBodyDataRootProgress()
            self.root_progress = temp_model.from_map(m.get('RootProgress'))

        self.sharding_progress = []
        if m.get('ShardingProgress') is not None:
            for k1 in m.get('ShardingProgress'):
                temp_model = main_models.GetJobExecutionProgressResponseBodyDataShardingProgress()
                self.sharding_progress.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.task_progress = []
        if m.get('TaskProgress') is not None:
            for k1 in m.get('TaskProgress'):
                temp_model = main_models.GetJobExecutionProgressResponseBodyDataTaskProgress()
                self.task_progress.append(temp_model.from_map(k1))

        if m.get('TotalProgress') is not None:
            temp_model = main_models.GetJobExecutionProgressResponseBodyDataTotalProgress()
            self.total_progress = temp_model.from_map(m.get('TotalProgress'))

        self.worker_progress = []
        if m.get('WorkerProgress') is not None:
            for k1 in m.get('WorkerProgress'):
                temp_model = main_models.GetJobExecutionProgressResponseBodyDataWorkerProgress()
                self.worker_progress.append(temp_model.from_map(k1))

        return self

class GetJobExecutionProgressResponseBodyDataWorkerProgress(DaraModel):
    def __init__(
        self,
        failed: int = None,
        pulled: int = None,
        queue: int = None,
        running: int = None,
        success: int = None,
        total: int = None,
        trace_id: str = None,
        worker_addr: str = None,
    ):
        self.failed = failed
        self.pulled = pulled
        self.queue = queue
        self.running = running
        self.success = success
        self.total = total
        self.trace_id = trace_id
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.pulled is not None:
            result['Pulled'] = self.pulled

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.running is not None:
            result['Running'] = self.running

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Pulled') is not None:
            self.pulled = m.get('Pulled')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')

        return self

class GetJobExecutionProgressResponseBodyDataTotalProgress(DaraModel):
    def __init__(
        self,
        finished: int = None,
        total: int = None,
    ):
        self.finished = finished
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finished is not None:
            result['Finished'] = self.finished

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetJobExecutionProgressResponseBodyDataTaskProgress(DaraModel):
    def __init__(
        self,
        failed: int = None,
        name: str = None,
        pulled: int = None,
        queue: int = None,
        running: int = None,
        success: int = None,
        total: int = None,
    ):
        self.failed = failed
        self.name = name
        self.pulled = pulled
        self.queue = queue
        self.running = running
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.name is not None:
            result['Name'] = self.name

        if self.pulled is not None:
            result['Pulled'] = self.pulled

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.running is not None:
            result['Running'] = self.running

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pulled') is not None:
            self.pulled = m.get('Pulled')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetJobExecutionProgressResponseBodyDataShardingProgress(DaraModel):
    def __init__(
        self,
        id: int = None,
        job_execution_id: str = None,
        result: str = None,
        status: int = None,
        status_type: main_models.GetJobExecutionProgressResponseBodyDataShardingProgressStatusType = None,
        worker_addr: str = None,
    ):
        # id
        self.id = id
        self.job_execution_id = job_execution_id
        self.result = result
        self.status = status
        self.status_type = status_type
        self.worker_addr = worker_addr

    def validate(self):
        if self.status_type:
            self.status_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.result is not None:
            result['Result'] = self.result

        if self.status is not None:
            result['Status'] = self.status

        if self.status_type is not None:
            result['StatusType'] = self.status_type.to_map()

        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusType') is not None:
            temp_model = main_models.GetJobExecutionProgressResponseBodyDataShardingProgressStatusType()
            self.status_type = temp_model.from_map(m.get('StatusType'))

        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')

        return self

class GetJobExecutionProgressResponseBodyDataShardingProgressStatusType(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        tips: Dict[str, str] = None,
    ):
        self.code = code
        self.name = name
        # -
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.tips is not None:
            result['Tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        return self

class GetJobExecutionProgressResponseBodyDataRootProgress(DaraModel):
    def __init__(
        self,
        finished: int = None,
        total: int = None,
    ):
        self.finished = finished
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finished is not None:
            result['Finished'] = self.finished

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

