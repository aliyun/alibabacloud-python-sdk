# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetRepoSyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        cross_user: bool = None,
        image_from: main_models.GetRepoSyncTaskResponseBodyImageFrom = None,
        image_to: main_models.GetRepoSyncTaskResponseBodyImageTo = None,
        is_success: bool = None,
        layer_tasks: List[main_models.GetRepoSyncTaskResponseBodyLayerTasks] = None,
        progress: int = None,
        request_id: str = None,
        sync_batch_task_id: str = None,
        sync_rule_id: str = None,
        sync_task_id: str = None,
        sync_trans_accelerate: bool = None,
        synced_size: int = None,
        task_issue: str = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the synchronization task is performed across Alibaba Cloud accounts.
        self.cross_user = cross_user
        # The source address of the image.
        self.image_from = image_from
        # The destination address of the image.
        self.image_to = image_to
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The synchronization tasks for the image layer.
        self.layer_tasks = layer_tasks
        # The synchronization progress. Valid values:
        # 
        # *   `0`: The synchronization starts or failed.
        # *   `1`: The synchronization is successful.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The ID of the synchronization task in which multiple images are synchronized at a time.
        self.sync_batch_task_id = sync_batch_task_id
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id
        # Indicates whether transfer acceleration is enabled in the synchronization process.
        self.sync_trans_accelerate = sync_trans_accelerate
        # The size of the image layer that is synchronized. Unit: bytes.
        self.synced_size = synced_size
        # The error message that is returned if the synchronization task fails.
        # 
        # >  The system uses this parameter to return an error message if the synchronization task fails.
        # 
        # Valid values:
        # 
        # *   OSS_POLICY_UNAUTHORIZED: Container Registry is not granted permissions to use Object Storage Service (OSS).
        # *   TAG_CONFLICT: The destination repository contains an image that has the same tag as the source image, and image tag immutability is enabled for the destination repository.
        # *   UNSUPPORTED_FORMAT: The manifest and config formats of the image to be synchronized are not supported.
        # *   INTERNAL_ERROR: The synchronization task failed due to internal issues on the server.
        # *   NETWORK_ERROR: The synchronization task failed due to unstable network connection.
        # *   DATA_LENGTH_EXCEEDED: The manifest or config of the image is oversized.
        self.task_issue = task_issue
        # The status of the task. Valid values:
        self.task_status = task_status
        # The policy that is used to trigger the synchronization task.
        self.task_trigger = task_trigger

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()
        if self.layer_tasks:
            for v1 in self.layer_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user

        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()

        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        result['LayerTasks'] = []
        if self.layer_tasks is not None:
            for k1 in self.layer_tasks:
                result['LayerTasks'].append(k1.to_map() if k1 else None)

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id

        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id

        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id

        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate

        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size

        if self.task_issue is not None:
            result['TaskIssue'] = self.task_issue

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')

        if m.get('ImageFrom') is not None:
            temp_model = main_models.GetRepoSyncTaskResponseBodyImageFrom()
            self.image_from = temp_model.from_map(m.get('ImageFrom'))

        if m.get('ImageTo') is not None:
            temp_model = main_models.GetRepoSyncTaskResponseBodyImageTo()
            self.image_to = temp_model.from_map(m.get('ImageTo'))

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        self.layer_tasks = []
        if m.get('LayerTasks') is not None:
            for k1 in m.get('LayerTasks'):
                temp_model = main_models.GetRepoSyncTaskResponseBodyLayerTasks()
                self.layer_tasks.append(temp_model.from_map(k1))

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')

        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')

        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')

        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')

        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')

        if m.get('TaskIssue') is not None:
            self.task_issue = m.get('TaskIssue')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')

        return self

class GetRepoSyncTaskResponseBodyLayerTasks(DaraModel):
    def __init__(
        self,
        artifact_digest: str = None,
        digest: str = None,
        size: int = None,
        sync_layer_task_id: str = None,
        synced_size: int = None,
        task_status: str = None,
    ):
        # The digest of the artifact.
        self.artifact_digest = artifact_digest
        # The digest of the image layer.
        self.digest = digest
        # The size of synchronized image layers.
        self.size = size
        # The ID of the synchronization task for the image layer.
        self.sync_layer_task_id = sync_layer_task_id
        # The size of the image layer that is synchronized.
        self.synced_size = synced_size
        # The status of the synchronization task. Valid values:
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_digest is not None:
            result['ArtifactDigest'] = self.artifact_digest

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.size is not None:
            result['Size'] = self.size

        if self.sync_layer_task_id is not None:
            result['SyncLayerTaskId'] = self.sync_layer_task_id

        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactDigest') is not None:
            self.artifact_digest = m.get('ArtifactDigest')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SyncLayerTaskId') is not None:
            self.sync_layer_task_id = m.get('SyncLayerTaskId')

        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class GetRepoSyncTaskResponseBodyImageTo(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        return self

class GetRepoSyncTaskResponseBodyImageFrom(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        return self

