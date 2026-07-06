# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoSyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sync_tasks: List[main_models.ListRepoSyncTaskResponseBodySyncTasks] = None,
        total_count: str = None,
    ):
        # The return code.
        self.code = code
        # Whether the request was successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # A list of sync tasks.
        self.sync_tasks = sync_tasks
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.sync_tasks:
            for v1 in self.sync_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SyncTasks'] = []
        if self.sync_tasks is not None:
            for k1 in self.sync_tasks:
                result['SyncTasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sync_tasks = []
        if m.get('SyncTasks') is not None:
            for k1 in m.get('SyncTasks'):
                temp_model = main_models.ListRepoSyncTaskResponseBodySyncTasks()
                self.sync_tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoSyncTaskResponseBodySyncTasks(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        cross_user: bool = None,
        custom_link: bool = None,
        image_from: main_models.ListRepoSyncTaskResponseBodySyncTasksImageFrom = None,
        image_to: main_models.ListRepoSyncTaskResponseBodySyncTasksImageTo = None,
        link_id: str = None,
        modifed_time: int = None,
        modified_time: int = None,
        sync_batch_task_id: str = None,
        sync_rule_id: str = None,
        sync_task_id: str = None,
        sync_trans_accelerate: bool = None,
        task_issue: str = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        # The creation time of the task.
        self.create_time = create_time
        # Whether the image is synchronized across accounts. Valid values:
        # 
        # - `true`: The image is synchronized across accounts.
        # 
        # - `false`: The image is synchronized within the same account.
        # 
        # Default value: `false`
        self.cross_user = cross_user
        # Whether a custom sync link is used.
        self.custom_link = custom_link
        # The source image.
        self.image_from = image_from
        # The destination image.
        self.image_to = image_to
        # The ID of the custom sync link.
        self.link_id = link_id
        # This parameter is deprecated due to a typo. Use `ModifiedTime` instead.
        self.modifed_time = modifed_time
        # The modification time of the task.
        self.modified_time = modified_time
        # The ID of the batch sync task. This ID is the same as the sync record ID (`SyncRecordId`).
        # 
        # > If an image matches multiple sync rules, multiple sync tasks are generated. These tasks share the same `SyncBatchTaskId`.
        self.sync_batch_task_id = sync_batch_task_id
        # The ID of the sync rule.
        self.sync_rule_id = sync_rule_id
        # The ID of the sync task.
        self.sync_task_id = sync_task_id
        # Whether transfer acceleration is enabled for the sync task.
        self.sync_trans_accelerate = sync_trans_accelerate
        # The task failure information.
        # 
        # > If the sync task fails, this field returns details about the failure.
        self.task_issue = task_issue
        # The task status.
        self.task_status = task_status
        # The trigger policy. Valid values:
        # 
        # - `PASSIVE`: The sync task is automatically triggered.
        # 
        # - `INITIATIVE`: The sync task is manually triggered.
        # 
        # Default value: `PASSIVE`
        self.task_trigger = task_trigger

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user

        if self.custom_link is not None:
            result['CustomLink'] = self.custom_link

        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()

        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()

        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.modifed_time is not None:
            result['ModifedTime'] = self.modifed_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id

        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id

        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id

        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate

        if self.task_issue is not None:
            result['TaskIssue'] = self.task_issue

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')

        if m.get('CustomLink') is not None:
            self.custom_link = m.get('CustomLink')

        if m.get('ImageFrom') is not None:
            temp_model = main_models.ListRepoSyncTaskResponseBodySyncTasksImageFrom()
            self.image_from = temp_model.from_map(m.get('ImageFrom'))

        if m.get('ImageTo') is not None:
            temp_model = main_models.ListRepoSyncTaskResponseBodySyncTasksImageTo()
            self.image_to = temp_model.from_map(m.get('ImageTo'))

        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('ModifedTime') is not None:
            self.modifed_time = m.get('ModifedTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')

        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')

        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')

        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')

        if m.get('TaskIssue') is not None:
            self.task_issue = m.get('TaskIssue')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')

        return self

class ListRepoSyncTaskResponseBodySyncTasksImageTo(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The image tag.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the region.
        self.region_id = region_id
        # The repository name.
        self.repo_name = repo_name
        # The repository namespace.
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

class ListRepoSyncTaskResponseBodySyncTasksImageFrom(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The image tag.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the region.
        self.region_id = region_id
        # The repository name.
        self.repo_name = repo_name
        # The repository namespace.
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

