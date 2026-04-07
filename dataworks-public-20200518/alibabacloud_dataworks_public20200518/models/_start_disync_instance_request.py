# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDISyncInstanceRequest(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        start_param: str = None,
        task_type: str = None,
    ):
        # *   If you set TaskType to DI_REALTIME, set this parameter to the ID of the real-time synchronization task that you want to start.
        # *   If you set TaskType to DI_SOLUTION, set this parameter to the ID of the data synchronization solution that you want to start.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # *   If you set TaskType to DI_REALTIME, the StartParam parameter specifies the startup parameters for the real-time synchronization task. The startup parameters include failover-related parameters, the parameter that specifies the number of dirty data records allowed, and the parameters in the data definition language (DDL) statements.
        # *   If you set TaskType to DI_SOLUTION, the StartParam parameter does not take effect.
        self.start_param = start_param
        # The type of the object that you want to start. Valid values:
        # 
        # *   DI_REALTIME: real-time synchronization task
        # *   DI_SOLUTION: data synchronization solution
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

        if self.start_param is not None:
            result['StartParam'] = self.start_param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartParam') is not None:
            self.start_param = m.get('StartParam')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

