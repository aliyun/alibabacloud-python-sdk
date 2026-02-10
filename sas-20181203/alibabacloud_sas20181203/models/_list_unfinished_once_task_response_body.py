# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListUnfinishedOnceTaskResponseBody(DaraModel):
    def __init__(
        self,
        once_tasks: List[main_models.ListUnfinishedOnceTaskResponseBodyOnceTasks] = None,
        request_id: str = None,
    ):
        # The details of the tasks.
        self.once_tasks = once_tasks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.once_tasks:
            for v1 in self.once_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnceTasks'] = []
        if self.once_tasks is not None:
            for k1 in self.once_tasks:
                result['OnceTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.once_tasks = []
        if m.get('OnceTasks') is not None:
            for k1 in m.get('OnceTasks'):
                temp_model = main_models.ListUnfinishedOnceTaskResponseBodyOnceTasks()
                self.once_tasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUnfinishedOnceTaskResponseBodyOnceTasks(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        finish: int = None,
        finish_count: int = None,
        progress: int = None,
        real_run_time: int = None,
        result_info: str = None,
        start_time: int = None,
        status: int = None,
        status_text: str = None,
        target: str = None,
        target_type: str = None,
        task_id: str = None,
        task_image_info: main_models.ListUnfinishedOnceTaskResponseBodyOnceTasksTaskImageInfo = None,
        task_name: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        # The time when the task ends.
        self.end_time = end_time
        # Indicates whether the task is complete. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.finish = finish
        # The number of assets on which the task is complete.
        self.finish_count = finish_count
        # The progress percentage of the task.
        self.progress = progress
        # The execution duration of the task.
        self.real_run_time = real_run_time
        # The execution result of the task.
        self.result_info = result_info
        # The time when the task is started.
        self.start_time = start_time
        # The status.
        self.status = status
        # The status of the task. Valid values:
        # 
        # *   **INIT**: The task is not started.
        # *   **START**: The task is started.
        # *   **SUCCESS**: The task is complete.
        # *   **TIMEOUT**: The task timed out.
        self.status_text = status_text
        # The objective of the task.
        self.target = target
        # The type of the assets that are scanned. Valid values:
        # 
        # *   **IMAGE_REPO**: image repository
        # *   **IMAGE**: image
        self.target_type = target_type
        # The ID of the task.
        self.task_id = task_id
        # The information about the image scan task.
        self.task_image_info = task_image_info
        # The name of the task.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_image_info:
            self.task_image_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.real_run_time is not None:
            result['RealRunTime'] = self.real_run_time

        if self.result_info is not None:
            result['ResultInfo'] = self.result_info

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_text is not None:
            result['StatusText'] = self.status_text

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_image_info is not None:
            result['TaskImageInfo'] = self.task_image_info.to_map()

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RealRunTime') is not None:
            self.real_run_time = m.get('RealRunTime')

        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskImageInfo') is not None:
            temp_model = main_models.ListUnfinishedOnceTaskResponseBodyOnceTasksTaskImageInfo()
            self.task_image_info = temp_model.from_map(m.get('TaskImageInfo'))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUnfinishedOnceTaskResponseBodyOnceTasksTaskImageInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        digest: str = None,
        image: str = None,
        node_instance_id: str = None,
        node_ip: str = None,
        node_name: str = None,
        pod: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_region_id: str = None,
        tag: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The image digest.
        self.digest = digest
        # The container image.
        self.image = image
        # The instance ID of the node.
        self.node_instance_id = node_instance_id
        # The IP address of the node.
        self.node_ip = node_ip
        # The name of the node.
        self.node_name = node_name
        # The pod of the image.
        self.pod = pod
        # The region ID of the server image.
        self.region_id = region_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The region ID of the image repository.
        self.repo_region_id = repo_region_id
        # The image tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.image is not None:
            result['Image'] = self.image

        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id

        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')

        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

