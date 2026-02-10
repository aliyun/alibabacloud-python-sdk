# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageFixTaskResponseBody(DaraModel):
    def __init__(
        self,
        build_tasks: List[main_models.DescribeImageFixTaskResponseBodyBuildTasks] = None,
        page_info: main_models.DescribeImageFixTaskResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The tasks returned.
        self.build_tasks = build_tasks
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.build_tasks:
            for v1 in self.build_tasks:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildTasks'] = []
        if self.build_tasks is not None:
            for k1 in self.build_tasks:
                result['BuildTasks'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_tasks = []
        if m.get('BuildTasks') is not None:
            for k1 in m.get('BuildTasks'):
                temp_model = main_models.DescribeImageFixTaskResponseBodyBuildTasks()
                self.build_tasks.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageFixTaskResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageFixTaskResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of tasks returned on the current page.
        self.count = count
        # The page number of the returned page. Default value: **1**
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**
        self.page_size = page_size
        # The total number of tasks returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageFixTaskResponseBodyBuildTasks(DaraModel):
    def __init__(
        self,
        build_task_id: str = None,
        finish_time: str = None,
        fix_time: str = None,
        new_tag: str = None,
        new_uuid: str = None,
        old_tag: str = None,
        old_uuid: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        status: int = None,
        task_type: str = None,
        vul_alias: str = None,
    ):
        # The ID of the task.
        self.build_task_id = build_task_id
        # The timestamp when the task starts. Unit: milliseconds.
        self.finish_time = finish_time
        # The timestamp when the task ends. Unit: milliseconds.
        self.fix_time = fix_time
        # The version of the image after image risks are fixed.
        self.new_tag = new_tag
        # The UUID of the image after image risks are fixed.
        self.new_uuid = new_uuid
        # The version of the image.
        self.old_tag = old_tag
        # The UUID of the image.
        self.old_uuid = old_uuid
        # The region of the image.
        self.region_id = region_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace of the image.
        self.repo_namespace = repo_namespace
        # The status of the task. Valid values:
        # 
        # *   **1**: The task is running.
        # *   **2**: The task is successful.
        # *   **3**: The task failed.
        self.status = status
        # The type of the task. The value is fixed as IMAGE_REPAIR. The value indicates a task that fixes image risks.
        self.task_type = task_type
        # The alias of the fixed vulnerability.
        self.vul_alias = vul_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.fix_time is not None:
            result['FixTime'] = self.fix_time

        if self.new_tag is not None:
            result['NewTag'] = self.new_tag

        if self.new_uuid is not None:
            result['NewUuid'] = self.new_uuid

        if self.old_tag is not None:
            result['OldTag'] = self.old_tag

        if self.old_uuid is not None:
            result['OldUuid'] = self.old_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.vul_alias is not None:
            result['VulAlias'] = self.vul_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('FixTime') is not None:
            self.fix_time = m.get('FixTime')

        if m.get('NewTag') is not None:
            self.new_tag = m.get('NewTag')

        if m.get('NewUuid') is not None:
            self.new_uuid = m.get('NewUuid')

        if m.get('OldTag') is not None:
            self.old_tag = m.get('OldTag')

        if m.get('OldUuid') is not None:
            self.old_uuid = m.get('OldUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VulAlias') is not None:
            self.vul_alias = m.get('VulAlias')

        return self

