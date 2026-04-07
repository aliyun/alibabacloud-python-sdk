# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDISyncTaskConfigForUpdatingRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: int = None,
        task_id: int = None,
        task_param: str = None,
        task_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. This parameter is used to prevent repeated operations that are caused by multiple calls.
        self.client_token = client_token
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The task ID.
        # 
        # *   If you set the TaskType parameter to DI_REALTIME, set the TaskId parameter to the value of the FileId parameter for the real-time synchronization task.
        # *   If you set the TaskType parameter to DI_SOLUTION, set the TaskId parameter to the value of the FileId parameter for the synchronization solution.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The script for updating the real-time synchronization task in Data Integration. DataWorks allows you to add or remove tables for a real-time synchronization task in Data Integration only in asynchronous mode. The following types of real-time synchronization tasks are supported:
        # 
        # *   Synchronization task that is used to synchronize data from MySQL to MaxCompute
        # *   Synchronization task that is used to synchronize data from MySQL data to Kafka
        # *   Synchronization task that is used to synchronize data from MySQL to Hologres
        # 
        # The SelectedTables parameter is used to specify tables that you want to synchronize from multiple databases. The Tables parameter is used to specify tables that you want to synchronize from a single database.
        # 
        # *   If the script contains the SelectedTables parameter, the system synchronizes data from the tables that you specify in the SelectedTables parameter.
        # *   If the script contains the Tables parameter, the system synchronizes data from the tables that you specify in the Tables parameter.
        # 
        # This parameter is required.
        self.task_param = task_param
        # The type of the object that you want to update in Data Integration in asynchronous mode. Valid values:
        # 
        # *   DI_REALTIME: real-time synchronization task
        # *   DI_SOLUTION: synchronization solution DataWorks allows you to create or update real-time synchronization tasks in Data Integration only in asynchronous mode.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

