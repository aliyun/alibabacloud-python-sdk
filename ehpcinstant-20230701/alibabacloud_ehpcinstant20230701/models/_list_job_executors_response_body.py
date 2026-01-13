# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListJobExecutorsResponseBody(DaraModel):
    def __init__(
        self,
        executor_status: main_models.ListJobExecutorsResponseBodyExecutorStatus = None,
        executors: List[main_models.ListJobExecutorsResponseBodyExecutors] = None,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_name: str = None,
        total_count: str = None,
    ):
        # Executor status statistics.
        self.executor_status = executor_status
        # The executor list.
        self.executors = executors
        # The job ID.
        self.job_id = job_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The job name.
        self.task_name = task_name
        # The total number of list entries.
        self.total_count = total_count

    def validate(self):
        if self.executor_status:
            self.executor_status.validate()
        if self.executors:
            for v1 in self.executors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_status is not None:
            result['ExecutorStatus'] = self.executor_status.to_map()

        result['Executors'] = []
        if self.executors is not None:
            for k1 in self.executors:
                result['Executors'].append(k1.to_map() if k1 else None)

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorStatus') is not None:
            temp_model = main_models.ListJobExecutorsResponseBodyExecutorStatus()
            self.executor_status = temp_model.from_map(m.get('ExecutorStatus'))

        self.executors = []
        if m.get('Executors') is not None:
            for k1 in m.get('Executors'):
                temp_model = main_models.ListJobExecutorsResponseBodyExecutors()
                self.executors.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobExecutorsResponseBodyExecutors(DaraModel):
    def __init__(
        self,
        allocation_spec: str = None,
        array_index: int = None,
        block_duration: int = None,
        create_time: str = None,
        end_time: str = None,
        executor_id: str = None,
        expiration_time: str = None,
        external_ip_address: List[str] = None,
        host_name: List[str] = None,
        ip_address: List[str] = None,
        preemptible: bool = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[main_models.ListJobExecutorsResponseBodyExecutorsTags] = None,
    ):
        self.allocation_spec = allocation_spec
        # The executor index number.
        self.array_index = array_index
        self.block_duration = block_duration
        # The time when the storage resource was created.
        self.create_time = create_time
        # The end time.
        self.end_time = end_time
        # The executor ID. The format is JobId-TaskName-ArrayIndex.
        self.executor_id = executor_id
        self.expiration_time = expiration_time
        # The list of public IP addresses of the nodes.
        self.external_ip_address = external_ip_address
        # An array of node hostnames.
        self.host_name = host_name
        # The list of node IP addresses.
        self.ip_address = ip_address
        self.preemptible = preemptible
        # The create time.
        self.start_time = start_time
        # The status of the executor. Valid values:
        # 
        # *   Pending
        # *   Initing
        # *   Succeed
        # *   Failed
        # *   Running
        # *   Unknown
        # *   Exception
        # *   Retrying
        # *   Expired
        # *   Deleted
        self.status = status
        # The description of the status reason.
        self.status_reason = status_reason
        # The list of executor tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec

        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index

        if self.block_duration is not None:
            result['BlockDuration'] = self.block_duration

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor_id is not None:
            result['ExecutorId'] = self.executor_id

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.external_ip_address is not None:
            result['ExternalIpAddress'] = self.external_ip_address

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.preemptible is not None:
            result['Preemptible'] = self.preemptible

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('BlockDuration') is not None:
            self.block_duration = m.get('BlockDuration')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecutorId') is not None:
            self.executor_id = m.get('ExecutorId')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('ExternalIpAddress') is not None:
            self.external_ip_address = m.get('ExternalIpAddress')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Preemptible') is not None:
            self.preemptible = m.get('Preemptible')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListJobExecutorsResponseBodyExecutorsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListJobExecutorsResponseBodyExecutorsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the executor tag.
        self.tag_key = tag_key
        # The value of the executor tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListJobExecutorsResponseBodyExecutorStatus(DaraModel):
    def __init__(
        self,
        deleted: int = None,
        exception: int = None,
        failed: int = None,
        initing: int = None,
        pending: int = None,
        restarting: int = None,
        running: int = None,
        succeeded: int = None,
        suspended: int = None,
    ):
        # The number of executers in the Deleted state.
        self.deleted = deleted
        # The number of executers in the abnormal state.
        self.exception = exception
        # The number of executers in the Failed state.
        self.failed = failed
        # The number of executers in the initialized state.
        self.initing = initing
        # The number of executers in the queued state.
        self.pending = pending
        self.restarting = restarting
        # The number of executers in the running state.
        self.running = running
        # The number of executoresin the Successful state.
        self.succeeded = succeeded
        self.suspended = suspended

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.exception is not None:
            result['Exception'] = self.exception

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.initing is not None:
            result['Initing'] = self.initing

        if self.pending is not None:
            result['Pending'] = self.pending

        if self.restarting is not None:
            result['Restarting'] = self.restarting

        if self.running is not None:
            result['Running'] = self.running

        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded

        if self.suspended is not None:
            result['Suspended'] = self.suspended

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Exception') is not None:
            self.exception = m.get('Exception')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Initing') is not None:
            self.initing = m.get('Initing')

        if m.get('Pending') is not None:
            self.pending = m.get('Pending')

        if m.get('Restarting') is not None:
            self.restarting = m.get('Restarting')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')

        if m.get('Suspended') is not None:
            self.suspended = m.get('Suspended')

        return self

