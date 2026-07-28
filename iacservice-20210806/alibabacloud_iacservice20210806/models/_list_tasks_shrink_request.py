# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTasksShrinkRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        kms_key_id: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        tag_shrink: str = None,
        task_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # The keyword for fuzzy search by task ID or task name.
        self.keyword = keyword
        self.kms_key_id = kms_key_id
        # The module ID.
        self.module_id = module_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Minimum value: 1. Maximum value: 100.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The job status. Valid values:
        # 
        # - Planning: The job is in the Plan execution phase.
        # - Planned: The job has completed the Plan execution.
        # - PlannedAndFinished: After the Plan execution is completed, no diff is found, and the job enters the final state.
        # - Applying: The job is in the Apply execution phase.
        # - Applied: The job has completed the Apply execution.
        # - Errored: The job execution encountered errors and entered the final state.
        self.status = status
        # The list of task tags.
        self.tag_shrink = tag_shrink
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        if self.module_id is not None:
            result['moduleId'] = self.module_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.status is not None:
            result['status'] = self.status

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

