# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetJobInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
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
            temp_model = main_models.GetJobInfoResponseBodyData()
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

class GetJobInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        cu_usage: int = None,
        end_at_time: int = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        input_bytes: float = None,
        instance_id: str = None,
        job_owner: str = None,
        job_sub_status_list: List[main_models.GetJobInfoResponseBodyDataJobSubStatusList] = None,
        job_type: str = None,
        memory_usage: int = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        scene_results: List[main_models.GetJobInfoResponseBodyDataSceneResults] = None,
        signature: str = None,
        status: str = None,
        submitted_at_time: int = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        self.cu_usage = cu_usage
        self.end_at_time = end_at_time
        self.ext_node_id = ext_node_id
        self.ext_node_on_duty = ext_node_on_duty
        self.ext_plant_from = ext_plant_from
        self.input_bytes = input_bytes
        self.instance_id = instance_id
        self.job_owner = job_owner
        self.job_sub_status_list = job_sub_status_list
        self.job_type = job_type
        self.memory_usage = memory_usage
        self.priority = priority
        self.project = project
        self.quota_nickname = quota_nickname
        self.quota_type = quota_type
        self.region = region
        self.running_at_time = running_at_time
        self.running_time = running_time
        self.scene_results = scene_results
        self.signature = signature
        self.status = status
        self.submitted_at_time = submitted_at_time
        self.tenant_id = tenant_id
        self.total_time = total_time
        self.waiting_time = waiting_time

    def validate(self):
        if self.job_sub_status_list:
            for v1 in self.job_sub_status_list:
                 if v1:
                    v1.validate()
        if self.scene_results:
            for v1 in self.scene_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage

        if self.end_at_time is not None:
            result['endAtTime'] = self.end_at_time

        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id

        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty

        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from

        if self.input_bytes is not None:
            result['inputBytes'] = self.input_bytes

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        result['jobSubStatusList'] = []
        if self.job_sub_status_list is not None:
            for k1 in self.job_sub_status_list:
                result['jobSubStatusList'].append(k1.to_map() if k1 else None)

        if self.job_type is not None:
            result['jobType'] = self.job_type

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
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')

        if m.get('endAtTime') is not None:
            self.end_at_time = m.get('endAtTime')

        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')

        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')

        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')

        if m.get('inputBytes') is not None:
            self.input_bytes = m.get('inputBytes')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        self.job_sub_status_list = []
        if m.get('jobSubStatusList') is not None:
            for k1 in m.get('jobSubStatusList'):
                temp_model = main_models.GetJobInfoResponseBodyDataJobSubStatusList()
                self.job_sub_status_list.append(temp_model.from_map(k1))

        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

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
                temp_model = main_models.GetJobInfoResponseBodyDataSceneResults()
                self.scene_results.append(temp_model.from_map(k1))

        if m.get('signature') is not None:
            self.signature = m.get('signature')

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

class GetJobInfoResponseBodyDataSceneResults(DaraModel):
    def __init__(
        self,
        description: str = None,
        params: Dict[str, str] = None,
        scene: str = None,
        scene_tag: str = None,
        summary: str = None,
        type: str = None,
    ):
        self.description = description
        self.params = params
        self.scene = scene
        self.scene_tag = scene_tag
        self.summary = summary
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

class GetJobInfoResponseBodyDataJobSubStatusList(DaraModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        start_time: str = None,
    ):
        self.code = code
        self.description = description
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

