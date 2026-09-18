# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListJobSnapshotInfosResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListJobSnapshotInfosResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: Informational - The request has been received and the process is continuing.
        # 
        # - 2xx: Success - The request was successfully received, understood, and accepted.
        # 
        # - 3xx: Redirection - Further action must be taken to complete the request.
        # 
        # - 4xx: Client Error - The request contains bad syntax or cannot be fulfilled.
        # 
        # - 5xx: Server Error - The server failed to fulfill an apparently valid request.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListJobSnapshotInfosResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListJobSnapshotInfosResponseBodyData(DaraModel):
    def __init__(
        self,
        job_info_list: List[main_models.ListJobSnapshotInfosResponseBodyDataJobInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of job snapshots.
        self.job_info_list = job_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_info_list:
            for v1 in self.job_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['jobInfoList'] = []
        if self.job_info_list is not None:
            for k1 in self.job_info_list:
                result['jobInfoList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('jobInfoList') is not None:
            for k1 in m.get('jobInfoList'):
                temp_model = main_models.ListJobSnapshotInfosResponseBodyDataJobInfoList()
                self.job_info_list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListJobSnapshotInfosResponseBodyDataJobInfoList(DaraModel):
    def __init__(
        self,
        cpu_request: int = None,
        cpu_usage: int = None,
        cpu_usage_to_request_ratio: float = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        ext_platform_id: str = None,
        instance_id: str = None,
        job_owner: str = None,
        job_type: str = None,
        max_cpu_pct: float = None,
        max_memory_pct: float = None,
        memory_request: int = None,
        memory_usage: int = None,
        memory_usage_to_request_ratio: float = None,
        min_cpu_pct: float = None,
        min_memory_pct: float = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        signature: str = None,
        snapshot_time: int = None,
        status: str = None,
        submitted_at_time: int = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The amount of CPU cores requested by the job at the snapshot time.
        self.cpu_request = cpu_request
        # The CPU usage of the job at the snapshot time. Unit: cores.
        self.cpu_usage = cpu_usage
        # The CPU fulfillment ratio of the job at the snapshot time. This is calculated by dividing the CPU usage by the CPU request.
        self.cpu_usage_to_request_ratio = cpu_usage_to_request_ratio
        # The upstream node ID.
        self.ext_node_id = ext_node_id
        # The account ID of the task owner.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        self.ext_platform_id = ext_platform_id
        # The job ID.
        self.instance_id = instance_id
        # The job owner.
        self.job_owner = job_owner
        # The job type.
        self.job_type = job_type
        # This parameter is not used.
        self.max_cpu_pct = max_cpu_pct
        # This parameter is not used.
        self.max_memory_pct = max_memory_pct
        # The amount of memory requested by the job at the snapshot time, in MB.
        self.memory_request = memory_request
        # The memory usage of the job at the snapshot time. Unit: MB.
        self.memory_usage = memory_usage
        # The memory fulfillment ratio of the job at the snapshot time. This is calculated by dividing the memory usage by the memory request.
        self.memory_usage_to_request_ratio = memory_usage_to_request_ratio
        # The CPU usage percentage of a subscription job at the snapshot time. This value is calculated by dividing the CPU usage by the sum of the reserved CPU guarantee and the elastic reserved CPU. This parameter is not available for pay-as-you-go jobs.
        self.min_cpu_pct = min_cpu_pct
        # The memory usage percentage of a subscription job at the observation time. This value is calculated by dividing the memory usage by the sum of the reserved memory guarantee and the elastic reserved memory. This parameter is not available for pay-as-you-go jobs.
        self.min_memory_pct = min_memory_pct
        # The job priority.
        self.priority = priority
        # The project name.
        self.project = project
        # The nickname of the computing quota that the job uses.
        self.quota_nickname = quota_nickname
        # The quota type.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The time when the job started running.
        # 
        # > The time when the job acquired its first computing resource.
        self.running_at_time = running_at_time
        # The runtime duration, in seconds. This is the duration from when the job started running to the snapshot time. If the job has not started, this parameter is empty.
        self.running_time = running_time
        # The signature of the SQL job.
        self.signature = signature
        # The snapshot time.
        self.snapshot_time = snapshot_time
        # The job status.
        # 
        # > The status of a snapshot job can only be \\`running\\`.
        self.status = status
        # The time when the job was submitted.
        self.submitted_at_time = submitted_at_time
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total duration, in seconds. This is the duration from when the job was submitted to the snapshot time.
        self.total_time = total_time
        # The waiting duration, in seconds. This is the duration from when the job was submitted to when it started running. If the job has not started, this is the duration from the submission time to the snapshot time.
        self.waiting_time = waiting_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_request is not None:
            result['cpuRequest'] = self.cpu_request

        if self.cpu_usage is not None:
            result['cpuUsage'] = self.cpu_usage

        if self.cpu_usage_to_request_ratio is not None:
            result['cpuUsageToRequestRatio'] = self.cpu_usage_to_request_ratio

        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id

        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty

        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from

        if self.ext_platform_id is not None:
            result['extPlatformId'] = self.ext_platform_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.job_type is not None:
            result['jobType'] = self.job_type

        if self.max_cpu_pct is not None:
            result['maxCpuPct'] = self.max_cpu_pct

        if self.max_memory_pct is not None:
            result['maxMemoryPct'] = self.max_memory_pct

        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request

        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage

        if self.memory_usage_to_request_ratio is not None:
            result['memoryUsageToRequestRatio'] = self.memory_usage_to_request_ratio

        if self.min_cpu_pct is not None:
            result['minCpuPct'] = self.min_cpu_pct

        if self.min_memory_pct is not None:
            result['minMemoryPct'] = self.min_memory_pct

        if self.priority is not None:
            result['priority'] = self.priority

        if self.project is not None:
            result['project'] = self.project

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        if self.quota_type is not None:
            result['quotaType'] = self.quota_type

        if self.region is not None:
            result['region'] = self.region

        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time

        if self.running_time is not None:
            result['runningTime'] = self.running_time

        if self.signature is not None:
            result['signature'] = self.signature

        if self.snapshot_time is not None:
            result['snapshotTime'] = self.snapshot_time

        if self.status is not None:
            result['status'] = self.status

        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total_time is not None:
            result['totalTime'] = self.total_time

        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuRequest') is not None:
            self.cpu_request = m.get('cpuRequest')

        if m.get('cpuUsage') is not None:
            self.cpu_usage = m.get('cpuUsage')

        if m.get('cpuUsageToRequestRatio') is not None:
            self.cpu_usage_to_request_ratio = m.get('cpuUsageToRequestRatio')

        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')

        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')

        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')

        if m.get('extPlatformId') is not None:
            self.ext_platform_id = m.get('extPlatformId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

        if m.get('maxCpuPct') is not None:
            self.max_cpu_pct = m.get('maxCpuPct')

        if m.get('maxMemoryPct') is not None:
            self.max_memory_pct = m.get('maxMemoryPct')

        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')

        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')

        if m.get('memoryUsageToRequestRatio') is not None:
            self.memory_usage_to_request_ratio = m.get('memoryUsageToRequestRatio')

        if m.get('minCpuPct') is not None:
            self.min_cpu_pct = m.get('minCpuPct')

        if m.get('minMemoryPct') is not None:
            self.min_memory_pct = m.get('minMemoryPct')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        if m.get('quotaType') is not None:
            self.quota_type = m.get('quotaType')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')

        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('snapshotTime') is not None:
            self.snapshot_time = m.get('snapshotTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')

        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')

        return self

