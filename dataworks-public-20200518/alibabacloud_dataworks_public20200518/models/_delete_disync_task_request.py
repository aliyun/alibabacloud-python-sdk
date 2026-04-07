# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDISyncTaskRequest(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        # The ID of the real-time synchronization task. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the task. Set the value to DI_REALTIME, which indicates a real-time synchronization task.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

