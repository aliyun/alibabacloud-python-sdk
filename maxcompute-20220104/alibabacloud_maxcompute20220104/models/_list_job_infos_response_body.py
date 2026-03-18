# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListJobInfosResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListJobInfosResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Indicates whether the business logic was successful. A value other than 200 indicates a failure.
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

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListJobInfosResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListJobInfosResponseBodyData(DaraModel):
    def __init__(
        self,
        job_info_list: List[main_models.ListJobInfosResponseBodyDataJobInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of job information.
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
                temp_model = main_models.ListJobInfosResponseBodyDataJobInfoList()
                self.job_info_list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListJobInfosResponseBodyDataJobInfoList(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        cu_snapshot: float = None,
        cu_usage: int = None,
        end_at_time: int = None,
        ext_node_id: str = None,
        ext_node_name: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        ext_platform_id: str = None,
        input_bytes: float = None,
        instance_id: str = None,
        job_owner: str = None,
        job_type: str = None,
        memory_snapshot: float = None,
        memory_usage: int = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        scene_results: List[main_models.ListJobInfosResponseBodyDataJobInfoListSceneResults] = None,
        signature: str = None,
        status: str = None,
        status_snapshot: str = None,
        submitted_at_time: int = None,
        tags: str = None,
        task_name: str = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The cluster ID.
        self.cluster = cluster
        # The proportion of CUs in the job snapshot.
        self.cu_snapshot = cu_snapshot
        # The total CUs used.
        self.cu_usage = cu_usage
        # The time when the job finished.
        self.end_at_time = end_at_time
        # The ID of the DataWorks node.
        self.ext_node_id = ext_node_id
        self.ext_node_name = ext_node_name
        # The person in charge of the execution.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        self.ext_platform_id = ext_platform_id
        # The amount of data scanned by the job. Unit: bytes.
        self.input_bytes = input_bytes
        # The instance ID.
        self.instance_id = instance_id
        # The account that submitted the job.
        self.job_owner = job_owner
        # The job type.
        self.job_type = job_type
        # The proportion of memory in the job snapshot.
        self.memory_snapshot = memory_snapshot
        # The total memory used.
        self.memory_usage = memory_usage
        # The priority.
        self.priority = priority
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that the job uses.
        self.quota_nickname = quota_nickname
        # The quota type.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The time when the job started to run.
        self.running_at_time = running_at_time
        # The runtime.
        self.running_time = running_time
        # The smart diagnosis results.
        self.scene_results = scene_results
        # The SQL signature.
        self.signature = signature
        # The status.
        self.status = status
        # The status of the job snapshot.
        self.status_snapshot = status_snapshot
        # The time when the job was submitted.
        self.submitted_at_time = submitted_at_time
        # The tags.
        self.tags = tags
        self.task_name = task_name
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total runtime.
        self.total_time = total_time
        # The waiting time.
        self.waiting_time = waiting_time

    def validate(self):
        if self.scene_results:
            for v1 in self.scene_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot

        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage

        if self.end_at_time is not None:
            result['endAtTime'] = self.end_at_time

        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id

        if self.ext_node_name is not None:
            result['extNodeName'] = self.ext_node_name

        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty

        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from

        if self.ext_platform_id is not None:
            result['extPlatformId'] = self.ext_platform_id

        if self.input_bytes is not None:
            result['inputBytes'] = self.input_bytes

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.job_type is not None:
            result['jobType'] = self.job_type

        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot

        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage

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

        result['sceneResults'] = []
        if self.scene_results is not None:
            for k1 in self.scene_results:
                result['sceneResults'].append(k1.to_map() if k1 else None)

        if self.signature is not None:
            result['signature'] = self.signature

        if self.status is not None:
            result['status'] = self.status

        if self.status_snapshot is not None:
            result['statusSnapshot'] = self.status_snapshot

        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time

        if self.tags is not None:
            result['tags'] = self.tags

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total_time is not None:
            result['totalTime'] = self.total_time

        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')

        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')

        if m.get('endAtTime') is not None:
            self.end_at_time = m.get('endAtTime')

        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')

        if m.get('extNodeName') is not None:
            self.ext_node_name = m.get('extNodeName')

        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')

        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')

        if m.get('extPlatformId') is not None:
            self.ext_platform_id = m.get('extPlatformId')

        if m.get('inputBytes') is not None:
            self.input_bytes = m.get('inputBytes')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')

        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')

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

        self.scene_results = []
        if m.get('sceneResults') is not None:
            for k1 in m.get('sceneResults'):
                temp_model = main_models.ListJobInfosResponseBodyDataJobInfoListSceneResults()
                self.scene_results.append(temp_model.from_map(k1))

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusSnapshot') is not None:
            self.status_snapshot = m.get('statusSnapshot')

        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')

        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')

        return self

class ListJobInfosResponseBodyDataJobInfoListSceneResults(DaraModel):
    def __init__(
        self,
        description: str = None,
        params: Dict[str, str] = None,
        scene: str = None,
        scene_tag: str = None,
        summary: str = None,
        type: str = None,
    ):
        # The details of the smart diagnosis result.
        self.description = description
        # Information about the nodes that have data skew or data bloat. This parameter is returned only when the diagnosis scenario is data skew or data bloat.
        self.params = params
        # The scenario of the smart diagnosis result.
        self.scene = scene
        # The tag of the smart diagnosis result.
        self.scene_tag = scene_tag
        # A summary of the smart diagnosis result.
        self.summary = summary
        # The type of the smart diagnosis result.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.params is not None:
            result['params'] = self.params

        if self.scene is not None:
            result['scene'] = self.scene

        if self.scene_tag is not None:
            result['sceneTag'] = self.scene_tag

        if self.summary is not None:
            result['summary'] = self.summary

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sceneTag') is not None:
            self.scene_tag = m.get('sceneTag')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

