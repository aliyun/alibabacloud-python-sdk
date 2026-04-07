# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDISyncTaskConfigProcessResultRequest(DaraModel):
    def __init__(
        self,
        async_process_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        # The asynchronous thread ID. You can call the [GenerateDISyncTaskConfigForCreating](https://help.aliyun.com/document_detail/383463.html) or [GenerateDISyncTaskConfigForUpdating](https://help.aliyun.com/document_detail/383464.html) operation to obtain the ID.
        # 
        # *   The GenerateDISyncTaskConfigForCreating operation is used to generate the ID of the asynchronous thread that is used to create a real-time synchronization task in Data Integration.
        # *   The GenerateDISyncTaskConfigForUpdating operation is used to generate the ID of the asynchronous thread that is used to update a real-time synchronization task in Data Integration.
        # 
        # This parameter is required.
        self.async_process_id = async_process_id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the object that you want to create or update in Data Integration in asynchronous mode. Valid values:
        # 
        # *   DI_REALTIME: real-time synchronization task
        # *   DI_SOLUTION: synchronization solution DataWorks allows you to create or update real-time synchronization tasks and synchronization solutions in Data Integration only in asynchronous mode.
        # 
        # Valid values:
        # 
        # *   DI_OFFLINE
        # *   DI_REALTIME
        # *   DI_SOLUTION
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
        if self.async_process_id is not None:
            result['AsyncProcessId'] = self.async_process_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncProcessId') is not None:
            self.async_process_id = m.get('AsyncProcessId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

